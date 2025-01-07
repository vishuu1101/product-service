from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rabbitmq import publish_to_rabbitmq

# Define the message payload
class MessageRequest(BaseModel):
    message: str
    routing_key: str

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}


@app.post("/send_message")
async def send_message(request: MessageRequest):
    # Publish the message to RabbitMQ using the imported function
    publish_to_rabbitmq(request.message, request.routing_key)
    return {"status": "Message sent to RabbitMQ", "message": request.message, "routing_key": request.routing_key}
