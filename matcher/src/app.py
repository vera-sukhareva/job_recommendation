from src.consumer.MessageConsumer import messageConsumer
from flask import Flask

app = Flask(__name__)
messageConsumer.start()
