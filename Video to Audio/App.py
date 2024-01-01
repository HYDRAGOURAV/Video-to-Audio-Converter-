import moviepy.editor
from tkinter.filedialog import *
vid = askopenfilename()
video =moviepy.editor.VideoFileClip(vid)# you can also Give Your Video Location 
print("Your video has been loaded!")
aud = video.audio
aud.write_audiofile("demo.mp3")
print("_---------------------END--------------------")