from pytube import Playlist

link = input("Please enter your YouTube's Playlist: ")
play = Playlist(link)
print("\nYour Playlist's Title: ", play.title)

for video in play.videos:
    video.streams.second().download()

print("\nYour Download is COMPLETED!")
