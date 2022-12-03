import pika
from pika.exchange_type import ExchangeType
from dotenv import load_dotenv
import os
load_dotenv()

# parameters = pika.ConnectionParameters(host='localhost',heartbeat=600,blocked_connection_timeout=300)

url_string = os.getenv('url_exchange')
parameters = pika.URLParameters(url=url_string)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.exchange_declare(exchange='ECommerce', exchange_type=ExchangeType.fanout)


# exchange is between  channel pub and queue
# exchange bind data to many queue

def publish(method, body, routing_key):
    properties = pika.BasicProperties(method)
    properties.expiration = str(60 * 9)
    channel.basic_publish(exchange='ECommerce', routing_key=routing_key, body=body, properties=properties)
    # channel push message to queue with exchange is logs
