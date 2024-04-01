from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)

print("View:", yt.views)

yd = yt.streams.get_highest_resolution()

#put the path you want your video downloaded in
yd.download("C:\Users\IMANE\Downloads")