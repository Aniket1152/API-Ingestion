import os

# API Configuration
API_BASE_URL = "https://restcountries.com/v3.1"
API_ALL_ENDPOINT = "/all"

# File paths - use absolute paths relative to project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_FILE = os.path.join(PROJECT_ROOT, "data", "countries.json")
LOG_FILE = os.path.join(PROJECT_ROOT, "logs", "pipeline.log")

# Threading configuration
MAX_WORKERS = 20
REQUEST_TIMEOUT = 30  # seconds