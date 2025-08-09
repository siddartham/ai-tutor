from pytubefix import YouTube


def download_audio(audio_link):
    video_url = audio_link.strip()
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename="audio.m4a")
