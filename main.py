import pafy
import urllib.request

print("Enter the URL of playlist");
playlist=input();

print("Enter the total number of videos");
num=int(input());

response=urllib.request.urlopen(playlist)
str=str(response.read())

for i in range(num):
    a=str.index("pl-video-title-link yt-uix-tile-link yt-uix-sessionlink")
    str=str[a:]
    a=0;
    b=str.index("pl-video-bottom-standalone-badge")
    link=str[a:b]

    x=link.index('href')
    y=link.index("data-sessionlink")-2
    x=x+6
    link=link[x:y]

    
    str=str[b:]
    
    print("https://www.youtube.com"+link+"\n")


    
