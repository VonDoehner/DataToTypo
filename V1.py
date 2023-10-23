import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/6.0_1/bin/ffmpeg"
from moviepy.editor import VideoFileClip, concatenate_videoclips, afx, vfx


Varx = {'Var1': '/Users/silvanzechner/Desktop/Predigtuploader/LOGO_Petrol_weiss.mp4', 'Var2': '/Users/silvanzechner/Desktop/Predigtuploader/Predigt.MOV', 'Var3': 0.0, 'Var4': 7.0, 'Var5': 61.0, 'Var6': 122.0, 'Var7': 0.5, 'Var8': 1.0}


Var1 = Varx["Var1"]
Var2 = Varx["Var2"]
Var3 = Varx["Var3"] #Intro_Starttime
Var4 = Varx["Var4"] #Intro_Endtime
Var5 = Varx["Var5"] #Predigt_Starttime
Var6 = Varx["Var6"] #Predigt_Endtime
Var7 = Varx["Var7"] #Factor_audio_intro_volume
Var8 = Varx["Var8"] #Time_Fadeout (in seconds)

print(Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8)



###Load and edit the Videfiles
#Load the Intro from the Variable, adjust the Volume
Intro = VideoFileClip(Var1).subclip(Var3, Var4).fx(afx.volumex, Var7)

#Load the Predigt from the Variable, load tonly the videodata between the timestamps, add a fadeout at the end
Predigt = VideoFileClip(Var2).subclip(Var5, Var6).fx(vfx.fadeout, Var6)

#Put together the Intro and the Predigt
Gesamt = concatenate_videoclips([Intro, Predigt])

#Take the audio from the Predigt videofile
Predigt_audio = Predigt.audio



###Export the mp3 and the concatenated Videofile
Predigt_audio.write_audiofile("Test_1.mp3")
Gesamt.write_videofile("Test_1.mp4")