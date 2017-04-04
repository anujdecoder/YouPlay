import urllib.request
import urllib.error as Errors
from pytube import YouTube
from pytube import exceptions as pyError


class playlist:

    def __init__(self):
        self.url = None
        self.num = 0
        self.list = []
        self.source_code =""


    #Asks the URL and checks the internet
    def get_url(self):
        print("Enter the URL of playlist")
        self.url = input()
        flag = 0
        # Check the internet and hang the script until the connection activates
        while True:
            try:
                response = urllib.request.urlopen(self.url, )
                self.source_code = str(response.read())
                if (flag):
                    print("Connected to the remote server")
                return True
            except Errors.URLError:
                if (flag == 0):
                    print("Could not connect to the remote server. Check your internet connection")
                    flag = 1
                continue


    #Check whether the URL is playlist or not
    def isPlaylist(self):
        while True:
            try:
                self.source_code.index('<meta property="og:site_name" content="YouTube">')
                break
            except ValueError:
                print("Invalid URL")
                self.get_url()
        while True:
            try:
                self.source_code.index("pl-header-details")
                break
            except ValueError:
                print("Invalid URL")
                self.get_url()

    def count_videos(self):
        temp_index = self.source_code.index("pl-header-details")
        part_of_code = self.source_code[temp_index:]

        temp_index = 0
        temp_index = part_of_code.index("</li><li>")
        part_of_code = part_of_code[temp_index:]

        temp_index = 0
        temp_index = part_of_code.index("videos") - 1

        part_of_code = part_of_code[0:temp_index]
        part_of_code = part_of_code[9:]
        number_of_videos = int(part_of_code)
        self.num = number_of_videos



    def total_videos(self):
        print("The total number of videos in the playlist are ",self.num)



    def get_video_links(self):
        str = self.source_code

        for i in range(self.num):
            a = str.index("pl-video-title-link yt-uix-tile-link yt-uix-sessionlink")
            str = str[a:]
            a = 0
            b = str.index("pl-video-bottom-standalone-badge")
            link = str[a:b]

            x = link.index('href')
            y = link.index("data-sessionlink") - 2
            x = x + 6
            link = link[x:y]

            str = str[b:]

            link = "https://www.youtube.com" + link
            self.list.append(link)



    def display_links(self):
        for i in self.list:
            print(i)


    def download(self, list):
        for i in list:
            # creating a youtube object
            try:
                yt = YouTube(self.list[i])
                print(yt.filename)
            except pyError.AgeRestricted:
                response = urllib.request.urlopen(list[i])
                code = str(response.read())
                index = code.index('<meta property="og:title" content="')
                index += len('<meta property="og:title" content="')
                code = code[index:]
                index = code.index(">")
                code = code[:index]
                name = code
                print(name + " contains age restricted content. Hence unable to download.")
            except Errors.URLError:
                flag = 0
                while True:
                    try:
                        response = urllib.request.urlopen(self.url)
                        if (flag == 1):
                            print("Connected to the remote server")
                        break
                    except Errors.URLError:
                        if (flag == 0):
                            print("Could not connect to the remote server. Check your internet connection")
                            flag = 1
                        continue

