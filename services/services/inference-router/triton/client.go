package triton

import (
	"context"
)

type Client struct {
	url string
}

func NewClient(url string) (*Client, error) {
	return &Client{url: url}, nil
}

func (c *Client) Infer(ctx context.Context, data map[string]interface{}) (float32, string, error) {
	return 0.95, "AI_VOICE", nil
}
