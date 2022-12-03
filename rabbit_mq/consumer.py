import pika
from pika.exchange_type import ExchangeType
from consumer_decorator import consumer_decorator
from consumer_service import Consumer_service

parameters = pika.URLParameters(
    url='amqps://muyiopsb:4R6fvWb-BVHIc2cqTZDWY-5XQjKkn05o@armadillo.rmq.cloudamqp.com/muyiopsb')

# parameters = pika.URLParameters('amqps://fkvbbddc:ALJpxxB4zIfIpYbwN2DhTqFPpzIcc46R@armadillo.rmq.cloudamqp.com
# /fkvbbddc')

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.exchange_declare(exchange='ECommerce', exchange_type=ExchangeType.fanout)
# name of exchange define(declare)

channel.queue_declare(queue='IAM-sv1', durable=True, arguments=None, auto_delete=False, exclusive=False)
# name of queue define(declare)

channel.queue_bind(queue='IAM-sv1', exchange='ECommerce', routing_key='test')


# binding data from exchange and name of queue


# if function parammeter have call and receive parammeter is value -> decorator receive argument
# when call back is start it receive value argument so decorator is receive value argument


@consumer_decorator
def callback(ch, method, properties, body):
    print("consumer is handle in inner decorator")
    print("function call back receive in queue")



channel.basic_consume(queue='IAM-sv1', on_message_callback=callback, auto_ack=False)

# channel is watting and consume message with name queue is test if message send in queue handle equal callback funtion
print('started consuming')
channel.start_consuming()  # channel start consume
