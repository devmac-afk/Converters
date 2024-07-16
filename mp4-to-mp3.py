from moviepy.editor import *
video = VideoFileClip("Paste your video full path HERE with \".mp4\" at the end")

# Extract audio from video
video.audio.write_audiofile("Paste your full path where you wanna save your audio file HERE with \".mp3\" ")
