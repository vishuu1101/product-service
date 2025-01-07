from app import AppInitializer


def create_app():
    """
    Create FastAPI app using AppInitializer.
    """
    app_initializer = AppInitializer()
    app_initializer.register_routes()
    return app_initializer.get_app()

# Create the app instance
app = create_app()
