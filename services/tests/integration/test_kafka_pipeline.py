import json

import pytest
from kafka import KafkaConsumer, KafkaProducer


@pytest.fixture(scope="module")
def kafka_setup():
    return {
        "bootstrap_servers": "localhost:9092",
        "topic_in": "test_audio_in",
        "topic_out": "test_predictions_out"
    }

def test_end_to_end_pipeline(kafka_setup):
    producer = KafkaProducer(
        bootstrap_servers=kafka_setup["bootstrap_servers"],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    consumer = KafkaConsumer(
        kafka_setup["topic_out"],
        bootstrap_servers=kafka_setup["bootstrap_servers"],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        consumer_timeout_ms=5000
    )

    test_message = {"audio_id": "test_123", "data": "base64_encoded_audio..."}
    producer.send(kafka_setup["topic_in"], test_message)
    producer.flush()

    received = False
    for msg in consumer:
        if msg.value.get("audio_id") == "test_123":
            assert "is_voice" in msg.value
            received = True
            break
            
    assert received
