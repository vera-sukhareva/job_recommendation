import json

from kafka import KafkaProducer

from src.utils.constants import Urls
from src.model.resume.Resume import Resume
from src.utils.Topics import Topics


class MessageProducer:
    def publish(self, resume: Resume, user_id: int):
        producer = KafkaProducer(bootstrap_servers=Urls.KAFKA_HOSTNAME,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send(Topics.RESUME_EVENT, {"user_id": user_id, "resume": resume.to_json()})


messageProducer = MessageProducer()
