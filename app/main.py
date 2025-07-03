from fastapi import FastAPI
from app.modules.catalog.presentation import routes as catalog_routes
from app.modules.basket.presentation import routes as basket_routes
app = FastAPI()

app.include_router(catalog_routes.router)
app.include_router(basket_routes.router)