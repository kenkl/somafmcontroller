#!/usr/bin/env python3

from tkinter import *
import requests, json

URL='http://claire.kenkl.org:5000/'
FONT="Ariel"
NORMAL="normal"
SIZE=14
W="W"
E="E"
streamslist = []
streams = []

def getstreams():
	global streamslist, streams
	resp = requests.get(f'{URL}streamlist')
	resp.raise_for_status()
	streams = json.loads(resp.text)
	for i in streams:
		streamslist.append(i['title'])

def playstream():
	streamtitle = selection.get()
	for i in streams:
		if i['title'] == streamtitle:
			streamid = i['id']
	streamurl = f'{URL}play?stream={streamid}'
	r=requests.get(streamurl)
	r.raise_for_status()

def stopstream():
	r = requests.get(f'{URL}stop')
	r.raise_for_status()

def volup():
	r = requests.get(f'{URL}volup')
	r.raise_for_status()

def voldown():
	r = requests.get(f'{URL}voldown')
	r.raise_for_status()

#------- UI Setup -------
   
window = Tk()
window.title('SomaFM Controller')
window.config(padx=10, pady=10)

title_label = Label(text="SomaFM Controller", font=(FONT, 20, "bold"))
title_label.grid(column=0, row=0, columnspan=3)

host_label = Label(text=f'Host: {URL}', font=(FONT, SIZE, NORMAL))
host_label.grid(column=0, row=1, sticky=W, columnspan = 3)

spacer_label = Label(text="  ", font=(FONT, SIZE, NORMAL))
spacer_label.grid(column=0, row=2)

stream_label = Label(text="Stream:", font=(FONT, SIZE, NORMAL))
stream_label.grid(column=0, row=3, sticky=W)

getstreams()
selection = StringVar(window)
selection.set("Select")
stream_menu = OptionMenu(window, selection, *streamslist)
stream_menu.config(width = 20)
stream_menu.grid(column=0, row=4, sticky=W)

play_button = Button(text=" PLAY ", command=playstream)
play_button.grid(column=1, row=4, sticky=E)

stop_button = Button(text=" STOP ", command=stopstream)
stop_button.grid(column=2, row=4, sticky=E)

vol_label = Label(text="Volume: ", font=(FONT, SIZE, NORMAL))
vol_label.grid(column=0, row=5, sticky=E)

volup_button = Button(text="+", command=volup)
volup_button.grid(column=1, row=5)

voldown_button = Button(text="-", command=voldown)
voldown_button.grid(column=2, row=5)


window.mainloop()