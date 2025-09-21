import sys
from src.api_client import fetch_all_countries_multithreaded
from src.data_processor import process_countries_data
from src.data_storage import save_data_as_dataframe_and_json
from logger_config import setup_logger

logger = setup_logger()

def main():
    try:
        logger.info("Starting country data pipeline")
        
        # Step 1: Fetch data with multithreading
        countries_data = fetch_all_countries_multithreaded()
        if not countries_data:
            logger.error("No data fetched, exiting pipeline")
            return False
        
        # Step 2: Process and validate data
        processed_data = process_countries_data(countries_data)
        
        if not processed_data:
            logger.error("No valid data after processing, exiting pipeline")
            return False
        
        # Step 3: Save data as both JSON and DataFrame (CSV)
        success = save_data_as_dataframe_and_json(processed_data)
        
        if success:
            logger.info("Pipeline completed successfully")
            print("Pipeline completed successfully!")
            print("Data saved as both JSON and CSV formats")
            return True
        else:
            logger.error("Pipeline failed during data saving")
            return False
            
    except Exception as e:
        logger.error(f"Pipeline failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)