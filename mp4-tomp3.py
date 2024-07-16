from moviepy.editor import *
video = VideoFileClip("C:/Users/Admin/Downloads/Video/Top 100 Songs From 60's - 60's के हिट गाने - HD Songs - All Songs From 60's - Lata M -Kishore Kumar.mp4")

# Extract audio from video
video.audio.write_audiofile("C:/Users/Admin/Downloads/Video/Top 100 Songs From 60's.mp3")