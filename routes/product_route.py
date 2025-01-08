from fastapi import APIRouter, Depends
from dto import AddProductRequest, AddProductResponse, GetVectorRequest, GetVectorResponse
from services import ProductService

router = APIRouter()

class ProductRoutes:

    async def add_product(self, addProductRequest: AddProductRequest,
                           product_service: ProductService = Depends(ProductService)) -> AddProductResponse:
        # Call the service layer to process the product and generate embeddings
        response = product_service.add_product(addProductRequest)
        return response
    
    async def get_vector_for_text(self, request: GetVectorRequest, product_service: ProductService = Depends(ProductService)) -> GetVectorResponse:
        response = product_service.get_vector_for_text(request.search_text)
        return GetVectorResponse(embedding=response)

product_routes = ProductRoutes()

# Register the route with the router manually
router.add_api_route("/add", product_routes.add_product, methods=["POST"])
router.add_api_route("/get-vector", product_routes.get_vector_for_text, methods=["POST"])
