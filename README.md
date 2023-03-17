Example RabbitMQ for test using

## 📋 Description
RabbitMQ is a messaging broker that enables software applications to communicate with each other by sending and receiving messages in a distributed system. It is open-source and implements the Advanced Message Queuing Protocol (AMQP), which is a messaging standard for enterprise messaging. RabbitMQ provides a flexible and scalable platform for decoupling application components, increasing system reliability, and enabling asynchronous communication between applications. It supports various messaging patterns such as point-to-point, publish/subscribe, and request/reply. RabbitMQ also provides features such as message durability, message acknowledgments, and dead-letter queues to enhance the reliability and resiliency of the messaging system. It is written in Erlang and can be easily integrated with various programming languages such as Python, Java, and .NET. RabbitMQ is widely used in various industries and applications, including finance, healthcare, telecommunications, and e-commerce.

## 📦 How to use
## Install docker
1. Install Docker on your machine, if you haven't already done so.

2. Open your terminal or command prompt and execute the following command to download the RabbitMQ image:

3. ```docker pull rabbitmq```

4. Once the image is downloaded, run the following command to start a RabbitMQ container on port 8080:

6. ```docker run -d --name rabbitmq -p 8080:5672 -p 15672:15672 rabbitmq```

7. This command will start a RabbitMQ container and expose port 8080 for AMQP and port 15672 for management.

8. After the container is started, you can verify that RabbitMQ is running by accessing the RabbitMQ management console at http://localhost:15672. The default username and password are both guest.

9. You can also use the docker logs command to view the logs of the RabbitMQ container.

10. ```docker logs rabbitmq```
### Install package pika in python
1. ```python3 -m pip install pika```
### Use RabbitMQ
1. Enter in browser: localhost:8080
2. Username: guest; Password: guest
3. Run send.py: ```python3 send.py```
4. Run receiver.py: ```python3 receiver.py```
5. Now check the queue and messages in the receiver terminal!

