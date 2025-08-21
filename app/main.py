from manager import Management
from fastapi import FastAPI
import os
import logging
import uvicorn


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
management = Management()


@app.get("/api/get-analysis")
async def read_all():
    processing = management.start()
    return processing

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT","8080")))  
