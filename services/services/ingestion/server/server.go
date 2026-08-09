package server

import (
	"context"
	"io"
	"github.com/voice-detect/ingestion/kafka"
	pb "github.com/voice-detect/proto/audio/v1"
)

type IngressServer struct {
	pb.UnimplementedAudioIngressServer
	producer *kafka.Producer
}

func NewIngressServer(p *kafka.Producer) *IngressServer {
	return &IngressServer{producer: p}
}

func (s *IngressServer) IngestAudio(stream pb.AudioIngress_IngestAudioServer) error {
	for {
		req, err := stream.Recv()
		if err == io.EOF {
			return stream.SendAndClose(&pb.IngestResponse{Success: true})
		}
		if err != nil {
			return err
		}
		
		err = s.producer.Publish(context.Background(), req.Chunk)
		if err != nil {
			return stream.SendAndClose(&pb.IngestResponse{
				Success: false,
				ErrorMessage: err.Error(),
			})
		}
	}
}
