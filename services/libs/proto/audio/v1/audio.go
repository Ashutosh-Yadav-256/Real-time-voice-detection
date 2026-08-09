package v1

import (
	"context"
	"google.golang.org/grpc"
)

type AudioChunk struct {
	StreamID    string `json:"stream_id"`
	TimestampMs int64  `json:"timestamp_ms"`
	Payload     []byte `json:"payload"`
	Format      string `json:"format"`
	SampleRate  int32  `json:"sample_rate"`
	Channels    int32  `json:"channels"`
}

type DetectionEvent struct {
	EventID     string  `json:"event_id"`
	StreamID    string  `json:"stream_id"`
	TimestampMs int64   `json:"timestamp_ms"`
	Probability float32 `json:"probability"`
	Label       string  `json:"label"`
}

type IngestRequest struct {
	Chunk *AudioChunk `json:"chunk"`
}

type IngestResponse struct {
	Success      bool   `json:"success"`
	ErrorMessage string `json:"error_message"`
}

type DetectionResult struct {
	RequestID   string  `json:"request_id"`
	StreamID    string  `json:"stream_id"`
	Probability float32 `json:"probability"`
	Label       string  `json:"label"`
}

type AudioIngressClient interface {
	IngestAudio(ctx context.Context, opts ...grpc.CallOption) (AudioIngress_IngestAudioClient, error)
}

type AudioIngress_IngestAudioClient interface {
	Send(*IngestRequest) error
	CloseAndRecv() (*IngestResponse, error)
	grpc.ClientStream
}

type AudioIngressServer interface {
	IngestAudio(AudioIngress_IngestAudioServer) error
}

type AudioIngress_IngestAudioServer interface {
	SendAndClose(*IngestResponse) error
	Recv() (*IngestRequest, error)
	grpc.ServerStream
}

type UnimplementedAudioIngressServer struct{}

func (UnimplementedAudioIngressServer) IngestAudio(AudioIngress_IngestAudioServer) error {
	return nil
}

func RegisterAudioIngressServer(s *grpc.Server, srv AudioIngressServer) {
}
