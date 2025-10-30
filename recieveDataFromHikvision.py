from fastapi import FastAPI, Request, File, UploadFile, Form
import logging
import json
import xml.etree.ElementTree as ET
import os
from datetime import  datetime

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Directory to save uploaded files

UPLOAD_DIRECTORY = "D:\data"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/TestACS")
async def receive_dynamic_body(
        request: Request,
       ):
    # print(request.body())
    body = await request.body()
    form_data = await request.form()
    print(form_data)

    print(body)
    # logger.info(f"Received raw body: {body.decode('utf-8', errors='ignore')}")
    # Process the event log (assuming it's JSON in the 'event_log' field)
    event_log = form_data.get('event_log')

    # Parse the event_log JSON
    event_data = json.loads(event_log)

    # Extract the 'dateTime' from the event log
    event_time_str = event_data.get('dateTime')

    # Parse the datetime string into a datetime object
    event_time = datetime.fromisoformat(event_time_str)

    if event_log:

        # Check if 'Name' and 'Employee Number' are present
        name = event_data.get('AccessControllerEvent', {}).get('name')
        employee_number = event_data.get('AccessControllerEvent', {}).get('employeeNoString')
        if name is not None and employee_number is not None:
            # Save event_log to a file
            event_log_filename = f"event_log_{event_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            with open(os.path.join(UPLOAD_DIRECTORY, event_log_filename), "w") as log_file:
                log_file.write(event_log)

    # Process the Picture file
    picture: UploadFile = form_data.get('Picture')
    if picture:
        picture_filename = f"{picture.filename.split('.')[0]}_{event_time.strftime('%Y-%m-%d_%H-%M-%S')}.{picture.filename.split('.')[-1]}"
        picture_path = os.path.join(UPLOAD_DIRECTORY, picture_filename)
        with open(picture_path, "wb") as picture_file:
            picture_file.write(await picture.read())

    # Process the Thermal file
    thermal: UploadFile = form_data.get('Thermal')
    if thermal:
        thermal_filename = f"{thermal.filename.split('.')[0]}_{event_time.strftime('%Y-%m-%d_%H-%M-%S')}.{thermal.filename.split('.')[-1]}"
        thermal_path = os.path.join(UPLOAD_DIRECTORY, thermal_filename)
        with open(thermal_path, "wb") as thermal_file:
            thermal_file.write(await thermal.read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="xx.xx.x.xxx", port=8080)