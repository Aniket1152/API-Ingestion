import json
import os
from config import RAW_DATA_FILE
from logger_config import setup_logger

logger = setup_logger()

def save_data_to_file(data, filename=RAW_DATA_FILE):
    """Save data to JSON file"""
    try:
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Successfully saved {len(data)} records to {filename}")
        return True
    except Exception as e:
        logger.error(f"Error saving data to file: {str(e)}")
        return False