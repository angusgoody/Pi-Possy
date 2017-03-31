# coding=utf-8


#=============================IMPORTS=============================
from tkinter import *
from tkinter import messagebox

#=============================WINDOW SETUP=============================
window=Tk()
window.title("PETER 2.0")
window.geometry("500x400")

#=============================PRE FUNCTION SETUPS=================================

#==============HEX FUNCTIONS================

def convertHex(value,intoDecOrHex):
	"""
	Convert a decimal to hex or hex to decimal
	"""
	if intoDecOrHex == "Decimal":
		return int("0x" + str(value), 16)
	else:
		hexValue = "#"
		hexValue = hexValue + str((format(value, '02x')).upper())
		return hexValue




def getHexSections(hexValue):
	"""
	This will split a 6 digit hex number into pairs and store them
	in an array
	"""
	if len(hexValue) <= 7 and "#" in hexValue:
		#Removes the #
		colourData = hexValue.replace("#", "")
		# Split HEX number into pairs
		colourSections = [colourData[i:i + 2] for i in range(0, len(colourData), 2)]
		return colourSections

def getDecimalHexSections(hexValue):
	hexSections=getHexSections(hexValue)
	decimalArray=[]
	for item in hexSections:
		decimalValue=convertHex(item,"Decimal")
		decimalArray.append(decimalValue)
	return decimalArray


def getColourForBackground(hexValue):
	"""
		This function will return white or black as a text colour
		depending on what the background colour passed to it is. For
		example if a dark background is passed then white will be returned because
		white shows up on dark best.
	"""
	chosenColour="Black"
	whiteCounter = 0

	#Checks the hex number is standard
	if len(hexValue) <= 7 and "#" in hexValue:

		colourSections=getHexSections(hexValue)
		for x in colourSections:
			#Convert to decimal
			y=convertHex(x,"Decimal")
			#If its less than half way between 0 and FF which is 255
			if y < 128:
				whiteCounter += 1
		if whiteCounter > 1:
			#White is returned
			chosenColour = "#ffffff"
		else:
			#Black is returned
			chosenColour = "#000000"
	return chosenColour

#==============UTILITY FUNCTIONS================

#=============================CLASSES=================================

class mainFrame(Frame):
	"""
	This is a modified frame class which 
	can be modified for every frame on screen. It 
	automatically changes colours and updates text colours
	 so they appear on dark/light background
	"""
	def __init(self,parent):
		Frame.__init__(self,parent)

	#Update colour method
	def colour(self,chosenColour):

		#Get FG colour for selected colour
		fgColour=getColourForBackground(chosenColour)
		widgetArray =["Entry", "Button", "Text", "Listbox", "OptionMenu", "Menu"]

		#Update frame itself
		self.config(bg=chosenColour)

		#Recursivley search through all children and change colour
		children=self.winfo_children()
		for child in children:
			if child.winfo_class() == mainFrame:
				child.colour(child,chosenColour)
			else:
				if child.winfo_class() in widgetArray:
					child.config(highlightbackground=chosenColour)
				else:
					child.config(bg=chosenColour)

				#Update labels so they show up on certain colours
				if child.winfo_class() == "Label":
					child.config(fg=fgColour)

	#Add a binding function to the frame and children
	def addBinding(self,bindFunction):
		self.bind("<Double-Button-1>",bindFunction)

		#Recursivley search through all children and add binding
		children = self.winfo_children()
		for child in children:
			if child.winfo_class() == mainFrame:
				child.addBinding(child,bindFunction)
			else:
				child.bind("<<Double-Button-1>",bindFunction)

class screenClass(mainFrame):
	"""
	Class for screen that is based off the Frame class
	"""
	screenArray=[]
	lastScreen=None
	def __init__(self,name):
		#Initialise the instance as a frame as well
		mainFrame.__init__(self,window)
		self.name=name
		screenClass.screenArray.append(self)


	def show(self):
		"""
		This makes sure the current screen isn't reloaded
		"""
		if self != screenClass.lastScreen:
			for item in screenClass.screenArray:
				item.pack_forget()
			self.pack(expand=True, fill=BOTH)
			statusVar.set(self.name)
			screenClass.lastScreen=self


	def getChildren(self):
		children=self.winfo_children()
		return children



#=============================MAIN UI SETUP=================================
#Status bar
statusVar=StringVar()
statusVar.set("")
statusFrame=mainFrame(window)
statusFrame.pack(side=BOTTOM,fill=X)
status=Label(statusFrame,textvariable=statusVar,font="Arial 15 bold")
status.pack(expand=True)
statusFrame.colour("#B2FF00")


#Home screen
homeScreen=screenClass("Home")
homeScreen.colour("#f8c13b")

tempScreen=screenClass("TEMP")
tempScreen.colour("#ff4bb8")

#=============================FUNCTIONS=============================

#=============================BINDINGS=============================
statusFrame.addBinding(homeScreen.show())
tempScreen.show()
#=============================MAIN RETURN=============================
window.mainloop()