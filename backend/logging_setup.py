import  logging


def setup_logger(name,logfilename,level = logging.DEBUG):
    # create a custom logger
    logger = logging.getLogger(name)

    # configure custom logger
    logger.setLevel(level)
    file_handler = logging.FileHandler(logfilename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



