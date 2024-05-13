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


def get_video_stream_itag_from_user(streams):
    print("Résolutions disponibles: ")
    index = 1
    for stream in streams:
        print(index, "-", stream.resolution, "-", stream.itag)
        index += 1

    while True:
        num_res = input("Quelle résolution choisissez-vous ? ")
        if num_res == "":
            print("Erreur! Vous devez choisir une résolution.")
        else:
            try:
                int_num_res = int(num_res)
            except ValueError:
                print("Erreur! Vous devez entrer un chiffre")
            else:
                if not 1 <= int_num_res <= len(streams):
                    print("Erreur! Vous devez entrer un nombre entre 1 et ", len(streams))
                else:
                    break

    itag = streams[int_num_res - 1].itag
    return itag


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")


# url = "https://www.youtube.com/watch?v=yWR5Oq9_1Ck"
url = get_video_url_from_user()
youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)

print("Titre:", youtube_video.title)

streams = youtube_video.streams.filter(progressive=False, file_extension="mp4", type="video").order_by("resolution").desc()
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
ffmpeg.output(ffmpeg.input(video_filename), ffmpeg.input(audio_filename), output_filename, vcodec="copy", acodec="copy").run()
print("OK")
