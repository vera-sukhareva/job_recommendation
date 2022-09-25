import json
import threading

from kafka import KafkaConsumer

from src.utils.constants import Urls
from src.matcher.Matcher import matcher
from src.model.Resume import Resume
from src.producer.MessageProducer import messageProducer
from src.utils.Topics import Topics


class MessageConsumer(threading.Thread):
    def run(self):
        consumer = KafkaConsumer(Topics.RESUME_EVENT,
                                 bootstrap_servers=Urls.KAFKA_HOSTNAME,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 group_id='group_1',
                                 )
        for msg in consumer:
            event_data = msg.value
            print("consumed", event_data)
            self._handle(event_data['user_id'], event_data['resume'])
            print("recommendation finished")

    def _handle(self, user_id: int, resume_json: dict):
        resume = self._map_to_resume(resume_json)
        recommendations = matcher.recommend(resume, 5)
        messageProducer.publish(user_id, recommendations)

    def _map_to_resume(self, resume_json: dict) -> Resume:
        resume = Resume(
            resume_json['name'],
            resume_json['email'],
            resume_json['skills'],
            resume_json['experience']
        )
        resume.id = resume_json['id']
        return resume


messageConsumer = MessageConsumer()
