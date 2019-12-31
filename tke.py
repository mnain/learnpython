#!/usr/bin/env python
  
import sys
import os
import tkinter
import subprocess
import time
import glob

def cleanLogs():
    outFiles = glob.glob('output*log')
    print(outFiles)
    for o in outFiles:
        os.remove(o)
    errFiles = glob.glob('error*log')
    print(errFiles)
    for e in errFiles:
        os.remove(e)

def download(url, audio):
    print("Url: "+url+" audio: "+audio)
    if audio.startswith('Audio'):
        cmds = ["python youtube-dl --no-progress -i -x --audio-format  mp3 --no-check-certificate "+url,]
    if audio.startswith('Video'):
        cmds = ["python youtube-dl --no-progress -f mp4 --no-check-certificate "+url,]
    print(cmds)
    timeStamp = time.strftime("%H%M%S")
    stdoutName = "output_"+timeStamp+".log"
    stderrName = "error_"+timeStamp+".log"
    print("Filenames {} {}".format(stdoutName, stderrName))
    stdoutFh = open(stdoutName, 'wt')
    stderrFh = open(stderrName, 'wt')
    rc = subprocess.run(cmds, stdout=stdoutFh, stderr=stderrFh, shell=True)
    print("RC = {}".format(rc))
    stdoutFh.close()
    stderrFh.close()
def handleEntry():
    global lbl
    txt = entry.get()
    print("Entry:" + txt)
    svar.set(txt)
    aOnly = audioVar.get()
    print(aOnly)
    print(dir(audioVar))
    lbl.update()
    download(txt, aOnly)

if __name__ == "__main__":
    cleanLogs()
    root = tkinter.Tk()
    entry = tkinter.Entry(width=45)
    entry.pack(),
    svar = tkinter.StringVar()
    svar.set('NONE')
    lbl = tkinter.Label(width=80, textvariable=svar)
    lbl.pack()
    audioVar = tkinter.StringVar()
    audioVar.set('Audio')
    audioOnly = tkinter.Checkbutton(text="Audio only", variable=audioVar, onvalue='Audio', offvalue='Video')
    audioOnly.pack()
    btn1 = tkinter.Button(text="Submit", command=handleEntry)
    btn1.pack()
    quit = tkinter.Button(text="Quit", command="exit")
    quit.pack()
    lbl.text = 'So far'
    lbl.update()
    root.mainloop()
