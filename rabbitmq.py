import pika
from fastapi import HTTPException
from config import load_config

config = load_config()

# Load RabbitMQ details from the configuration
rabbitmq_host = config['rabbitmq_host']
exchange_name = config['exchange_name']

def publish_to_rabbitmq(message: str, routing_key: str):
    try:
        # Establish RabbitMQ connection
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()

        # Declare exchange and queue
        channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

        # Publish message to RabbitMQ
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
        print(f"Message sent: '{message}' with routing key: '{routing_key}'")

        # Close the connection
        connection.close()
    except Exception as e:
        print(f"Error publishing to RabbitMQ: {e}")
        raise HTTPException(status_code=500, detail="Failed to send message to RabbitMQ")
