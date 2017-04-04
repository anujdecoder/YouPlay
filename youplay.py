from functions import *

def main():
    temp = playlist()
    temp.get_url()
    temp.isPlaylist()
    temp.count_videos()
    temp.get_video_links()
    num=list(range(temp.num))
    temp.download(num)

main()

