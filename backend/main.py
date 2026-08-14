from fast_API import set_router
from fastapi import FastAPI
from uvicorn import run

app = FastAPI()
set_router(app)

def main():
    run("main:app", port=5000, log_level="info", reload=True)


if __name__ == "__main__":
    main()