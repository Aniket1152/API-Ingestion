import json
import pandas as pd
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

def save_dataframe_to_csv(data, csv_filename="data/countries.csv"):
    """Save data as DataFrame to CSV file"""
    try:
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(csv_filename), exist_ok=True)
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Save to CSV
        df.to_csv(csv_filename, index=False)
        
        logger.info(f"Successfully saved DataFrame with {len(df)} records to {csv_filename}")
        return True
    except Exception as e:
        logger.error(f"Error saving DataFrame to CSV: {str(e)}")
        return False

def save_data_as_dataframe_and_json(data, base_filename="data/countries"):
    """Save data in both JSON and CSV formats"""
    try:
        # Save as JSON
        json_filename = f"{base_filename}.json"
        json_success = save_data_to_file(data, json_filename)
        
        # Save as CSV
        csv_filename = f"{base_filename}.csv"
        csv_success = save_dataframe_to_csv(data, csv_filename)
        
        return json_success and csv_success
    except Exception as e:
        logger.error(f"Error saving data in multiple formats: {str(e)}")
        return False