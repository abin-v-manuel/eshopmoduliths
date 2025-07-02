 
from fastapi import FastAPI
from app.bootstrapper.startup import setup

app = FastAPI(debug=True)
setup(app)