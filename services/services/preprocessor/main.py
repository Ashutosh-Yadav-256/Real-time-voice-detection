import json
import logging

try:
    from confluent_kafka import Consumer, Producer
except ImportError:
    Consumer = Producer = None
from config import Config
from processor import AudioProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    cfg = Config()
    consumer = Consumer({
        'bootstrap.servers': cfg.kafka_brokers,
        'group.id': cfg.group_id,
        'auto.offset.reset': 'earliest'
    })
    producer = Producer({'bootstrap.servers': cfg.kafka_brokers})
    processor = AudioProcessor(target_sr=cfg.target_sample_rate)

    consumer.subscribe([cfg.input_topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logger.error(str(msg.error()))
                continue

            try:
                data = json.loads(msg.value().decode('utf-8'))
                processed = processor.process(data)
                if processed:
                    producer.produce(
                        cfg.output_topic,
                        key=processed['stream_id'],
                        value=json.dumps(processed)
                    )
                    producer.poll(0)
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                logger.error(str(e))
    finally:
        consumer.close()
        producer.flush()

if __name__ == '__main__':
    main()
