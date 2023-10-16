import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Define the API endpoint URL
url = "https://api.openstreetmap.org/api/0.6/gpx/create"  # Replace with the actual API URL

# Define the parameters required in a multipart/form-data HTTP message
params = {
    "description": os.getenv("TRACE_DESCRIPTION"),
    "tags": os.getenv("TRACE_TAGS"),
    "visibility": os.getenv("TRACE_VISIBILITY"),  # Choose the appropriate visibility
}

for filename in os.listdir("output"):
    print(f"Uploading {filename}")

    # Define the files to upload in a dictionary
    files = {
        "file": (f"{filename}", open(f"output/{filename}", "rb"))  # Replace with the actual file path
    }

    # Send the POST request with authentication
    response = requests.post(url, data=params, files=files, auth=(os.getenv("OSM_USERNAME"), os.getenv("OSM_PASSWORD")))  # Replace with your authentication credentials

    # Check the response status code
    if response.status_code == 200:
        gpx_id = int(response.text)  # Extract the ID from the response
        print(f"GPX ID: {gpx_id}")
        os.remove(f"output/{filename}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        exit()
    time.sleep(1)
