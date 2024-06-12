from pytube import YouTube

def download_video(url, resolution):
    try:
        yt = YouTube(url)

        print(f"Downloading {yt.title} ...")

        stream = yt.streams.filter(progressive=True, res=resolution).first()

        if stream:
            stream.download()
            print(f"Downloaded {yt.title} at {resolution}")
        else:
            print(f"Resolution {resolution} not available for this video. Available resolutions are:")
            for s in yt.streams.filter(progressive=True):
                print(f" - {s.resolution}")

    except Exception as e:
        print("Something went wrong make sure the link is right")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    resolution = input("Enter desired resolution (In this format: 720p, 1080p): ")
    download_video(url, resolution)

