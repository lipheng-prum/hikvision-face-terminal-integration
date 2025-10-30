from fastapi import FastAPI, Request
import logging
import os

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Directory to save uploaded files
UPLOAD_DIR = "D:/data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/")
async def receive_dynamic_body(request: Request):
    # Read the raw body
    body = await request.body()
    body_decoded = body.decode('utf-8', errors='ignore')

    # Log the received body
    logger.info(f"Received raw body: {body_decoded}")

    # Save the body to a file
    file_path = os.path.join(UPLOAD_DIR, "received_data.txt")
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(body_decoded)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="xx.xx.x.xx", port=8088)
