from src.model.Resume import Resume


class MessageProducer:
    def publish(self, resume: Resume, user_id: int) -> bool:
        return True


messageProducer = MessageProducer()
