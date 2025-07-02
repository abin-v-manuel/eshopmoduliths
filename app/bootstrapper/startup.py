 
def setup(app):
    from app.modules.catalog.presentation.routes import router as catalog_router
    from app.modules.basket.presentation.routes import router as basket_router
    from app.modules.ordering.presentation.routes import router as ordering_router
    from app.modules.identity.presentation.routes import router as identity_router

    app.include_router(catalog_router, prefix="/catalog")
    app.include_router(basket_router, prefix="/basket")
    app.include_router(ordering_router, prefix="/orders")
    app.include_router(identity_router, prefix="/auth")

    # TODO: Initialize DB, Redis, RabbitMQ, middleware etc.