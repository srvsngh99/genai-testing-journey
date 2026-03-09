"""Logging configuration mapped to week 6 practice."""
import logging

def setup_logger(name):
    """Sets up a basic logger that outputs to console and a file."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Check if handlers already exist to avoid duplicate logs when imported multiple times
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        
        file_handler = logging.FileHandler("api_caller.log")
        file_handler.setFormatter(formatter)
        
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        
    return logger
