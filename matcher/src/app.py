from flask import Flask
from src.consumer.MessageConsumer import messageConsumer

app = Flask(__name__)
messageConsumer.start()
