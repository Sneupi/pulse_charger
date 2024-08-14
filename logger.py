import datetime
from threading import Lock

class Logger:
    """Encapsulates logging lines to a file with a timestamp."""
    def __init__(self, filepath: str, mode='a'):
        self.file = open(filepath, mode)
        self.lock = Lock()  # multithreading access lock
        
    def log(self, *args):
        """Logs to file each string form of *args 
        delimited by commas following a timestamp"""
        with self.lock:
            elements = ','.join([str(e) for e in args])
            self.file.write(f'{datetime.datetime.now()},{elements}\n')
    
    def close(self):
        self.file.close()
        
    def __del__(self):
        self.close()