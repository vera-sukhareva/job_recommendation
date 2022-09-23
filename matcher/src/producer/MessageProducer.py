import json
from typing import List

from kafka import KafkaProducer

from src.utils.constants import Urls
from src.utils.Topics import Topics


class MessageProducer:
    def publish(self, user_id: int, recommendations: List[str]) -> bool:
        producer = KafkaProducer(bootstrap_servers=Urls.KAFKA_HOSTNAME,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send(Topics.RECOMMENDATION_EVENT, {'user_id': user_id,
                                                    'recommendations': recommendations})
        return True


messageProducer = MessageProducer()
