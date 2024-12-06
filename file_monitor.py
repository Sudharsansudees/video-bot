from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VideoEventHandler(FileSystemEventHandler):
    def __init__(self, upload_function):
        self.upload_function = upload_function

    def on_created(self, event):
        if event.src_path.endswith(".mp4"):
            asyncio.run(self.upload_function(event.src_path))
