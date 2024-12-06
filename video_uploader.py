import aiohttp
import hashlib
import os

async def get_upload_url(token):
    url = "https://api.socialverseapp.com/posts/generate-upload-url"
    headers = {"Flic-Token": token, "Content-Type": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={}, headers=headers) as response:
            return await response.json()

async def upload_video(pre_signed_url, video_path):
    async with aiohttp.ClientSession() as session:
        async with session.put(pre_signed_url, data=open(video_path, 'rb')) as response:
            return response.status

async def create_post(token, title, hash_value, category_id):
    url = "https://api.socialverseapp.com/posts"
    headers = {"Flic-Token": token, "Content-Type": "application/json"}
    payload = {
        "title": title,
        "hash": hash_value,
        "is_available_in_public_feed": False,
        "category_id": category_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            return await response.json()
