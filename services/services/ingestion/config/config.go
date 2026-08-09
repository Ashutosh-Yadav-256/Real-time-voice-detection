package config

import (
	"os"
	"strings"
)

type Config struct {
	KafkaBrokers []string
	KafkaTopic   string
	ListenAddr   string
}

func LoadConfig() *Config {
	brokers := os.Getenv("KAFKA_BROKERS")
	if brokers == "" {
		brokers = "localhost:9092"
	}
	topic := os.Getenv("KAFKA_TOPIC")
	if topic == "" {
		topic = "raw-audio"
	}
	addr := os.Getenv("LISTEN_ADDR")
	if addr == "" {
		addr = ":50051"
	}
	return &Config{
		KafkaBrokers: strings.Split(brokers, ","),
		KafkaTopic:   topic,
		ListenAddr:   addr,
	}
}
