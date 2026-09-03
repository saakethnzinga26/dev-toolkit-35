import logging
from logging.handlers import RotatingFileHandler
import sys
import os

class DevLogger:
    def __init__(self, name='dev-toolkit-35', path='logs/app.log', max_bytes=1048576, backups=5):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)s | %(message)s')
        
        file_handler = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backups)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

def setup_logger(name='dev-toolkit-35'):
    return DevLogger(name=name).get_logger()

if __name__ == '__main__':
    log = setup_logger()
    log.info('toolkit initialized successfully')