from pytube import YouTube

BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='

while True:
    url = input("Entrez l'url de la vidéo à télécharger: ")
    # if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
    if url.lower().startswith(BASE_YOUTUBE_URL):
        break
    print("ERREUR: vous devez entrer une url de vidéo YouTube !")


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")


youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)

print("Titre:", youtube_video.title)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(" ", stream)

stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement...")
stream.download()
print("OK")
