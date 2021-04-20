import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

HEIGHT = 700
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='chicago2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

title = tk.Label(root, text="Chicago Crime Analysis", font=('Open Sans', 25))
title.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

upperFrame = tk.Frame(root, bg='#76b5c5', bd=10)
upperFrame.place(relx=0.5, rely=0.17, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(upperFrame, text="Get Analysis", font=('Open Sans', 12), command=lambda: mainFunc(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

entry = tk.Entry(upperFrame, font=('Open Sans', 12))
entry.place(relwidth=0.65, relheight=1)

lowerFrame = tk.Frame(root, bg='#76b5c5', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

lowerLabel = tk.Label(lowerFrame, justify=LEFT, anchor=NW)
lowerLabel.place(relwidth=1, relheight=0.775, rely= 0.225)

textLabel = tk.Label(lowerFrame, justify=LEFT, anchor=NW)
textLabel.place(relwidth=1, relheight=0.20, rely= 0)

url = 'https://data.cityofchicago.org/api/views/kn9c-c2s2/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

url2 = 'https://github.com/k-chuang/chicago-crime-data-analysis/blob/master/Crimes_-_2001_to_present.csv?raw=true'
df_main = pd.read_csv(url2)

def getHardShipIndex(entry):
	try:
		intEntry = int(entry)
		if (intEntry > 0 and intEntry < 78):
			df_area = df[['Community Area Number', 'COMMUNITY AREA NAME', 'HARDSHIP INDEX']]
			is_area = df_area['Community Area Number'] == intEntry
			df_return = df_area[is_area]
			name_str = df_return.to_string(columns=['COMMUNITY AREA NAME'], header=False, index=False)
			hardship_str = df_return.to_string(columns=['HARDSHIP INDEX'], header=False, index=False)
			textLabel['text'] = "Area Name:" + name_str + "\nHardship Index:" + hardship_str
		else:
			final_str = 'Entry is not a valid community number'
			textLabel['text'] = final_str				
	except:
		final_str = 'Entry is not a valid community number'
		textLabel['text'] = final_str


def getAnalysis(entry):
	try:	
		intEntry = int(entry)	
		if (intEntry > 0 and intEntry < 78):
			lowerLabel = tk.Label(lowerFrame, justify=LEFT, anchor=NW)
			lowerLabel.place(relwidth=1, relheight=0.775, rely= 0.225)
			is_area = df_main['Community Area'] == intEntry
			df_area = df_main[is_area]
			df_typeCount = df_area['Primary Type'].value_counts().head(10)
			fig = Figure(figsize = (4.3, 3), dpi = 90)
			ax = fig.add_subplot(111)
			df_typeCount.plot(kind = 'pie', ax= ax)
			canvasFig = FigureCanvasTkAgg(fig, master = lowerLabel)
			canvasFig.draw()
			canvasFig.get_tk_widget().pack()
		else:
			final_str = 'Entry is not a valid community number'
			lowerLabel['text'] = final_str	
	except:
		final_str = 'Entry is not a valid community number'
		lowerLabel['text'] = final_str
				
def mainFunc(entry):
	getAnalysis(entry)
	getHardShipIndex(entry)

root.mainloop()
