from fastapi import APIRouter

route_test = APIRouter(prefix="/routetest", tags=["Route Test"])

@route_test.get("/test")
def test():
    return "Test succes"

@route_test.get("/")
def welcome():
    return "Welcome !"