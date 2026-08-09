module github.com/voice-detect/ingestion

go 1.22

require (
	github.com/IBM/sarama v1.42.1
	github.com/voice-detect/proto v0.0.0
	google.golang.org/grpc v1.61.0
	google.golang.org/protobuf v1.32.0
)

replace github.com/voice-detect/proto => ../../libs/proto


