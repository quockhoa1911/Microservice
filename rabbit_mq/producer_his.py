import pika
from pika.exchange_type import ExchangeType
from dotenv import load_dotenv
import os
load_dotenv()


def publish_history(method, body, routing_key):
    url_string = os.getenv('url_exchange_history')

    parameters = pika.URLParameters(url=url_string)

    connection = pika.BlockingConnection(parameters=parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange='ECommerce', exchange_type=ExchangeType.fanout)

    # exchange(trao doi) is between  channel pub and queue
    # exchange bind data to many queue
    properties = pika.BasicProperties(method)
    properties.expiration = str(60 * 9)
    channel.basic_publish(exchange='ECommerce', routing_key=routing_key, body=body, properties=properties)
    channel.close()
    # channel push message to queue with exchange is logs
