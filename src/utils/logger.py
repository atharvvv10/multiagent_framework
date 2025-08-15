from datetime import datetime

class Logger:
    @staticmethod
    def log(msg):
        print(f"[{datetime.now()}] {msg}")
