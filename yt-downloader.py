from pytube import YouTube
from pytube import Playlist
import sys
import glob

# Storage path for downloads
DOWNLOADPATH = "downloads/"

# List of video's to fetch
VIDEOS = "videos.txt"

# Returns list of urls to download
def readFile(filename) -> list:
    url = []
    with open(filename, 'r') as file:
        for line in file:
            url.append(line.rstrip('\n'))
    return url

def checkFileExists(path, filename) -> bool:
    if glob.glob(path + filename  + ".*"):
        return True
    else:
        return False

# Grabs highest quality audio only stream and downloads if new
def downloadNewVideo(urlList) -> None:
    for url in urlList:
        yt = YouTube(url)
        if checkFileExists(DOWNLOADPATH, yt.title) == True:
            print(f"{yt.title} exists already skipping")
            continue
        else:
            print(f"Downloading {yt.title}")
            yt.streams.filter(adaptive=True, only_audio=True).first().download(DOWNLOADPATH)

def main():
    # Download any arguments passed to the program from command line
    if len(sys.argv) > 1:
        downloadNewVideo(sys.argv[1:])

    # Event Horizon
    downloadNewVideo(readFile(VIDEOS))


if __name__ == "__main__":
    main()
else:
    print("This is a standalone program")