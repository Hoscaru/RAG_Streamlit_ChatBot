import logging

def setup_logger(name = "RagBot"):
    """
    Setup a logger for the application.
    Args:
        name (str): Name of the logger.
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    #Formatter
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)
    return logger

logger = setup_logger()