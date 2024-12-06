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




Explanation of the Video Search and Upload Bot :


The **Video Search and Upload Bot** is a Python project designed to automate the process of finding, downloading, and uploading videos from social media platforms. Here's a clear breakdown of what the bot does and how it works:

---

### **Objective**

The goal of the bot is to:
1. **Search for videos** on platforms like Instagram, TikTok, and Reddit.
2. **Download the videos** to a local directory (`/videos`).
3. **Upload the videos** to a remote server using a set of API endpoints.
4. Automate the workflow for efficiency, including tasks like:
   - Monitoring the `/videos` directory for new files.
   - Automatically cleaning up local files after uploading them.

---

### **Core Features**

1. **Search and Download Videos**:
   - The bot uses APIs or scraping tools to search and download `.mp4` videos from specified platforms.
   - Supported platforms:
     - **Instagram**: Using tools like `instaloader`.
     - **TikTok**: Using libraries like `tiktokpy`.
     - **Reddit**: Using the `praw` library to fetch video links from subreddits.

2. **Upload Videos to a Server**:
   - The bot integrates with a server via APIs to upload videos.
   - The process involves:
     - Requesting a **pre-signed upload URL** from the server.
     - Uploading the video to the server using this URL.
     - Creating a post entry on the server with video details.

3. **Directory Monitoring**:
   - The bot monitors the `/videos` directory for any newly added `.mp4` files.
   - When a new video is detected, the bot automatically starts the upload process.

4. **Asynchronous Operations**:
   - To handle multiple tasks concurrently (e.g., downloading and uploading videos), the bot uses Python’s `asyncio`.

5. **Auto-Delete Local Files**:
   - After a video is successfully uploaded, it is deleted from the local system to save storage.

6. **Progress Tracking**:
   - The bot provides progress bars (using `tqdm`) for downloading and uploading tasks.

---

### **How the Bot Works**

#### **Workflow Overview**

1. **Searching and Downloading Videos**:
   - The bot takes user-specified criteria (e.g., hashtags, subreddit names) to find videos.
   - Videos are downloaded and saved to the `/videos` directory.

2. **Monitoring for New Files**:
   - A directory monitor continuously watches the `/videos` folder for new `.mp4` files using the `watchdog` library.

3. **Uploading Videos to the Server**:
   - For each new video:
     1. The bot requests a pre-signed URL from the API to securely upload the file.
     2. It uploads the video to the server using this pre-signed URL (via an HTTP PUT request).
     3. Once uploaded, it sends metadata (e.g., title, file hash) to the server to create a post entry.

4. **Cleaning Up**:
   - After successful uploads, the bot deletes the video file locally.

---

### **API Workflow**

The bot interacts with the server using three main API endpoints:

1. **Get Upload URL**:
   - This API generates a pre-signed URL for uploading a specific video.
   - Example response:
     ```json
     {
         "url": "https://upload-url.com/signed",
         "hash": "video-file-hash"
     }
     ```

2. **Upload Video**:
   - The bot uploads the video using the pre-signed URL via a PUT request.

3. **Create Post**:
   - After uploading, the bot sends a POST request to create a post entry on the server, including:
     - The video title.
     - The hash received from the first API.
     - A category ID for categorization.

---

### **Technical Components**

1. **Python Libraries Used**:
   - **`asyncio`**: For asynchronous tasks like concurrent downloads/uploads.
   - **`aiohttp`**: For making asynchronous HTTP requests to the API.
   - **`watchdog`**: For monitoring the `/videos` directory for new files.
   - **`tqdm`**: For displaying progress bars for downloads/uploads.
   - **Platform-specific tools** for downloading:
     - `instaloader` for Instagram.
     - `praw` for Reddit.
     - `tiktokpy` for TikTok.

2. **Project Structure**:
   - The project is modular, with separate files for downloading, uploading, and monitoring tasks.
   - Main script (`main.py`) ties everything together.

---

### **Expected Output**

When the bot runs:
1. It actively watches the `/videos` directory.
2. New `.mp4` files added to the directory are automatically uploaded to the server.
3. Progress bars display the status of each upload.
4. Files are deleted locally after successful uploads.

---

### **Usage Example**

1. The user specifies hashtags or subreddits to search for videos.
2. The bot fetches and downloads the videos into `/videos`.
3. The bot detects the new files and uploads them to the server.
4. Metadata for each video is sent to the server, and the local file is deleted.

---

This bot automates video handling tasks, saving time and reducing manual effort for users managing video content. Let me know if further clarification is needed!
