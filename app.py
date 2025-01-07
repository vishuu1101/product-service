from fastapi import FastAPI
from routes.product_route import router as product_router

class AppInitializer:
    def __init__(self):
        self.app = FastAPI()

    def register_routes(self):
        """
        Register routes with FastAPI app.
        """
        self.app.include_router(product_router)

    def get_app(self):
        """
        Return the FastAPI app instance after routes are registered.
        """
        return self.app
