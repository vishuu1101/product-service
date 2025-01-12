from dto import AddProductRequest, AddProductResponse, MessageDTO
from rabbitmq import publish_to_rabbitmq
from util.text_util import encode_text
from fastapi import Depends
import requests


class ProductService:

    def add_product(self, addProductRequest: AddProductRequest) -> AddProductResponse:
        embedData = encode_text(addProductRequest.searchText)
        response = AddProductResponse(name=addProductRequest.name,
                                      pvid=addProductRequest.pvid,
                                      pmid=addProductRequest.pmid,
                                      searchText=addProductRequest.searchText,
                                      category=addProductRequest.category,
                                      price=addProductRequest.price,
                                       embedding=embedData)
        messageDTO = MessageDTO(pattern='product-info.vector-embed.successful', data=response.model_dump_json())
        publish_to_rabbitmq(messageDTO.model_dump_json(), 'product-info.vector-embed.successful')
        return response
    
    def get_vector_for_text(self, search_text: str):
        embedData = encode_text(search_text)
        return embedData