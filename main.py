import asyncio
from video_downloader import download_video
from video_uploader import get_upload_url, upload_video, create_post
from file_monitor import VideoEventHandler
from watchdog.observers import Observer
import time

TOKEN = "<YOUR_TOKEN>"

async def process_video(file_path):
    # Get upload URL
    upload_url_data = await get_upload_url(TOKEN)
    pre_signed_url = upload_url_data["url"]
    video_hash = upload_url_data["hash"]

    # Upload video
    status = await upload_video(pre_signed_url, file_path)
    if status == 200:
        # Create post
        title = "Uploaded Video"
        category_id = 1  # Example category
        await create_post(TOKEN, title, video_hash, category_id)

        # Delete file after upload
        os.remove(file_path)

def start_monitoring():
    event_handler = VideoEventHandler(process_video)
    observer = Observer()
    observer.schedule(event_handler, path='./videos', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitoring()
