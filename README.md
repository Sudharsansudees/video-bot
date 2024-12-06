video-bot/
├── main.py                # Main script to execute the bot
├── video_downloader.py    # Video downloading logic
├── video_uploader.py      # Upload and API integration logic
├── file_monitor.py        # Directory monitoring logic
├── utils.py               # Utility functions (hashing, etc.)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation


⚙️ API Integration Details
1. Get Upload URL
Endpoint: https://api.socialverseapp.com/posts/generate-upload-url
Method: POST
Headers:
json
Copy code
{
    "Flic-Token": "<YOUR_TOKEN>",
    "Content-Type": "application/json"
}
Response:
json
Copy code
{
    "url": "pre-signed-upload-url",
    "hash": "file-hash"
}


2. Upload Video
URL: Pre-signed upload URL from Step 1.
Method: PUT
Data: Binary file data.


3. Create Post
Endpoint: https://api.socialverseapp.com/posts
Method: POST
Headers:
json
Copy code
{
    "Flic-Token": "<YOUR_TOKEN>",
    "Content-Type": "application/json"
}
Body:
json
Copy code
{
    "title": "<video title>",
    "hash": "<hash from Step 1>",
    "is_available_in_public_feed": false,
    "category_id": <category_id>
}


🌟 Key Functions
Video Downloader
Path: video_downloader.py
Handles downloading videos from Instagram, TikTok, and Reddit.
Video Uploader
Path: video_uploader.py
Manages:
Fetching pre-signed upload URLs.
Uploading videos to the server.
Creating posts via API.
File Monitor
Path: file_monitor.py
Uses watchdog to monitor the /videos directory for new .mp4 files and triggers uploads.


💡 Example Workflow
The bot monitors the /videos directory.
When a new .mp4 file is added:
Fetches a pre-signed upload URL.
Uploads the file to the server.
Creates a post entry using the file hash.
Deletes the file locally after a successful upload.

