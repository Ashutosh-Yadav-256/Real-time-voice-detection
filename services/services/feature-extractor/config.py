import os


class Config:
    def __init__(self):
        self.kafka_brokers = os.getenv('KAFKA_BROKERS', 'localhost:9092')
        self.input_topic = os.getenv('INPUT_TOPIC', 'preprocessed-audio')
        self.output_topic = os.getenv('OUTPUT_TOPIC', 'inference-requests')
        self.group_id = os.getenv('GROUP_ID', 'feature-extractor-group')
