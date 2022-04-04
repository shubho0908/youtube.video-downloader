import string
from pytube import YouTube

print("Welcome to the YouTube Video/Audio Downloader\n")
link = input("Please Enter your video's URL: ")
youtube_1 = YouTube(link)

print("\nYour video's Title is:", youtube_1.title)
data = input(
    "\nIn which format you wanna download the video? (Audio or Video) ")
if data == "Audio":
    audio = youtube_1.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    print()

    strm = int(input("Enter your preferrable option: "))
    audio[strm].download()
    print("\nYour Download is COMPLETED!")

elif data == "Video":
    video = youtube_1.streams.all()
    vid = list(enumerate(video))
    for a in vid:
        print(a)
    print()

    strm_1 = int(input("Enter your preferrable option: "))
    video[strm_1].download()
    print("\nYour Download is COMPLETED!")
