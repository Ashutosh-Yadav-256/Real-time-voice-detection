package main

import (
	"log"
	"net"
	"os"
	"os/signal"
	"syscall"

	"github.com/voice-detect/ingestion/config"
	"github.com/voice-detect/ingestion/kafka"
	"github.com/voice-detect/ingestion/server"
	pb "github.com/voice-detect/proto/audio/v1"

	"google.golang.org/grpc"
)

func main() {
	cfg := config.LoadConfig()
	prod, err := kafka.NewProducer(cfg.KafkaBrokers, cfg.KafkaTopic)
	if err != nil {
		log.Fatalf("fatal: %v", err)
	}
	defer prod.Close()

	lis, err := net.Listen("tcp", cfg.ListenAddr)
	if err != nil {
		log.Fatalf("fatal: %v", err)
	}

	grpcServer := grpc.NewServer()
	srv := server.NewIngressServer(prod)
	pb.RegisterAudioIngressServer(grpcServer, srv)

	go func() {
		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalf("fatal: %v", err)
		}
	}()

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c
	grpcServer.GracefulStop()
}
