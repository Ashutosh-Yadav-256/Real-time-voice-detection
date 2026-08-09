package router

import (
	"context"
	"encoding/json"
	"fmt"
	"time"

	"github.com/voice-detect/inference-router/config"
	"github.com/voice-detect/inference-router/triton"
	"github.com/IBM/sarama"
)

type Router struct {
	consumer sarama.Consumer
	producer sarama.SyncProducer
	triton   *triton.Client
	cfg      *config.Config
}

func NewRouter(cfg *config.Config) (*Router, error) {
	c, err := sarama.NewConsumer(cfg.KafkaBrokers, nil)
	if err != nil {
		return nil, err
	}
	
	pconfig := sarama.NewConfig()
	pconfig.Producer.Return.Successes = true
	p, err := sarama.NewSyncProducer(cfg.KafkaBrokers, pconfig)
	if err != nil {
		return nil, err
	}

	t, err := triton.NewClient(cfg.TritonURL)
	if err != nil {
		return nil, err
	}

	return &Router{
		consumer: c,
		producer: p,
		triton:   t,
		cfg:      cfg,
	}, nil
}

func (r *Router) Run(ctx context.Context) error {
	pc, err := r.consumer.ConsumePartition(r.cfg.InputTopic, 0, sarama.OffsetNewest)
	if err != nil {
		return err
	}
	defer pc.Close()

	for {
		select {
		case <-ctx.Done():
			return nil
		case msg := <-pc.Messages():
			var req map[string]interface{}
			if err := json.Unmarshal(msg.Value, &req); err != nil {
				continue
			}

			prob, label, err := r.triton.Infer(ctx, req)
			if err != nil {
				continue
			}

			res := map[string]interface{}{
				"stream_id":    req["stream_id"],
				"timestamp_ms": req["timestamp_ms"],
				"probability":  prob,
				"label":        label,
				"event_id":     fmt.Sprintf("%v-%v", req["stream_id"], time.Now().UnixNano()),
			}

			data, _ := json.Marshal(res)
			r.producer.SendMessage(&sarama.ProducerMessage{
				Topic: r.cfg.OutputTopic,
				Key:   sarama.StringEncoder(res["stream_id"].(string)),
				Value: sarama.ByteEncoder(data),
			})
		}
	}
}
