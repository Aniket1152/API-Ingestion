import os
import sys
from src.api_client import fetch_all_countries_multithreaded
from src.data_processor import process_countries_data
from src.data_storage import save_data_to_file
from logger_config import setup_logger

print("=== DEBUG: Starting Pipeline ===")

# Setup
logger = setup_logger()
logger.info("=== DEBUG: Pipeline starting ===")

def main():
    try:
        print("Step 1: Fetching countries data...")
        logger.info("Step 1: Fetching countries data...")
        
        # Fetch data
        countries_data = fetch_all_countries_multithreaded(max_workers=5)
        print(f"Step 1 Result: Got {len(countries_data)} countries")
        logger.info(f"Step 1 Result: Got {len(countries_data)} countries")
        
        if not countries_data:
            print("ERROR: No countries data fetched!")
            logger.error("ERROR: No countries data fetched!")
            return False
        
        print("Step 2: Processing data...")
        logger.info("Step 2: Processing data...")
        
        # Process data
        processed_data = process_countries_data(countries_data)
        print(f"Step 2 Result: Processed {len(processed_data)} countries")
        logger.info(f"Step 2 Result: Processed {len(processed_data)} countries")
        
        if not processed_data:
            print("ERROR: No processed data!")
            logger.error("ERROR: No processed data!")
            return False
        
        print("Step 3: Saving data...")
        logger.info("Step 3: Saving data...")
        
        # Save data
        print(f"Saving to: data/countries.json")
        success = save_data_to_file(processed_data, "data/countries.json")
        print(f"Step 3 Result: Save success = {success}")
        logger.info(f"Step 3 Result: Save success = {success}")
        
        if success:
            print("SUCCESS: Pipeline completed!")
            logger.info("SUCCESS: Pipeline completed!")
            return True
        else:
            print("ERROR: Failed to save data!")
            logger.error("ERROR: Failed to save data!")
            return False
            
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        logger.error(f"CRITICAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running debug main...")
    success = main()
    print(f"Final result: {success}")
    sys.exit(0 if success else 1)