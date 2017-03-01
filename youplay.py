import pafy
import urllib.request
import os, sys
import winsound

print("Enter the URL of playlist");
playlist = input();

print("The total number of videos are", end=" ");

response = urllib.request.urlopen(playlist)
str = str(response.read())

p = str.index("pl-header-details")
number_of_videos = str[p:]

p = 0
p = number_of_videos.index("</li><li>")
number_of_videos = number_of_videos[p:]

p = 0
p = number_of_videos.index("videos") - 1

number_of_videos = number_of_videos[0:p]
number_of_videos = number_of_videos[9:]
number_of_videos = int(number_of_videos)
num = number_of_videos

if (num > 100):
    num = 100

print(num)

list = []

for i in range(num):
    a = str.index("pl-video-title-link yt-uix-tile-link yt-uix-sessionlink")
    str = str[a:]
    a = 0;
    b = str.index("pl-video-bottom-standalone-badge")
    link = str[a:b]

    x = link.index('href')
    y = link.index("data-sessionlink") - 2
    x = x + 6
    link = link[x:y]

    str = str[b:]

    link = "https://www.youtube.com" + link
    list.append(link)

print("Enter the number of video from which to begin download")
begin = int(input())

print("Enter the number of video on which to end download")
end = int(input())

print("Enter the file location to be saved")
path = input()

if (os.path.exists(path) == False):
    os.mkdir(path)

del str
os.chdir(path)

for i in range(begin, end + 1):
    object = pafy.new(list[i - 1])
    video = object.getbest()
    filename = video.download()
    fp = open("data.txt", "w+")
    fp.write(str(i))

fp.close()

winsound.Beep(350,500)