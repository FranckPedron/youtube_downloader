import youtube_downloader


def get_user_choice():
    urls = []
    while True:
        choice = input("Combien de vidéos souhaitez vous télécharger ? ")
        print("")
        if choice == "":
            print("Erreur! Vous devez choisir un nombre de vidéos")
        else:
            try:
                int_choice = int(choice)
            except ValueError:
                print("Erreur! Vous devez entrer un chiffre")
            else:
                if int_choice < 1:
                    print("Erreur! Choisissez un nombre supérieur ou égal à 1")
                else:
                    break
    for i in range(int_choice):
        url = youtube_downloader.get_video_url_from_user()
        urls.append(url)

    return urls


urls = get_user_choice()

for url in urls:
    youtube_downloader.download_video(url)
    print("")
