# coding=utf-8

#Angus Goody
#PETER 2.0
#1/04/17

#============================================(IMPORTS)================================================
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import random
import datetime
#============================================(WINDOW SETUP)================================================
window=Tk()
window.title("PETER 2.0")
window.geometry("500x400")
#============================================(MENU SETUP)================================================

#Main Menu
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub Menus
fileMenu=Menu(mainMenu)
editMenu=Menu(mainMenu)
studentMenu=Menu(mainMenu)
helpMenu=Menu(mainMenu)

#============================================(GLOBAL VARIABLES)================================================
maxLogSize=100

#============================================(GLOBAL ARRAYS)================================================
mainLogArray=[]

#============================================(EXTRA CODE SPACE)================================================
"""
This area is for code that needs to be
at the top of the program because it needs
to be declared before certain items
"""
#====================UI CLASSES====================

def recursiveChangeColour(parent,colour,fgColour):
	"""
	This function will recursivly search all children
	of an element and change their colour
	"""
	widgetArray =["Entry", "Button", "Text", "Listbox", "OptionMenu", "Menu"]
	parentClass=parent.winfo_class()
	if parentClass == "Frame":
		parent.config(bg=colour)
		children=parent.winfo_children()
		for item in children:
			recursiveChangeColour(item,colour,fgColour)
	else:
		try:
			#Certain widgets need diffrent attention
			if parent.winfo_class() in widgetArray:
					parent.config(highlightbackground=colour)
			else:
				parent.config(bg=colour)

			#Update labels so they show up on certain colours
			if parent.winfo_class() == "Label":
					parent.config(fg=fgColour)
		except:
			pass

def recursiveBind(parent,bindButton,bindFunction):
	"""
	This function is similar to the change colour function
	but it uses recursion to add a binding to every child
	"""
	parentClass=parent.winfo_class()
	if parentClass == "Frame":
		parent.bind(bindButton,bindFunction)
		children=parent.winfo_children()
		for item in children:
			recursiveBind(item,bindButton,bindFunction)
	else:
		try:
			parent.bind(bindButton,bindFunction)
		except:
			pass

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

		#Recursivley search through all children and change colour
		recursiveChangeColour(self,chosenColour,fgColour)

	#Add binding method
	def addBinding(self,bindButton,bindFunction):
		recursiveBind(self,bindButton,bindFunction)

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

	#Show screen method
	def show(self):
		if self != screenClass.lastScreen:
			for item in screenClass.screenArray:
				item.pack_forget()
			self.pack(expand=True, fill=BOTH)
			statusVar.set(self.name)
			screenClass.lastScreen=self

	#Get children method
	def getChildren(self):
		children=self.winfo_children()
		return children

class displayView(mainFrame):
	"""
	This is the class for displaying multiple frames
	of data on the screen. The frames are equally spaced
	apart and automatically adjust colour etc
	"""
	labelSections={}
	def __init__(self,parent):
		mainFrame.__init__(self,parent)
		self.frameArray=[]

	def addSection(self,colour,frameToDisplay):
		frameToDisplay.colour(colour)
		self.frameArray.append(frameToDisplay)

	def addLabelSection(self,text,colour,indentify):
		"""
		This method will add a small section to the display
		view with some text on. It does this by creating a pre
		made frame and using the addSection method
		"""
		#Creates the frame to display
		newFrame=mainFrame(self)
		Label(newFrame,text=text,font=font.Font(size=16)).pack(expand=True)
		self.addSection(colour,newFrame)
		#Add Frame to dictionary to track it using identifier string
		displayView.labelSections[indentify]=newFrame

	def addLabelCommand(self,identifier,bindButton,command):
		"""
		This method will use the identifier to add a binding
		command to a label section because they do not have a 
		deceleration in the main program. 
		"""
		if identifier in displayView.labelSections:
			instance=displayView.labelSections[identifier]
			instance.addBinding(bindButton,command)
		else:
			report("Unknown identifier:",identifier)

	def showSections(self):
		for item in self.frameArray:
			item.pack(expand=True, fill=BOTH)

#====================LOG SCREEN====================
#region logscreen
logScreen=screenClass("Logs")

columnArray=["Message","Time"]
allColumnArray=["Message","Time"]

#Display log widgets
logTree=ttk.Treeview(logScreen,columns=allColumnArray,show="headings")
logTree.pack(fill="both",expand=True)

logTree.column("Message",width=10,minwidth=45)
logTree.column("Time",width=5,minwidth=20)

logTree.heading("Message",text="Message")
logTree.heading("Time",text="Time")

#endregion

#============================================(PRE FUNCTIONS)================================================


#==============LOG FUNCTIONS================
def report(message,*extra):
	if len(extra) > 0:
		#Concatonate variables
		for item in extra:
			message+=" "
			message+=str(item)

	currentTime=datetime.datetime.now().time()
	temp=[message,currentTime]

	#Makes sure logArray isn't filled up
	if len(mainLogArray) < maxLogSize:
		mainLogArray.append(temp)
	else:
		print("Log array filled up")
	logTree.insert("" , 0,values=(message,currentTime))

#==============FILE FUNCTIONS================
def getContent(fileName):
	try:
		file=open(fileName)
	except:
		report("Error opening file",fileName)
	else:
		content=file.readlines()
		return content


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

def generateHexColour():
	"""
	This function will generate a random HEX colour

	"""
	baseNumber=random.randint(1,16777216)
	hexValue=convertHex(baseNumber,"Hex")
	hexLeng=len(hexValue)
	while hexLeng != 7:
		hexValue=hexValue+"0"
		hexLeng=len(hexValue)
	return hexValue
#============================================(CLASSES)================================================


#============================================(MAIN UI SETUP)================================================

#====================STATUS BAR====================
#region statusbar
statusVar=StringVar()
statusVar.set("")
statusFrame=mainFrame(window)
statusFrame.pack(side=BOTTOM,fill=X)
status=Label(statusFrame,textvariable=statusVar,font="Arial 15 bold")
status.pack(expand=True)
statusFrame.colour("#B2FF00")

#endregion
#====================HOME SCREEN====================
#region homescreen
homeScreen=screenClass("Home")

homeDisplayScreen=displayView(homeScreen)
homeDisplayScreen.pack(expand=True,fill=BOTH)

#Section setup

homeDisplayScreen.addLabelSection("Welcome","#52A341","Welcome")
homeDisplayScreen.addLabelSection("Total Pupils","#1EC5B0","Total")
homeDisplayScreen.addLabelSection("A-C Pupils","#21D6BF","Pass")
homeDisplayScreen.addLabelSection("D-F Pupils","#24ECD3","Fail")

homeDisplayScreen.showSections()

#endregion
#====================View All SCREEN====================

#============================================(MAIN FUNCTIONS)================================================

#=========UTILITY FUNCTIONS===========

def askMessage(pre,message):
	"""
	This function will launch the tkinter
	dialog and ask a question to user
	"""
	try:
		messagebox.showinfo(pre,message)
	except:
		print(message)

def insertEntry(entry,message):
	"""
	This function will add text into entry
	"""
	entry.delete(0,END)
	entry.insert(END,message)

#=========PROGRAM FUNCTIONS===========

def test():
	askMessage("LEO","Hi")
#============================================(MENUS/CASCADES)================================================

#============CASCADES==========

mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="Students",menu=studentMenu)
mainMenu.add_cascade(label="Help",menu=helpMenu)

#============CASCADES==========


#File Menu
fileMenu.add_command(label="Home",command=lambda: homeScreen.show())

#Edit Menu

#Help Menu
helpMenu.add_command(label="Show Log",command=lambda :logScreen.show())

#============================================(BINDINGS)================================================

#Status Bar
statusFrame.addBinding("<Double-Button-1>",lambda event: homeScreen.show())

#Home screen
homeDisplayScreen.addBinding("<Double-Button-1>",lambda event: test() )
#============================================(BUTTONS)================================================

#============================================(INITIAL SETUP)================================================
homeScreen.show()

#============================================(END)================================================
window.mainloop()