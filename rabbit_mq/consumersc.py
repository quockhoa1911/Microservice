import json
import pika
from pika.exchange_type import ExchangeType

# parameters = pika.ConnectionParameters(host='localhost', heartbeat=600, blocked_connection_timeout=300)
parameters = pika.URLParameters(url='amqps://muyiopsb:4R6fvWb-BVHIc2cqTZDWY-5XQjKkn05o@armadillo.rmq.cloudamqp.com/muyiopsb')

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.exchange_declare(exchange='ECommerce', exchange_type=ExchangeType.fanout)
#name of exchange define(declare)

channel.queue_declare(queue='Secondqueue', exclusive=True)
# name of queue define(declare)

channel.queue_bind(queue='Secondqueue', exchange='ECommerce', routing_key='test')
# binding data from exchange and name of queue


def callback(ch, method, properties, body):
    print("received from test and second comsumer")
    print(body)
    print(properties)
    print(properties.content_type)


channel.basic_consume(queue='Secondqueue', on_message_callback=callback, auto_ack=True)
# channel is watting and consume message with name queue if message send in queue handle equal callback funtion
print('started consuming')
channel.start_consuming()  # channel start consume
