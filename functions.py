import urllib.request
import urllib.error as Errors
from pytube import YouTube
from pytube import exceptions as pyError
import os
import time
import winsound


class video:
    # Constructor- initializes the data members
    def __init__(self):
        self.url = None  # data member to store the url of video
        self.location = None  # data member to store the location of video where it is to be stored
        self.extension = None  # data member to store the file format of video
        self.resolution = None  # data member to store the resolution of video
        self.yt = None  # data member to download the video

    # Function to set the data members
    def set(self, location, extension, resolution):
        self.location = location
        self.extension = extension
        self.resolution = resolution

    # Asks the URL of the video
    def get_url(self):
        print("Enter the URL of video")
        # This block of code checks the syntax of the input
        while True:
            url = input()
            try:
                url.index("https://")
                break
            except ValueError:
                print("Invalid Input. Enter the URL again")
                continue

        while True:
            # Exception handling to handle different types of error
            try:
                self.yt = YouTube(url)
                break
            except ValueError:
                print("Invalid URL. Enter a Valid URL")
                url = input()
            except AttributeError:
                print("Invalid URL. Enter a Valid URL")
                url = input()
            except Errors.URLError:
                print("Could not connect to the remote sever.Check Your internet connection")
                time.sleep(5)
            except pyError.AgeRestricted:
                while True:
                    try:
                        response = urllib.request.urlopen(self.url)
                        break
                    except Errors.URLError:
                        print("Could not connect to the remote sever.Check Your internet connection")
                        time.sleep(5)
                code = str(response.read())
                index = code.index('<meta property="og:title" content="')
                index += len('<meta property="og:title" content="')
                code = code[index:]
                index = code.index(">")
                code = code[:index]
                name = code
                print(name + " contains age restricted content. Hence unable to download.")
                break
            except pyError.PytubeError:
                time.sleep(5)
                continue
        self.url = url

    # Gets the resolutions, file formats of the video and location where the video is to be saved
    def get_details(self):
        print("The video is available in following formats:")
        # Arranging the available resolutions in a list
        available_resolution = []
        for i in self.yt.get_videos():
            print(i.resolution)
            available_resolution.append(i.resolution)
        print("Enter the resolution :")
        # Exception Handling for wrong input type
        while True:
            try:
                temp = input()
                available_resolution.index(temp)
                break
            except ValueError:
                print("Invalid resolution. Enter again.")
                continue
        self.resolution = temp  # Resolution Data member modified

        # Checking the available file formats according to the user's choice
        available_extension = self.yt.filter(resolution=self.resolution)
        available_extension.sort()
        for i in available_extension:
            self.extension = i.extension
            break

        # Asks for the file location
        print("Enter the file location to be saved")
        while True:
            try:
                path = input()
                break
            except FileNotFoundError:
                print("Invalid Path")
                continue

        # Creates the location if it does not exist
        if not os.path.exists(path):
            os.mkdir(path)
        self.location = path

    # Following functions helps to manipulate video data members for the playlist
    # A function to create the video object of the video of the playlist
    def set_playlist_video_url(self, url):
        while True:
            try:
                self.yt = YouTube(url)
                break
            # Exception handling to notify user about the disconnected internet connection
            except Errors.URLError:
                print("Could not connect to the remote sever.Check Your internet connection")
                time.sleep(5)
            # Exception handling to notify user about the restricted content
            except pyError.AgeRestricted:
                while True:
                    try:
                        response = urllib.request.urlopen(self.url)
                        break
                    except Errors.URLError:
                        print("Could not connect to the remote sever.Check Your internet connection")
                        time.sleep(5)
                code = str(response.read())
                index = code.index('<meta property="og:title" content="')
                index += len('<meta property="og:title" content="')
                code = code[index:]
                index = code.index(">")
                code = code[:index]
                name = code
                print(name + " contains age restricted content. Hence unable to download.")
                break
            except pyError.PytubeError:
                time.sleep(5)
                continue
        self.url = url

    # Sets the resolution and the file formats for the videos of the playlist
    def set_from_quality(self, quality, path):
        self.location = path
        available_videos = self.yt.get_videos()
        if quality == "high":
            for i in available_videos:
                if i.profile == "High":
                    break
            self.extension = i.extension
            self.resolution = i.resolution
        elif quality == "medium":
            for i in available_videos:
                if i.profile == "Baseline":
                    break
            self.extension = i.extension
            self.resolution = i.resolution
        elif quality == "low":
            for i in available_videos:
                if i.profile == "Simple":
                    break
            self.extension = i.extension
            self.resolution = i.resolution

    # Begins the download
    def save(self):
        flag = True
        filename = self.yt.filename
        fp = open("start.txt", "w+")
        fp.write(filename)
        fp.close()
        temp_video = self.yt.get(self.extension, self.resolution)
        try:
            temp_video.download(self.location)
        except OSError:
            print(filename+" already exists. Skipping download.")
            flag = False

        if flag:
            print("Completed - " + filename)


# CLASS PLAYLIST
class PlayList:
    # Constructor - initializes the data members
    def __init__(self):
        self.url = None  # To store the url of the playlist
        self.num = 0  # To store the total number of videos in the playlist
        self.list = []  # To store the individual url of the videos
        self.source_code = ""  # To store the http response
        self.quality = None  # To store the video quality of the playlist
        self.location = None  # To store the file location
        self.name = None  # To store the name of the playlist


    # This function sets the members
    def set_members(self,url,quality,path):
        self.url = url
        self.quality = quality
        self.location = path

    # Asks the URL and checks the internet
    def get_url(self):
        print("Enter the URL of playlist")
        # This block of code checks the syntax of the input
        while True:
            url = input()
            try:
                url.index("https://")
                break
            except ValueError:
                print("Invalid Input. Enter the URL again")
                continue
        self.url = url

    # Checks the internet connection and notifies the user
    def check_internet(self):
        flag = 0
        # Check the internet and hang the script until the connection activates
        while True:
            try:
                response = urllib.request.urlopen(self.url)
                self.source_code = str(response.read())
                if flag:
                    print("Connected to the remote server")
                return True
            except Errors.URLError:
                if flag == 0:
                    print("Could not connect to the remote server. Check your internet connection")
                    flag = 1
                continue

    # This function determines whether the entered url is of a valid playlist or not
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
        fp = open("url.txt", "w+")
        fp.write(self.url)
        fp.close()

    # This function gets the name of the folder
    def get_name(self):
        index = self.source_code.index("<title>")
        index += len("<title>")
        name = self.source_code[index:]
        index = name.index("-")
        name = name[:index]
        self.name = name

    # This function counts the total number of videos present in the playlist
    def count_videos(self):
        temp_index = self.source_code.index("pl-header-details")
        part_of_code = self.source_code[temp_index:]

        temp_index = part_of_code.index("</li><li>")
        part_of_code = part_of_code[temp_index:]

        temp_index = part_of_code.index("videos") - 1

        part_of_code = part_of_code[0:temp_index]
        part_of_code = part_of_code[9:]
        number_of_videos = int(part_of_code)
        self.num = number_of_videos

    # This function displays the number of videos in the playlist
    def total_videos(self):
        print("The total number of videos in the playlist " + self.name + " are " + str(self.num))

    # This function scraps and stores the url of each video in list data member
    def get_video_links(self):
        code = self.source_code

        for i in range(self.num):
            a = code.index("pl-video-title-link yt-uix-tile-link yt-uix-sessionlink")
            code = code[a:]  # list slicing
            a = 0
            b = code.index("pl-video-bottom-standalone-badge")
            link = code[a:b]

            x = link.index('href')
            y = link.index("data-sessionlink") - 2
            x += 6
            link = link[x:y]

            code = code[b:]

            link = "https://www.youtube.com" + link
            self.list.append(link)  # inbuilt list function

    # This function prompts the user for the location at which playlist is to be saved
    def get_path(self):
        print("Enter the file location to be saved")
        while True:
            try:
                path = input()
                if not os.path.exists(path):  # exists() check whether the entered path exists or not
                    os.mkdir(path)  # if path does not exists mkdir() creates it
                break
            except FileNotFoundError:
                print("Invalid Path. Enter the path again")
                continue
            except OSError:
                print("The filename, directory name, or volume label syntax is incorrect: " + "'" + path + "'")
                continue

        self.location = path
        fp = open("path.txt", "w+")
        fp.write(self.location)
        fp.close()

    # This functions prompts the user for the videos quality of the playlist
    def get_quality(self):
        print("The playlist is available in following resolutions:")
        print("High\nMedium\nLow")

        while True:
            try:
                quality = input()
                quality = quality.lower()
            except KeyboardInterrupt:
                continue
            if quality != "high" and quality != "medium" and quality != "low":
                print("Invalid input. Enter again.")
            else:
                break
        self.quality = quality
        fp = open("qua.txt", "w+")
        fp.write(self.quality)
        fp.close()

    # This functions downloads the individual video of the playlist
    def save(self):
        for video_url in self.list:
            temp_video = video()
            temp_video.set_playlist_video_url(video_url)
            temp_video.set_from_quality(self.quality, self.location)
            temp_video.save()

        winsound.MessageBeep()
