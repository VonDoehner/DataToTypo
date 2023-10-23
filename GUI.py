import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/6.0_1/bin/ffmpeg"
from moviepy.editor import VideoFileClip, concatenate_videoclips, afx, vfx
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk



###Erstelle das Anwendungshauptfenster
root = tk.Tk()
root.title("Predigt ins WWW")
root.geometry("600x800")


###Erstelle ein äusseres Frame
outer_Frame = tk.Frame(root, borderwidth=1, relief="ridge")
outer_Frame.pack(pady=8, padx=8)


###Create the global VAR-list to catch all Variables for use in the video editing
Varx = {}

###Create the placeholder for the check_img, the check_img aswell as an empty image and make them usable in tk.Labels
placeholder_img_raw = Image.open("data/V1_empty.png")
placeholder_img_resized = placeholder_img_raw.resize((18, 18), Image.LANCZOS)
placeholder_img = ImageTk.PhotoImage(placeholder_img_resized)

check_img_raw = Image.open("data/V1_check.png")
check_img_resized = check_img_raw.resize((18, 18), Image.LANCZOS)
check_img = ImageTk.PhotoImage(check_img_resized)

empty_img_raw = Image.open("data/img_empty.png")
empty_img_resized = empty_img_raw.resize((18, 18), Image.LANCZOS)
empty_img = ImageTk.PhotoImage(empty_img_resized)


###Define the function for finding files on the device and putting them into the dictionary
###under a specific Variable Number, aswell as placing the check
def findVar(VarNum, PlaceHolderName):
    global Varx
    Varx["Var" + str(VarNum)] = filedialog.askopenfilename()
    PlaceHolderName.config(image=check_img)
    print(Varx)


###Create the first inner frame to house the file search buttons
inner_frame_1 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge")
inner_frame_1.columnconfigure(0, weight=1)
inner_frame_1.grid(row=0, column=0, sticky="w", pady=6, padx=10)


###Button for finding the Intro_ File and the placeholder for the check_img
plh1 = tk.Label(inner_frame_1, image=placeholder_img)
plh1.grid(row=0, column=1)
btn1 = tk.Button(inner_frame_1, text="Suche das Introvideo", font=("Helvetica", 14), command=lambda: findVar(1, plh1))
btn1.grid(row=0, column=0, sticky="w", pady=6, padx=10)




###Button for finding the Predigt_videofile aswell as the placeholder for the ckeck_img
plh2 = tk.Label(inner_frame_1, image=placeholder_img)
plh2.grid(row=1, column=1)
btn2 = tk.Button(inner_frame_1, text="Suche das Predigtvideo", font=("Helvetica", 14), command=lambda: findVar(2, plh2))
btn2.grid(row=1, column=0, sticky="w", pady=6, padx=10)



###Define the Start and Endtime for the Intro Video in a seperate nested grid

###Function for calculating and putting the entered time in the list under the right variables

def TimeToDict(VarNum, MinSpinBox, SecSpinBox, PlaceHolderName):
    global Varx
    Varx["Var" + str(VarNum)] = float(int(MinSpinBox.get()) * 60 + float(SecSpinBox.get()))
    PlaceHolderName.config(image=check_img)
    print(Varx)

###Denfine the start time
inner_frame_2 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge")
inner_frame_2.columnconfigure(0, weight=0)
inner_frame_2.grid(row=2, column=0, sticky="w", pady=6, padx=10)

lbl1 = tk.Label(inner_frame_2, text="Definiere eine Anfangs- und eine Schlusszeit für das Intro", font=("Helvetica", 16))
lbl1.grid(row=0, column=0, sticky="w")

lbl2 = tk.Label(inner_frame_2, text="Anfangszeitpunkt:", font=("Helvetica", 12))
lbl2.grid(row=1, column=0, sticky="w")

lbl4 = tk.Label(inner_frame_2, text="Minute:", font=("Helvetica", 9))
lbl4.grid(row=2, column=0, sticky="w")
spb1 = tk.Spinbox(inner_frame_2, from_=0, to=999, width=4)
spb1.grid(row=2, column=0)

lbl5 = tk.Label(inner_frame_2, text="Sekunde:", font=("Helvetica", 9))
lbl5.grid(row=2, column=3, sticky="w")
spb2 = tk.Spinbox(inner_frame_2, from_=0, to=60, width=4)
spb2.grid(row=2, column=4, sticky="w")

plh3 = tk.Label(inner_frame_2, image=placeholder_img)
plh3.grid(row=3, column=3, sticky="w")
btn3 = tk.Button(inner_frame_2, text="Startzeit speichern", font=("Helvetica", 14), command=lambda: TimeToDict(3, spb1, spb2, plh3))
btn3.grid(row=3, column=0, sticky="e")

###Define the end timestamp for the Intro vide

###add the placeholder_img to row 4 to add some verzical space
plh4 = tk.Label(inner_frame_2, image=empty_img)
plh4.grid(row=4, column=0)

lbl7 = tk.Label(inner_frame_2, text="Endzeitpunkt:", font=("Helvetica", 12))
lbl7.grid(row=5, column=0, sticky="w")

lbl9 = tk.Label(inner_frame_2, text="Minute:", font=("Helvetica", 9))
lbl9.grid(row=6, column=0, sticky="w")
spb3 = tk.Spinbox(inner_frame_2, from_=0, to=999, width=4)
spb3.grid(row=6, column=0)

lbl10 = tk.Label(inner_frame_2, text="Sekunde:", font=("Helvetica", 9))
lbl10.grid(row=6, column=3, sticky="w")
spb4 = tk.Spinbox(inner_frame_2, from_=0, to=60, width=4)
spb4.grid(row=6, column=4, sticky="w")

plh5 = tk.Label(inner_frame_2, image=placeholder_img)
plh5.grid(row=7, column=3, sticky="w")
btn4 = tk.Button(inner_frame_2, text="Schlusszeit speichern", font=("Helvetica", 14), command=lambda: TimeToDict(4, spb3, spb4, plh5))
btn4.grid(row=7, column=0, sticky="e")



######
######
######



###Denfine the start time Predigt
inner_frame_3 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge")
inner_frame_3.columnconfigure(0, weight=0)
inner_frame_3.grid(row=3, column=0, sticky="w", pady=6, padx=10)


lbl11 = tk.Label(inner_frame_3, text="Definiere eine Anfangs- und eine Schlusszeit für die Predigt", font=("Helvetica", 16))
lbl11.grid(row=0, column=0, sticky="w")

lbl12 = tk.Label(inner_frame_3, text="Anfangszeitpunkt:", font=("Helvetica", 12))
lbl12.grid(row=1, column=0, sticky="w")

lbl14 = tk.Label(inner_frame_3, text="Minute:", font=("Helvetica", 9))
lbl14.grid(row=2, column=0, sticky="w")
spb5 = tk.Spinbox(inner_frame_3, from_=0, to=999, width=4)
spb5.grid(row=2, column=0)

lbl15 = tk.Label(inner_frame_3, text="Sekunde:", font=("Helvetica", 9))
lbl15.grid(row=2, column=3, sticky="w")
spb6 = tk.Spinbox(inner_frame_3, from_=0, to=60, width=4)
spb6.grid(row=2, column=4, sticky="w")

plh6 = tk.Label(inner_frame_3, image=placeholder_img)
plh6.grid(row=3, column=3, sticky="w")
btn5 = tk.Button(inner_frame_3, text="Startzeit speichern", font=("Helvetica", 14), command=lambda: TimeToDict(5, spb5, spb6, plh6))
btn5.grid(row=3, column=0, sticky="e")

###Define the end timestamp for the Intro vide

###add the placeholder_img to row 4 to add some verzical space
plh7 = tk.Label(inner_frame_3, image=empty_img)
plh7.grid(row=4, column=0)

lbl17 = tk.Label(inner_frame_3, text="Endzeitpunkt:", font=("Helvetica", 12))
lbl17.grid(row=5, column=0, sticky="w")

lbl19 = tk.Label(inner_frame_3, text="Minute:", font=("Helvetica", 9))
lbl19.grid(row=6, column=0, sticky="w")
spb7 = tk.Spinbox(inner_frame_3, from_=0, to=999, width=4)
spb7.grid(row=6, column=0)

lbl20 = tk.Label(inner_frame_3, text="Sekunde:", font=("Helvetica", 9))
lbl20.grid(row=6, column=3, sticky="w")
spb8 = tk.Spinbox(inner_frame_3, from_=0, to=60, width=4)
spb8.grid(row=6, column=4, sticky="w")

plh8 = tk.Label(inner_frame_3, image=placeholder_img)
plh8.grid(row=7, column=3, sticky="w")
btn6 = tk.Button(inner_frame_3, text="Schlusszeit speichern", font=("Helvetica", 14), command=lambda: TimeToDict(6, spb7, spb8, plh8))
btn6.grid(row=7, column=0, sticky="e")




######
######
######

###Define further Video settings

#Define function to send the entered factors to the Varx dictionary

def DecimalsToDictionary(VarNum=0, VarNumList=[], MultipleFactorsBoolean=False, SpinBox=0, SpinBoxList=[], PlaceHolder=0):
    global Varx
    i = 0
    if MultipleFactorsBoolean == True:
        for item in SpinBoxList:
            Varx["Var" + str(VarNumList[i])] = float(SpinBoxList[i].get())
            i += 1

    else:
        Varx["Var" + str(VarNum)] = SpinBox.get()

    PlaceHolder.config(image=check_img)

    print(Varx)



#Create the GUI
inner_frame_4 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge")
inner_frame_4.columnconfigure(0, weight=0)
inner_frame_4.grid(row=4, column=0, sticky="w", pady=6, padx=10)

lbl21 = tk.Label(inner_frame_4, text="Weitere Video- und Audioeinstellungen", font=("Helvetica", 16))
lbl21.grid(row=0, column=0, sticky="w")

lbl22 = tk.Label(inner_frame_4, text="Faktor Lautstärke Intro:", font=("Helvetica", 12))
lbl22.grid(row=1, column=0, sticky="w")

lbl23 = tk.Label(inner_frame_4, text="Faktor (0 = stumm, 1=keine Änderung, 2=doppelte Lautstärke)", font=("Helvetica", 9))
lbl23.grid(row=2, column=0, sticky="w")

spb9 = tk.Spinbox(inner_frame_4, from_=0, to=8, increment=0.1, width=3)
spb9.grid(row=2, column=1, sticky="w")

###add the placeholder_img to row 4 to add some verzical space
plh7 = tk.Label(inner_frame_4, image=empty_img)
plh7.grid(row=3, column=0)

lbl25 = tk.Label(inner_frame_4, text="Faktor Lautstärke Predigt", font=("Helvetica", 12))
lbl25.grid(row=4, column=0, sticky="w")

lbl26 = tk.Label(inner_frame_4, text="Faktor (0 = stumm, 1=keine Änderung, 2=doppelte Lautstärke)", font=("Helvetica", 9))
lbl26.grid(row=5, column=0, sticky="w")

spb10 = tk.Spinbox(inner_frame_4, from_=0, to=8, increment=0.1, width=3)
spb10.grid(row=5, column=1, sticky="w")

plh8 = tk.Label(inner_frame_4, image=placeholder_img)
plh8.grid(row=6, column=1, sticky="w")
btn7 =tk.Button(inner_frame_4, text="Eingabe speichern", font=("Helvetica", 12), command=lambda: \
    DecimalsToDictionary(MultipleFactorsBoolean=True, SpinBoxList=[spb9, spb10], VarNumList=[7, 8], PlaceHolder=plh8))
btn7.grid(row=6, column=0, sticky="e")


###
###
###


#Buttons for exporting and uploading to web aswell as the video editing function

#The function for actually processing the videos with the entered data
def VideoEditing(Varx):

    Var1 = Varx["Var1"]
    Var2 = Varx["Var2"]
    Var3 = Varx["Var3"]  # Intro_Starttime
    Var4 = Varx["Var4"]  # Intro_Endtime
    Var5 = Varx["Var5"]  # Predigt_Starttime
    Var6 = Varx["Var6"]  # Predigt_Endtime
    Var7 = Varx["Var7"]  # Factor_audio_intro_volume
    Var8 = Varx["Var8"]  # Time_Fadeout (in seconds)

    print(Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8)

    ###Load and edit the Videfiles
    # Load the Intro from the Variable, adjust the Volume
    Intro = VideoFileClip(Var1).subclip(Var3, Var4).fx(afx.volumex, Var7)

    # Load the Predigt from the Variable, load tonly the videodata between the timestamps, add a fadeout at the end
    Predigt = VideoFileClip(Var2).subclip(Var5, Var6).fx(vfx.fadeout, Var6)

    # Put together the Intro and the Predigt
    Gesamt = concatenate_videoclips([Intro, Predigt])

    # Take the audio from the Predigt videofile
    Predigt_audio = Predigt.audio

    ###Export the mp3 and the concatenated Videofile
    Predigt_audio.write_audiofile("Test_1.mp3")
    Gesamt.write_videofile("Test_1.mp4")


#The function for  removing all current widgets from the window and placing the export and upload options
def PlaceUploadOptions():

    #Remove the previous inner frames
    inner_frame_1.grid_forget()
    inner_frame_2.grid_forget()
    inner_frame_3.grid_forget()
    inner_frame_4.grid_forget()
    inner_frame_5.grid_forget()

    #Place the new elements with the upload options
    inner_frame_6 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge" )
    inner_frame_6.grid(row=1, column=0, sticky="w")

    






#Create the inner frame
inner_frame_5 = tk.Frame(outer_Frame, borderwidth=2, relief="ridge")
inner_frame_5.columnconfigure(0, weight=0)
inner_frame_5.grid(row=5, column=0, sticky="w", pady=6, padx=10)
btn8 = tk.Button(inner_frame_5, text="Videos exportieren", font=("Helvetica", 12), command=lambda: PlaceUploadOptions())
btn8.grid(row=1, column=0)






###Start the mainloop
root.mainloop()