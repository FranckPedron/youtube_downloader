from pytube import YouTube

url = "https://www.youtube.com/watch?v=8VfsciIdJrs"

youtube_video = YouTube(url)
print("Titre:", youtube_video.title)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(" ", stream)

stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement...")
stream.download()
print("OK")
