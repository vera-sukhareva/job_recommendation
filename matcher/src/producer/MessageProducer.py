from typing import List


class MessageProducer:
    def publish(self, user_id: int, recommendations: List[str]) -> bool:
        print(user_id, recommendations)
        return True


messageProducer = MessageProducer()