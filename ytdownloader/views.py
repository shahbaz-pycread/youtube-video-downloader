from django.shortcuts import render, redirect
from pytube import *

# defining funtion

def Youtubelink(request):
    # Checking whether request method is POST or not
    if request.method == 'POST':
        # Getting Link
        link = request.POST['link']
        yt_video = YouTube(link)

        # Setting Video Resolution
        stream = yt_video.streams.get_lowest_resolution()

        # Download Video
        stream.download("C:/videos/ytvideos_downloader")

        #Returninh HTML Page
        return render(request, 'main.html')
        
    return render(request, 'main.html')
