import uvicorn
from fastapi import FastAPI

from text_finder.init_routers import init_routers


app = FastAPI()

init_routers(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
