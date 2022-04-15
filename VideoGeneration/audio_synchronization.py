from moviepy.editor import *

audioclip = AudioFileClip("data_test1.wav")
videoclip = VideoFileClip("video.avi")

videoclip2 = videoclip.set_audio(audioclip)

videoclip2.write_videofile('video1.mp4')