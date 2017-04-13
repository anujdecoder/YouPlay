from functions import *


def download_playlist():
    playlist = PlayList()
    playlist.get_url()
    playlist.check_internet()
    playlist.isPlaylist()
    playlist.get_name()
    playlist.count_videos()
    playlist.total_videos()
    playlist.get_video_links()
    playlist.get_path()
    playlist.get_quality()
    playlist.save()


def download_video():
    youtube_video = video()
    youtube_video.get_url()
    youtube_video.get_details()
    youtube_video.save()
    winsound.MessageBeep()


def resume_download():
    fp = open("url.txt", "r")
    url = fp.read()
    fp.close()
    fp = open("qua.txt", "r")
    quality = fp.read()
    fp.close()
    fp = open("path.txt", "r")
    path = fp.read()
    fp.close()

    continue_download = PlayList()
    continue_download.set_members(url, quality, path)
    continue_download.check_internet()
    continue_download.get_name()
    continue_download.count_videos()
    continue_download.get_video_links()
    continue_download.save()

def main():
    while True:
        try:
            choice = input()
            choice = choice.lower()
            if choice != "video" and choice != "playlist" and choice != "resume":
                print("Error : Invalid Input")
                continue
            break
        except KeyboardInterrupt:
            continue

    if choice == "video":
        download_video()
    elif choice == "playlist":
        download_playlist()
    elif choice == "resume":
        resume_download()


main()
