package config

import (
	"os"
	"strings"
)

type Config struct {
	KafkaBrokers []string
	InputTopic   string
	OutputTopic  string
	TritonURL    string
}

func LoadConfig() *Config {
	brokers := os.Getenv("KAFKA_BROKERS")
	if brokers == "" {
		brokers = "localhost:9092"
	}
	return &Config{
		KafkaBrokers: strings.Split(brokers, ","),
		InputTopic:   os.Getenv("INPUT_TOPIC"),
		OutputTopic:  os.Getenv("OUTPUT_TOPIC"),
		TritonURL:    os.Getenv("TRITON_URL"),
	}
}
