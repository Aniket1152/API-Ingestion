import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import API_BASE_URL, API_ALL_ENDPOINT, MAX_WORKERS, REQUEST_TIMEOUT
from logger_config import setup_logger

logger = setup_logger()

def fetch_country_detail(country_name):
    """Fetch detailed data for a single country"""
    try:
        # Using name endpoint to get full details
        url = f"{API_BASE_URL}/name/{country_name}"
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully fetched data for {country_name}")
            return data[0]  # API returns array, we take first result
        else:
            logger.error(f"Failed to fetch {country_name}: {response.status_code}")
            return None
    except requests.Timeout:
        logger.error(f"Timeout fetching {country_name}")
        return None
    except Exception as e:
        logger.error(f"Error fetching {country_name}: {str(e)}")
        return None

def fetch_all_countries_multithreaded(max_workers=MAX_WORKERS):
    """Fetch all countries data using multithreading"""
    logger.info(f"Starting to fetch all countries data with multithreading (max_workers={max_workers})")
    
    # First get the list of all country names
    try:
        response = requests.get(f"{API_BASE_URL}{API_ALL_ENDPOINT}?fields=name", timeout=REQUEST_TIMEOUT)
        if response.status_code != 200:
            logger.error("Failed to get countries list")
            return []
    except Exception as e:
        logger.error(f"Error getting countries list: {str(e)}")
        return []
    
    countries_list = response.json()
    country_names = [country['name']['common'] for country in countries_list]
    
    logger.info(f"Found {len(country_names)} countries to fetch")
    
    # Use ThreadPoolExecutor for multithreading
    all_countries_data = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_country = {
            executor.submit(fetch_country_detail, name): name 
            for name in country_names
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_country):
            country_name = future_to_country[future]
            try:
                country_data = future.result()
                if country_data:
                    all_countries_data.append(country_data)
            except Exception as e:
                logger.error(f"Error processing {country_name}: {str(e)}")
    
    logger.info(f"Successfully fetched data for {len(all_countries_data)} countries")
    return all_countries_data