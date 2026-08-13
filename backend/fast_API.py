from fastapi import FastAPI
from routes.route_test import route_test


def set_router(app: FastAPI):
    app.include_router(route_test)

