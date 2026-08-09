import os


class Config:
    def __init__(self):
        self.kafka_brokers = os.getenv('KAFKA_BROKERS', 'localhost:9092')
        self.input_topic = os.getenv('INPUT_TOPIC', 'raw-audio')
        self.output_topic = os.getenv('OUTPUT_TOPIC', 'preprocessed-audio')
        self.group_id = os.getenv('GROUP_ID', 'preprocessor-group')
        self.target_sample_rate = int(os.getenv('TARGET_SAMPLE_RATE', '16000'))
