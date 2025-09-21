import logging
import os
from datetime import datetime
from config import PATHS_CONFIG, PROJECT_ROOT

def setup_logger():
    # Create logs directory if it doesn't exist (using absolute path)
    log_dir = os.path.join(PROJECT_ROOT, PATHS_CONFIG['logs_dir']) if not os.path.isabs(PATHS_CONFIG['logs_dir']) else PATHS_CONFIG['logs_dir']
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate timestamped log filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_pattern = PATHS_CONFIG['log_file_pattern']
    
    # Handle both relative and absolute paths
    if '{}' in log_file_pattern:
        if os.path.isabs(log_file_pattern):
            log_file = log_file_pattern.format(timestamp)
        else:
            log_file = os.path.join(PROJECT_ROOT, log_file_pattern.format(timestamp))
    else:
        log_file = os.path.join(PROJECT_ROOT, log_file_pattern)
    
    # Configure logger
    logger = logging.getLogger('country_pipeline')
    logger.setLevel(logging.INFO)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(file_handler)
    
    # Also add console handler for immediate feedback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger