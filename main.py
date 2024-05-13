from pytube import YouTube

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


url = get_video_url_from_user()
youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)

print("Titre:", youtube_video.title)

print("STREAMS")
all_streams = youtube_video.streams

streams = all_streams.filter(progressive=True, file_extension="mp4")

itag_index = get_video_stream_itag_from_user(streams)
stream = streams.get_by_itag(itag_index)
print(stream)
print("Téléchargement...")
stream.download()
print("OK")
