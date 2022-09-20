import os
from moviepy.editor import *

def mp4_to_mp3(mp4, mp3):
            mp4_without_frames = AudioFileClip(mp4)
            mp4_without_frames.write_audiofile(mp3)
            mp4_without_frames.close()

mp4_to_mp3("C:/Users/Adrian/Desktop/Youtube Video Downloader GUI App Using Python and Tkinter.mp4",
           "C:/Users/Adrian/Desktop/Youtube Video Downloader GUI App Using Python and Tkinter.mp3")
os.remove("C:/Users/Adrian/Desktop/Youtube Video Downloader GUI App Using Python and Tkinter.mp4")