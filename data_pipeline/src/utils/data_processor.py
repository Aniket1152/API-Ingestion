from logger_config import setup_logger
from config import VALIDATION_CONFIG

logger = setup_logger()

def validate_country_data(country_data):
    """Comprehensive validation for country data"""
    # Check required fields
    required_fields = VALIDATION_CONFIG['required_fields']
    
    for field in required_fields:
        if field not in country_data:
            country_name = country_data.get('name', {}).get('common', 'Unknown') if isinstance(country_data.get('name'), dict) else 'Unknown'
            logger.warning(f"Missing field {field} in country {country_name}")
            return False
    
    # Validate population
    population_min = VALIDATION_CONFIG['population_min']
    if not isinstance(country_data['population'], (int, float)) or country_data['population'] < population_min:
        country_name = country_data.get('name', {}).get('common', 'Unknown') if isinstance(country_data.get('name'), dict) else 'Unknown'
        logger.warning(f"Invalid population data for {country_name}")
        return False
    
    # Validate name structure
    if not isinstance(country_data['name'], dict):
        logger.warning(f"Invalid name structure for country")
        return False
    
    return True

def process_countries_data(countries_data):
    """Process and validate all countries data"""
    logger.info("Starting data processing and validation")
    
    valid_countries = []
    invalid_count = 0
    
    for country in countries_data:
        if validate_country_data(country):
            # Clean/normalize data
            cleaned_country = {
                'name': country['name'].get('common', 'Unknown'),
                'official_name': country['name'].get('official', ''),
                'population': country.get('population', 0),
                'region': country.get('region', 'Unknown'),
                'capital': country.get('capital', ['Unknown'])[0] if country.get('capital') else 'Unknown'
            }
            valid_countries.append(cleaned_country)
        else:
            invalid_count += 1
    
    logger.info(f"Processed {len(valid_countries)} valid countries, {invalid_count} invalid")
    return valid_countries