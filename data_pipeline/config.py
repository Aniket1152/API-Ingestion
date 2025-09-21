import yaml
import os
from datetime import datetime

# Get the directory where this config file is located (project root)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

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
    """Return default configuration with proper paths"""
    return {
        'api': {
            'base_url': 'https://restcountries.com/v3.1',
            'all_endpoint': '/all',
            'fields': '?fields=name,capital,population,region,subregion'
        },
        'paths': {
            'data_dir': os.path.join(PROJECT_ROOT, 'data'),
            'logs_dir': os.path.join(PROJECT_ROOT, 'logs'),
            'raw_data_file': os.path.join(PROJECT_ROOT, 'data', 'countries.json'),
            'csv_file': os.path.join(PROJECT_ROOT, 'data', 'countries.csv'),
            'log_file_pattern': os.path.join(PROJECT_ROOT, 'logs', 'pipeline_{}.log')
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