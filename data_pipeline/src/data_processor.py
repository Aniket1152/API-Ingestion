from logger_config import setup_logger

logger = setup_logger()

def validate_country_data(country_data):
    """Comprehensive validation for country data"""
    # Check required fields
    required_fields = ['name', 'population']
    
    for field in required_fields:
        if field not in country_data:
            logger.warning(f"Missing field {field} in country data: {country_data.get('name', 'Unknown')}")
            return False
    
    # Validate population
    if not isinstance(country_data['population'], (int, float)) or country_data['population'] < 0:
        logger.warning(f"Invalid population data for {country_data['name']}")
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
    
    # Fixed: was "for country in countries_:" 
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