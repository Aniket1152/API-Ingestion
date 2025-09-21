import yaml
import os

def load_config(config_file="config.yaml"):
    """Load configuration from YAML file"""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return get_default_config()
    except Exception as e:
        print(f"Error loading config: {e}")
        return get_default_config()

def get_default_config():
    """Return default configuration"""
    return {
        'api': {
            'base_url': 'https://restcountries.com/v3.1',
            'all_endpoint': '/all',
            'fields': '?fields=name,capital,population,region,subregion'
        },
        'paths': {
            'data_dir': 'data',
            'logs_dir': 'logs',
            'raw_data_file': 'data/countries.json',
            'csv_file': 'data/countries.csv',
            'log_file': 'logs/pipeline.log'
        },
        'threading': {
            'max_workers': 20,
            'request_timeout': 30
        },
        'validation': {
            'required_fields': ['name', 'population'],
            'population_min': 0
        }
    }

# Load configuration
CONFIG = load_config()

# Export individual settings for easy access
API_CONFIG = CONFIG['api']
PATHS_CONFIG = CONFIG['paths']
THREADING_CONFIG = CONFIG['threading']
VALIDATION_CONFIG = CONFIG['validation']