from src.Matcher import matcher
from src.model.Resume import Resume
from src.producer.MessageProducer import messageProducer


class MessageConsumer:
    def consume(self, resume: Resume, user_id: int) -> bool:
        recommendations = matcher.recommend(resume)
        messageProducer.publish(user_id, recommendations)
        return True


messageConsumer = MessageConsumer()