from manager import Management
from fastapi import FastAPI, BackgroundTasks
import os
import logging
import uvicorn


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
management = Management()
processing = None

def start_background_process():
    """Start analysis in background processing."""
    global processing
    processing = management.start()

@app.get("/api/processing")
async def start_processing(background_tasks: BackgroundTasks):
    """Start analysis in background processing."""
    background_tasks.add_task(start_background_process)
    return {"status": "started"}

@app.get("/api/get-analysis")
async def read_all():
    """Get the analysis results."""
    if not processing: return {"error": "Processing not started yet. Please start processing first."}
    return processing

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT","8080")))  
