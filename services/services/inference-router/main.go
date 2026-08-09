package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/voice-detect/inference-router/config"
	"github.com/voice-detect/inference-router/router"
)

func main() {
	cfg := config.LoadConfig()
	r, err := router.NewRouter(cfg)
	if err != nil {
		log.Fatalf("fatal: %v", err)
	}

	ctx, cancel := context.WithCancel(context.Background())
	
	go func() {
		if err := r.Run(ctx); err != nil {
			log.Printf("error: %v", err)
		}
	}()

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c
	cancel()
}
