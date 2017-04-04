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
					parent.changeColour(getColourForBackground(colour))

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

class mainLabel(Label):
	"""
	This is a class that modifies
	the label class to give more control
	over customizing the label
	"""
	labelArray=[]

	#Initialise
	def __init__(self,parent,**keyArgs):
		Label.__init__(self,parent,keyArgs)
		#Setup
		self.text=""
		self.fontString=""
		self.fg="#000000"
		#If certain parameters are passed
		if "text" in keyArgs:
			self.text=keyArgs["text"]

		if "font" in keyArgs:
			self.fontString=keyArgs["font"]

		if "bg" in keyArgs:
			try:
				self.fg=getColourForBackground(keyArgs["bg"])
				self.config(fg=self.fg)
			except:
				report("Error changing label fg",keyArgs["bg"],tag="error")

		#Configure default font
		self.fontSize=14
		self.fontFamily="TkDefaultFont"
		self.strength=""
		self.getDefaultFont()

		#Add label to array
		mainLabel.labelArray.append(self)

	#Class method only
	def getDefaultFont(self):
		words=self.fontString.split()
		if len(words) > 0:
			counter=0
			for f in words:
				counter+=1
				if counter == 1:
					self.fontFamily=f
				elif counter == 2:
					self.fontSize=f
				elif counter == 3:
					self.strength=f

	#Class method only
	def updateFont(self):
		temp=""
		temp+=self.fontFamily
		temp+=" "
		temp+=str(self.fontSize)
		temp+=" "
		temp+=self.strength
		try:
			self.config(font=temp)
		except:
			report("Error updating font",temp,tag="error")
		else:
			report("Successfully updated font",tag="font")

	def changeFontSize(self,size):
		self.fontSize=size
		self.updateFont()

	def changeFontName(self,fontFamilyPar):
		self.fontFamily=fontFamilyPar
		self.updateFont()

	def strength(self, boldOrNormal):
		if boldOrNormal == "Bold" or boldOrNormal == "Normal":
			if boldOrNormal == "Bold":
				self.strength="bold"
			else:
				self.strength=""
			self.updateFont()
		else:
			report("Invalid font bold option")

	def changeColour(self,colour,**keyargs):
		"""
		This method changes the fg of
		 the label and if temp is passed as
		 true it will not update the labels fg 
		 value so it remembers the old one
		"""
		if "temp" in keyargs:
			if keyargs["temp"]:
				self.config(fg=colour)
			else:
				self.config(fg=colour)
				self.fg=colour
		else:
			self.config(fg=colour)
			self.fg=colour





	def restoreColour(self):
		self.config(fg=self.fg)

class mainFrame(Frame):
	"""
	This is a modified frame class which 
	can be modified for every frame on screen. It 
	automatically changes colours and updates text colours
	 so they appear on dark/light background
	"""
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.labelViews=[]
		self.colourVar=""

	#Update colour method
	def colour(self,chosenColour):

		#Get FG colour for selected colour
		fgColour=getColourForBackground(chosenColour)

		self.colourVar=chosenColour

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
	currentName=""
	currentScreen=""
	def __init__(self,name):
		#Initialise the instance as a frame as well
		mainFrame.__init__(self,window)
		self.name=name
		screenClass.screenArray.append(self)
		self.runCommandDict={}

	#Show screen method
	def show(self):
		if self != screenClass.lastScreen:
			for item in screenClass.screenArray:
				item.pack_forget()
			self.pack(expand=True, fill=BOTH)
			statusVar.set(self.name)
			screenClass.currentName=self.name
			screenClass.currentScreen=self
			screenClass.lastScreen=self

			#Run screen commands
			self.runCommands()
			report("Loaded screen",self.name,tag="screen")

	def addCommand(self,command):
		self.runCommandDict[command]="function"

	def addLambdaCommand(self,command):
		self.runCommandDict[command]="command"


	def runCommands(self):
		"""
		This method runs certain commands when the screen is loaded. These can
		be setup commands etc
		"""
		if len(self.runCommandDict) > 0:
			for item in self.runCommandDict:
				print(self.runCommandDict)
				if self.runCommandDict[item] == "function":
					try:
						item()
					except:
						report("Error executing screen function",tag="error")
				else:
					item()
					try:
						item()
					except:
						report("Error executing lambda screen function",tag="error")

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
		self.labelDict={}

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
		newFrameLabel=mainLabel(newFrame,text=text)
		newFrameLabel.changeFontSize(16)
		newFrameLabel.pack(expand=True)
		self.labelDict[indentify]=newFrameLabel

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

	def changeLabelColour(self,identifier,colour,**keyargs):
		if identifier in self.labelDict:
			instance=self.labelDict[identifier]
			if "temp" in keyargs:
				if keyargs["temp"] == True:
 					instance.changeColour(colour,temp=True)
				else:
					instance.changeColour(colour)
			else:
				instance.changeColour(colour)

	def restoreLabelColour(self,identifier):
		if identifier in self.labelDict:
			instance=self.labelDict[identifier]
			instance.restoreColour()

class masterControl(mainFrame):
	"""
	This frame is used to control different
	views that can be changed.
	"""
	viewArray=[]
	def __init__(self,parent):
		mainFrame.__init__(self,parent)

	def addView(self,frameToDisplay):
		masterControl.viewArray.append(frameToDisplay)

	def showView(self,screenToDisplay):
		"""
		This method will show a screen on the master
		"""
		if screenToDisplay in masterControl.viewArray:
			for item in masterControl.viewArray:
				item.pack_forget()
			screenToDisplay.pack(expand=True,fill=BOTH)

	def showMultipleViews(self,viewsToDisplay):
		"""
		This method will display multiple frames
		on top of each other
		"""
		validScreens=[]
		#Filters valid screens
		for screen in viewsToDisplay:
			if screen in masterControl.viewArray:
				validScreens.append(screen)
		#Hide all other screens
		for screen in masterControl.viewArray:
			screen.pack_forget()
		#Show the screens
		for screen in validScreens:
			screen.pack(expand=True,fill=BOTH)

	def showViewUnder(self,frameToPack):
		"""
		Method will pack a frame ontop of current frames
		"""
		if frameToPack in masterControl.viewArray:
			frameToPack.pack(expand=True,fill=BOTH)

	def showViewTop(self,frameToPack):
		if frameToPack in masterControl.viewArray:
			frameToPack.pack(expand=True,fill=BOTH,side=TOP)

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

#Add Tree View tags here
logTreeTagDict={"font":"#8990E3",
                "screen":"#8EE3DF",
                "file":"#E37DB8",
                "error":"#E36265",
                "warning":"#E3B521"}

for tag in logTreeTagDict:
	logTree.tag_configure(tag,background=logTreeTagDict[tag])


#endregion

#============================================(PRE FUNCTIONS)================================================


#==============LOG FUNCTIONS================
def report(message,*extra,**keywords):

	tag=""
	#Check for extra info
	if len(extra) > 0:
		#Concatonate variables
		for item in extra:
			message+=" "
			message+=str(item)

	#Check for tags
	if len(keywords) > 0:
		if "tag" in keywords:
			tag=keywords["tag"]

	currentTime=datetime.datetime.now().time()
	temp=[message,currentTime]

	#Makes sure logArray isn't filled up
	if len(mainLogArray) < maxLogSize:
		mainLogArray.append(temp)
	else:
		print("Log array filled up")
	logTree.insert("" , 0,values=(message,currentTime),tags=(tag))

#==============FILE FUNCTIONS================
def getContent(fileName):
	try:
		file=open(fileName)
	except:
		report("Error opening file",fileName,tag="error")
	else:
		content=file.readlines()

		#Filter content
		newContent=[]
		for line in content:
			words=line.split()
			#Removes empty lines
			if len(words) > 0:
				line=line.rstrip()
				newContent.append(line)

		report("Got content from file",fileName,tag="file")
		return newContent


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

def getOppositeHexValue(hexValue):
	"""
	This function returns a hex value 
	that is opposite the parameter value
	in the colour spectrum
	"""
	hexValue = hexValue.replace("#", "")
	binaryValue=str(bin(int(hexValue, 16))[2:])

	#Twos Compliment to get opposite
	binaryStep=binaryValue.replace("1","?")
	binaryStep=binaryStep.replace("0","1")
	binaryStep=binaryStep.replace("?","0")
	numberValue=int(binaryStep,2)
	numberValue+=1
	finalValue=convertHex(numberValue,"Hex")
	print(finalValue)
#============================================(CLASSES)================================================

class studentClass:
	"""
	Class for keeping students
	"""
	studentArray=[]
	def __init__(self,name,second,age,grade):
		self.name=name
		self.second=second
		self.age=age
		self.grade=grade
		self.dict={"Name":self.name,
		           "Second":self.second,
		           "Age":self.age,
		           "Grade":self.grade}

		#Add instance to array
		studentClass.studentArray.append(self)




#============================================(MAIN UI SETUP)================================================

#====================STATUS BAR====================
#region statusbar
statusVar=StringVar()
statusVar.set("")

statusBaseFrame=mainFrame(window)
statusBaseFrame.pack(side=BOTTOM,fill=X)
statusBaseFrame.colour("#F951A3")

#Status master control
statusController=masterControl(statusBaseFrame)
statusController.pack(expand=True, fill=BOTH)

#=================STATUS SUB VIEWS============


#Actual Status View
statusMainView=mainFrame(statusController)
mainStatusLabel=mainLabel(statusMainView,textvariable=statusVar,font="Arial 15 bold")
mainStatusLabel.pack(expand=True)
statusMainView.colour("#A9F955")

#Status Loading View
statusLoadingView=mainFrame(statusController)
statusLoading=ttk.Progressbar(statusLoadingView, orient="horizontal", length=200, mode="determinate")
statusLoading.pack(fill=X)
statusLoadingView.colour("#A9F955")


#Adding Views to status control
statusController.addView(statusMainView)
statusController.addView(statusLoadingView)
#endregion
#====================HOME SCREEN====================
#region homescreen
homeScreen=screenClass("Home")

homeDisplayScreen=displayView(homeScreen)
homeDisplayScreen.pack(expand=True,fill=BOTH)

#Section setup

homeDisplayScreen.addLabelSection("Welcome","#2F9679","Welcome")
homeDisplayScreen.addLabelSection("Total Pupils","#1EC5B0","Total")
homeDisplayScreen.addLabelSection("A-C Pupils","#21D6BF","Pass")
homeDisplayScreen.addLabelSection("D-F Pupils","#24ECD3","Fail")

homeDisplayScreen.showSections()

#endregion
#====================View All SCREEN================
viewAllScreen=screenClass("View All")
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
def showHomeMessage(enterOrLeave):
	"""
	This function will display a message on the 
	status bar when the mouse enters the bar
	"""
	if enterOrLeave == "Enter":
		if screenClass.currentScreen != homeScreen:
			statusVar.set("Double click to go home")
	else:
		if screenClass.currentScreen != homeScreen:
			statusVar.set(screenClass.currentName)

def updateGlobalFont(font):
	for label in mainLabel.labelArray:
			label.changeFontName(font)
	report("Updated global font to",font,tag="font")

def createStudents(fileContent):
	validItems=["Name","Second","Age","Grade","PB","Notes"]
	studentCounter=0
	#Makes sure maximum of 500 students are loaded
	for line in fileContent:
		if len(line) > 0:
			try:
				studentDict=eval(line)
			except:
				report("Error evaluating string in setup",tag="error")
			else:

				#Must get basic info to create instance
				try:
					studentName=studentDict["Name"]
					studentSecond=studentDict["Second"]
				except:
					report("Error getting basic student info",tag="warning")
				else:
					#Try and get the rest of the data
					collectedData=[]
					for section in studentDict:
						print(section)





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
statusController.addBinding("<Double-Button-1>",lambda event: homeScreen.show())

statusMainView.addBinding("<Enter>",lambda event: showHomeMessage("Enter"))
statusMainView.addBinding("<Leave>",lambda event: showHomeMessage("Leave"))

#Home screen
homeDisplayScreen.addLabelCommand("Welcome","<Enter>",lambda event: homeDisplayScreen.changeLabelColour("Welcome",
                                  getOppositeHexValue(homeDisplayScreen.colourVar),temp=True))
homeDisplayScreen.addLabelCommand("Welcome","<Leave>",lambda event: homeDisplayScreen.restoreLabelColour("Welcome"))

#============================================(SCREEN COMMANDS)================================================



#============================================(BUTTONS)================================================


#============================================(INITIAL SETUP)================================================
homeScreen.show()
statusController.showView(statusMainView)

students=getContent("pupils.txt")
createStudents(students)

getOppositeHexValue("#000000")
#============================================(END)================================================
window.mainloop()