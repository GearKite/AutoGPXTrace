# AutoGPXTrace

Simple scripts to sort automatically collected GPS traces and upload them to OpenStreetMap.

## Usage

### Install

1. Clone the repository
1. Create a Python virtual environment  
1. Install required packages using `pip install -r requirements`

### Sorting

1. Create `./input` and `./output` directories  
1. Put your automatically collected GPS traces in the input directory  
1. Configure the requirements inside `filter.py` using your favourite code/text editor  
1. Run `python3 filter.py`

After it's finished GPX files matching the requirements should be in the output directory

### Uploading

1. Rename `env.example` to `.env`  
1. Inside `.env` set your OSM username and password
1. Change the trace description, tags and visibility
1. Run `python3 upload.py`

This will upload all the GPS traces inside `./output` to OpenStreetMap
