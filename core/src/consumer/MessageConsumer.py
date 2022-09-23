import json
import threading
from typing import List

from kafka import KafkaConsumer

from src.constants import Urls
from src.servicies.UserService import userService
from src.utils.Topics import Topics


class MessageConsumer(threading.Thread):

    def run(self):
        consumer = KafkaConsumer(Topics.RECOMMENDATION_EVENT,
                                 bootstrap_servers=Urls.KAFKA_HOSTNAME,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 group_id='group_2')
        for msg in consumer:
            event_data = msg.value
            print("consumed:", event_data)
            self._handle(event_data['user_id'], event_data['recommendations'])
            print("user updated with recommendation")

    def _handle(self, user_id: int, recommendations: List[str]):
        user = userService.get_by_id(user_id)
        user.recommendations = recommendations
        userService.update_user(user)


messageConsumer = MessageConsumer()
