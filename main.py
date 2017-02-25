import pafy
import urllib.request

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
print(num)

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

    print("https://www.youtube.com" + link + "\n")



