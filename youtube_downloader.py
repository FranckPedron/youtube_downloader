import os
from pytube import YouTube
import ffmpeg

BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='


def get_video_url_from_user():
    while True:
        url = input("Entrez l'url de la vidéo à télécharger: ")
        # if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
        if url.lower().startswith(BASE_YOUTUBE_URL):
            return url
        print("ERREUR: vous devez entrer une url de vidéo YouTube !")


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")


def download_video(url):
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(on_download_progress)

    print("")
    print("Titre:", youtube_video.title)
    print("")

    streams = youtube_video.streams.filter(progressive=False, file_extension="mp4", type="video").order_by(
        "resolution").desc()
    video_streaam = streams[0]

    streams = youtube_video.streams.filter(progressive=False, file_extension="mp4", type="audio").order_by("abr").desc()
    audio_streaam = streams[0]

    print("Téléchargement vidéo...")
    video_streaam.download("video")
    print("OK")

    print("Téléchargement audio...")
    audio_streaam.download("audio")
    print("OK")

    audio_filename = os.path.join("audio", audio_streaam.default_filename)
    video_filename = os.path.join("video", video_streaam.default_filename)
    output_filename = video_streaam.default_filename

    print("Combinaison des fichiers...")
    ffmpeg.output(ffmpeg.input(video_filename), ffmpeg.input(audio_filename), output_filename, vcodec="copy",
                  acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("OK")

    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
