import youtube_downloader

urls = ["https://www.youtube.com/watch?v=ujnqNTQRw6k", "https://www.youtube.com/watch?v=iMDQy2HwO8A&pp=ygULYmxheXplIGZheWE%3D", "https://www.youtube.com/watch?v=F9hwvIJNaMk&pp=ygULYmxheXplIGZheWE%3D"]

for url in urls:
    youtube_downloader.download_video(url)
