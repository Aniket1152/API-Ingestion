import logging
import os
from config import PATHS_CONFIG

def setup_logger():
    # Create logs directory if it doesn't exist
    log_dir = PATHS_CONFIG['logs_dir']
    os.makedirs(log_dir, exist_ok=True)
    
    # Get log file path
    log_file = PATHS_CONFIG['log_file']
    
    # Configure logger
    logger = logging.getLogger('country_pipeline')
    logger.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(file_handler)
    
    return logger