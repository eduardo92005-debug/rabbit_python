import pika

#Create a list of messages to send to a queue
messages = ['test','hello','world']
#Create connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Create a queue called hello
channel.queue_declare(queue='hello')

#Function to send multiple messages to a queue
def send_multiple_messages(messages):
    for message in messages:
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print (f" [x] Sent '{message}'")

send_multiple_messages(messages)
connection.close()