from dto import AddProductRequest, AddProductResponse, MessageDTO
from rabbitmq import publish_to_rabbitmq

class ProductService:

    def add_product(self, addProductRequest: AddProductRequest) -> AddProductResponse:
        response = AddProductResponse(name=addProductRequest.name)
        messageDTO = MessageDTO(pattern='product-info.vector-embed.successful', data=response.model_dump_json())
        publish_to_rabbitmq(messageDTO.model_dump_json(), 'product-info.vector-embed.successful')
        return response