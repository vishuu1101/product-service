from fastapi import APIRouter, Depends
from dto import AddProductRequest, AddProductResponse
from services import ProductService

router = APIRouter()

class ProductRoutes:

    async def add_product(self, addProductRequest: AddProductRequest,
                           product_service: ProductService = Depends(ProductService)) -> AddProductResponse:
        # Call the service layer to process the product and generate embeddings
        response = product_service.add_product(addProductRequest)
        return response

product_routes = ProductRoutes()

# Register the route with the router manually
router.add_api_route("/add-product/", product_routes.add_product, methods=["POST"])
