# coding=utf-8

#Angus Goody
#PETER 2.0
#1/04/17

#============================================(IMPORTS)================================================
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import datetime
from tkinter import font
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
mainPassColour="#85EB00"
mainFailColour="#F07A90"
mainUnknownColour="#C7BC27"
viewAllCounterVar=StringVar()
#============================================(GLOBAL ARRAYS)================================================
mainLogArray=[]
passGrades=["A*","A","B","C"]
mainStudentFields=["Name","Second","Age","Grade","PB","Notes"]
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
	This function is very important because python
	only binds functions to one item. This function will
	bind all the children of that item to the same function.
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
	report("Added recursive binding to",parent.winfo_class(),tag="binding",system=True)

def temp(data):
	print(data)

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
			report("Error updating font",self.text,temp,tag="error")
		else:
			report("Successfully updated font",self.text,tag="font")

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
	 so they appear on dark/light background handles bindings and pop up
	 menus
	"""
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.labelViews=[]
		self.colourVar=""

		#Pop up menu
		self.popUpMenu=Menu(self)


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

	#Add a popup menu when right clicking on frame
	def addPopMenu(self,menuDict):
		for item in menuDict:
			self.popUpMenu.add_command(label=item,command=menuDict[item])
		#Bind right click menu to self
		self.addBinding("<Button-2>",lambda event: self.popUpMenu.post(event.x_root, event.y_root))

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

		#Track status bar frames
		self.statusBarList=[]

		#Add a status bar to every screen
		self.statusBottom=mainFrame(self)


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
			report("Loaded screen",self.name,tag="screen",system=True)

	#Add command method
	def addCommand(self,command):
		self.runCommandDict[command]="function"

	#Add a command with lambda
	def addLambdaCommand(self,command):
		self.runCommandDict[command]="command"

	#Run the commands
	def runCommands(self):
		"""
		This method runs certain commands when the screen is loaded. These can
		be setup commands etc
		"""

		if len(self.runCommandDict) > 0:
			for item in self.runCommandDict:
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

	def addStatusScreen(self,frameToAdd):
		report("Adding item to status bar of type",type(frameToAdd),tag="screen",system=True)
		self.statusBarList.append(frameToAdd)

	def showStatusScreen(self,screenToShow):
		if screenToShow in self.statusBarList:
			for screen in self.statusBarList:
				screen.pack_forget()
			screenToShow.pack(side=BOTTOM,fill=X)

class displayView(mainFrame):
	"""
	This is the class for displaying multiple frames
	of data on the screen. The frames are equally spaced
	apart and automatically adjust colour etc
	"""
	labelSections={}
	def __init__(self,parent):
		mainFrame.__init__(self,parent)
		#Tracks all frames
		self.frameArray=[]
		#Tracks just labels
		self.labelDict={}
		#Tracks frames with labels in
		self.labelFrameDict={}

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
		self.labelFrameDict[indentify]=newFrame
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

	def bindAllHover(self,*colour,**keyargs):
		"""
		This method binds the "Enter" command
		to all the labels and changes their colour
		when the mouse enters it
		"""

		#Opposite binds the oposite colour when hovering over label
		if "opposite" in keyargs:
			for label in self.labelDict:
				if keyargs["opposite"] == True:
					labelInstance=self.labelDict[label]
					oppositeCol=getColourForBackground(labelInstance.fg)
					labelInstance.bind("<Enter>",lambda event,
				                                            lab=label,col=oppositeCol,args=keyargs: self.changeLabelColour(lab,col,temp=True))
		elif len(colour) > 0:
			colour=colour[0]
			for label in self.labelDict:
				self.labelDict[label].bind("<Enter>",lambda event,
				                                            lab=label,col=colour,args=keyargs: self.changeLabelColour(lab,col,temp=True))

	def bindAllLeave(self):
		"""
		This method binds the leave
		command to reset the label to 
		the default colour
		"""
		for label in self.labelDict:
			self.labelDict[label].bind("<Leave>",lambda event,lab=label: self.restoreLabelColour(lab))

	def getLabelFrameSection(self, identifier):
		"""
		This method will return the object of the frame
		so it can be used in the main program
		"""
		if identifier in self.labelFrameDict:
			match=self.labelFrameDict[identifier]
			return match
		else:
			print("Please use valid identifier")

	def getLabelObject(self,identifier):
		if identifier in self.labelDict:
			match=self.labelDict[identifier]
			return match
		else:
			print("Use valid identifier")

class masterControl(mainFrame):
	"""
	This class is basically a mini TK window
	inside a frame or section of the program. It can
	itself display diffrent frames.
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

class studentListbox(Listbox):
	def __init__(self,parent,**kwargs):
		Listbox.__init__(self,parent,kwargs)
		self.listData=[]
		self.listDict={}

	def add(self,studentInstance):

		#Get colour for grade
		grade=studentInstance.grade
		if grade in passGrades:
			sectionColour=mainPassColour
		else:
			sectionColour=mainFailColour


		#Get Name and Second

		wholeName=studentInstance.fullName

		#Add to list data
		if studentInstance not in self.listData:
			self.listData.append(studentInstance)

		#Add to listbox
		self.insert(END,wholeName)
		self.itemconfig(END,bg=sectionColour)

		#Add to dictionary
		if wholeName not in self.listDict:
			self.listDict[wholeName]=studentInstance

		#Update label
		amount=len(self.get(0,END))
		viewAllCounterVar.set(str(amount)+" Results")

	def addArray(self,arrayData):
		self.delete(0,END)
		for student in arrayData:
			self.add(student)

	def clear(self):
		self.listDict={}
		self.listData=[]
	def getData(self):
		return self.listData

#====================LOG SCREEN====================

#region logscreen
logScreen=screenClass("Logs")

columnArray=["Message","Time"]
allColumnArray=["Message","Time"]

#Log screen notebook View

logScreenNotebook=ttk.Notebook(logScreen)
logScreenNotebook.pack(expand=True,fill=BOTH)

#Display log normal view
logTree=ttk.Treeview(logScreenNotebook,columns=allColumnArray,show="headings")
logTree.pack(fill="both",expand=True)

logTreeScroll=Scrollbar(logTree)
logTreeScroll.pack(side=RIGHT,fill=Y)

logTreeScroll.config(command=logTree.yview)
logTree.config(yscrollcommand=logTreeScroll.set)

logTree.column("Message",width=10,minwidth=45)
logTree.column("Time",width=5,minwidth=20)

logTree.heading("Message",text="Message")
logTree.heading("Time",text="Time")

#Log Tree system events view
logSystemTree=ttk.Treeview(logScreenNotebook,columns=allColumnArray,show="headings")
logSystemTree.pack(fill="both",expand=True)

logSystemTreeScroll=Scrollbar(logSystemTree)
logSystemTreeScroll.pack(side=RIGHT,fill=Y)

logSystemTreeScroll.config(command=logSystemTree.yview)
logSystemTree.config(yscrollcommand=logSystemTreeScroll.set)

logSystemTree.column("Message",width=10,minwidth=45)
logSystemTree.column("Time",width=5,minwidth=20)

logSystemTree.heading("Message",text="Message")
logSystemTree.heading("Time",text="Time")

#Add notebook pages
logScreenNotebook.add(logTree,text="Normal")
logScreenNotebook.add(logSystemTree,text="System")

#Add Tree View tags here
logTreeTagDict={"font":"#B1FF5E",
                "screen":"#9195FF",
                "file":"#E37DB8",
                "error":"#E36265",
                "warning":"#E3B521",
                "binding":"#F4FF2B",
                "system":"#FFCCD0",
                "student":"#4AC7C4"}

for tag in logTreeTagDict:
	logTree.tag_configure(tag,background=logTreeTagDict[tag])
	logSystemTree.tag_configure(tag,background=logTreeTagDict[tag])


#endregion

#============================================(PRE FUNCTIONS)================================================


#==============LOG FUNCTIONS================
def report(message,*extra,**keywords):

	tag=""
	system=False

	#Check for extra info
	if len(extra) > 0:
		#Concatonate variables
		for item in extra:
			message+=" "
			message+=str(item)

	#Check for tags and system data
	for item in keywords:
		if item == "tag":
			tag=keywords[item]
		elif item == "system":
			systemValue=keywords[item]
			if systemValue:
				system=True


	#Gets current time and date
	currentTime=datetime.datetime.now().time()
	temp=[message,currentTime]

	#If the data is system data put it in separate tree
	if system:
		logSystemTree.insert("" , 0,values=(message,currentTime),tags=tag)
	else:
		#Makes sure logArray isn't filled up
		if len(mainLogArray) < maxLogSize:
			mainLogArray.append(temp)
		else:
			print("Log array filled up")
		logTree.insert("" , 0,values=(message,currentTime),tags=tag)

#==============FILE FUNCTIONS================
def getContent(fileName,**kwargs):

	#CHeck if duplicates should be prevented or not
	#By default duplicates will be prevented
	duplicates=False
	if "duplicates" in kwargs:
		if kwargs["duplicates"] == True:
			duplicates=True

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
				if duplicates == False:
					if line not in newContent:
						newContent.append(line)
					else:
						report("Prevented duplicate from file",system=True,tag="file")

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
	#todo this is not working
	"""
	This function returns a hex value 
	that is opposite the parameter value
	in the colour spectrum
	"""
	hexValue = hexValue.replace("#", "")
	print(hexValue)
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
	studentNames=[]
	def __init__(self,name,second):
		self.name=name
		self.second=second
		self.fullName=self.name+" "+self.second
		self.age=0
		self.grade="C"
		self.notes="No notes"
		self.pb={"100m":0,"200m":0}

		#Add instance to array
		studentClass.studentArray.append(self)
		studentClass.studentNames.append(self.fullName)

	def addAge(self,ageToAdd):
		self.age=ageToAdd
	def addGrade(self,gradeToAdd):
		self.grade=gradeToAdd
	def addNotes(self,notes):
		self.notes=notes
	def addPb(self,pbDict):
		self.pb=pbDict
	def getInfo(self):
		return {"Name":self.name,
		        "Full":self.fullName,
		           "Second":self.second,
		           "Age":self.age,
		           "Grade":self.grade,
		           "PB":self.pb,
		           "Notes":self.notes}

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

#-------------STATUS SUB VIEWS-----------


#Actual Status View
statusMainView=mainFrame(statusController)
mainStatusLabel=mainLabel(statusMainView,textvariable=statusVar,font="Arial 15 bold")
mainStatusLabel.pack(expand=True)
statusMainView.colour("#577EEB")

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

homeDisplayScreen.addLabelSection("Welcome","#E2698B","Welcome")
homeWelcomeLabel=homeDisplayScreen.getLabelObject("Welcome")
homeWelcomeLabel.changeFontSize(25)
homeDisplayScreen.addLabelSection("All Pupils","#C75D7C","Total")
homeDisplayScreen.addLabelSection("A-C Pupils","#AA4F69","Pass")
homeDisplayScreen.addLabelSection("D-F Pupils","#8F4359","Fail")

homeDisplayScreen.showSections()

#endregion
#====================View All SCREEN================
#region viewall
viewAllScreen=screenClass("View All")

#-------Search Bar-------

viewAllSearchFrame=mainFrame(viewAllScreen)
viewAllSearchFrame.pack(side=TOP,fill=X,pady=5)

viewAllSearchSubFrame=mainFrame(viewAllSearchFrame)
viewAllSearchSubFrame.pack(expand=True)

viewAllSearchSubEntryFrame=mainFrame(viewAllSearchSubFrame)
viewAllSearchSubEntryFrame.pack(side=LEFT)

#Label
viewAllSearchLabel=mainLabel(viewAllSearchSubEntryFrame,text="Search")
viewAllSearchLabel.pack(side=LEFT)

#Entry
viewAllSearchEntry=Entry(viewAllSearchSubEntryFrame,width=30)
viewAllSearchEntry.pack(side=RIGHT)

#Clear button
viewAllClearButton=Button(viewAllSearchSubFrame,text="Clear")
viewAllClearButton.pack(side=RIGHT,padx=5)

#Counter Label

viewAllCounterFrame=mainFrame(viewAllScreen)
viewAllCounterFrame.pack(fill=X)

viewAllCounterLabel=mainLabel(viewAllCounterFrame,textvariable=viewAllCounterVar)
viewAllCounterLabel.pack(expand=True)

#-------Listbox--------
viewAllListboxFrame=mainFrame(viewAllScreen)
viewAllListboxFrame.pack(expand=True,fill=BOTH)

viewAllListbox=studentListbox(viewAllListboxFrame,font=font.Font(size=19))
viewAllListbox.pack(expand=True,fill=BOTH)

viewAllListboxScrollBar=Scrollbar(viewAllListbox)
viewAllListboxScrollBar.pack(side=RIGHT,fill=Y)

viewAllListboxScrollBar.config(command=viewAllListbox.yview)
viewAllListbox.config(yscrollcommand=viewAllListboxScrollBar.set)

#-------Filter and sort options-------
viewAllOptionFrame=mainFrame(viewAllScreen)
viewAllOptionFrame.pack(fill=BOTH,pady=10)

viewAllOptionSubFrame=mainFrame(viewAllOptionFrame)
viewAllOptionSubFrame.pack(expand=True)

#Filter
viewAllFilterFrame=mainFrame(viewAllOptionSubFrame)
viewAllFilterFrame.pack(side=LEFT)

viewAllFilterVar=StringVar()
viewAllFilterVar.set("All")

viewALlFilterOptions=["All"]+mainStudentFields

mainLabel(viewAllFilterFrame,text="Filter by").pack()

#endregion
#====================Log Screen Extra================
#region logextra
logScreenStatus=mainFrame(logScreen)
logScreenStatusSub=mainFrame(logScreenStatus)
logScreenStatusSub.pack(expand=True)

for item in logTreeTagDict:
	mainLabel(logScreenStatusSub,text=item,bg=logTreeTagDict[item]).pack(fill=X,side=LEFT)
#endregion
#====================View student screen================
viewStudentScreen=screenClass("Showing Student")

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

def subSearch(target,dataToSearch):
	"""
	This function is the actual search
	function and will recursivley search and return
	True or False
	"""
	#Setup
	target=str(target)
	target=target.upper()

	#print("Searching for",target,"in",dataToSearch,"of type",type(dataToSearch))
	#Iterate through all data
	for item in dataToSearch:
		#Get data type
		try:
			dataType=type(item)
		except:
			report("Error converting data type to search",tag="error",system=True)
		else:

			#If data is number or float
			if dataType == int or dataType == float:
				item=str(item)
				dataType=type(item)

			#If data is simple string
			if dataType == str:
				if target in item.upper():
					return True
			#If data is list
			elif dataType == list:
				for section in item:
					if subSearch(target,[section]):
						return True
			#If data is dictionary
			elif dataType == dict:
				for section in item:
					dataInSection=item[section]
					if subSearch(target,[dataInSection]):
						return True
			#If data is a student class
			elif dataType == studentClass:
				data=item.getInfo()
				if subSearch(target,data):
					return True

	return False

def mainSearch(target,section,dataToSearch):
	validSections=["All","Name","Second","Age","Grade","PB","Notes"]
	if section in validSections:
		resultArray=[]
		for student in dataToSearch:
			#The all section
			if section == "All":
				sectionToSearch=[student.getInfo()]
			#This must be square brackets because otherwise strings will be sliced
			else:
				sectionToSearch=[student.getInfo()[section]]


			#Actual Search part
			if subSearch(target,sectionToSearch):
				resultArray.append(student)

		#Finished checking
		return resultArray


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
	"""
	This function will create the student objects
	from the content of the txt file
	"""
	#todo fix this function

	#Track number of students
	studentCounter=0

	#ValidData
	validData={"Age":"addAge","Grade":"addGrade","Notes":"addNotes","PB":"addPb"}

	#Loop through data
	for line in fileContent:
		try:
			studentDict=eval(line)
		except:
			report("Error evaluating file content",tag="student")
		else:
			try:
				fullName=str(studentDict["Name"])+" "+studentDict["Second"]
			except:
				pass
			else:
				if fullName not in studentClass.studentNames:
					if type(studentDict) == dict:
						try:
							studentInstance=studentClass(studentDict["Name"],studentDict["Second"])
						except:
							report("Could not find basic student info",tag="student")
						else:
							#Add the rest of the data here
							for item in studentDict:
								if item != "Name" and item != "Second":
									if item in validData:
										match=validData[item]
										try:
											getattr(studentInstance,match)(studentDict[item])
										except:
											report("Attribute error",tag="system")
										else:
											report("Added student attribute",studentDict["Name"],item,tag="student",system=True)

							studentCounter+=1
							report("Added student",studentDict["Name"],tag="student")
				else:
					report("Prevented full name duplicate",tag="student",system=True)

def viewAllSearch():
	section=viewAllFilterVar.get()
	target=viewAllSearchEntry.get()
	dataToSearch=viewAllListbox.getData()
	results=mainSearch(target,section,dataToSearch)
	viewAllListbox.addArray(results)
def clearButtonCommand(entry,searchCommand):
	insertEntry(entry,"")
	searchCommand()
#============================================(MENU?/CASCADES)================================================

mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="Students",menu=studentMenu)
mainMenu.add_cascade(label="Help",menu=helpMenu)

#============CASCADES==========

#File Menu
fileMenu.add_command(label="Home",command=lambda: homeScreen.show())

#Edit Menu

#Student menu
studentMenu.add_command(label="View All",command=lambda: viewAllScreen.show())
#Help Menu
helpMenu.add_command(label="Show Log",command=lambda :logScreen.show())

#============================================(BINDINGS)================================================

#Status Bar
statusController.addBinding("<Double-Button-1>",lambda event: homeScreen.show())

mainStatusLabel.bind("<Enter>",lambda event: showHomeMessage("Enter"))
mainStatusLabel.bind("<Leave>",lambda event: showHomeMessage("Leave"))

#Home screen
homeDisplayScreen.bindAllHover(opposite=True)
homeDisplayScreen.bindAllLeave()

#View all screen
viewAllSearchEntry.bind("<KeyRelease>",lambda event: viewAllSearch())
#============================================(SCREEN COMMANDS)================================================

#==========================================(OPTION MENUS)=================================

#View all screen
viewAllFilterOptionMenu=OptionMenu(viewAllFilterFrame,viewAllFilterVar,*viewALlFilterOptions,
                                   command=lambda event: viewAllSearch())
viewAllFilterOptionMenu.config(width=12)
viewAllFilterOptionMenu.pack()
#============================================(BUTTONS)================================================

#View all screen
viewAllClearButton.config(command=lambda: clearButtonCommand(viewAllSearchEntry,viewAllSearch))

#============================================(INITIAL SETUP)================================================

#Screen to show on startup
viewAllScreen.show( )
#Status view to show on startup
statusController.showView(statusMainView)
#Get the students from file
students=getContent("pupils.txt")
#Create the student objects from the file
createStudents(students)

#Display the log screen key on log screen
logScreen.addStatusScreen(logScreenStatus)
logScreen.showStatusScreen(logScreenStatus)
#Add the initial students to the view all listbox
viewAllListbox.addArray(studentClass.studentArray)
#============================================(TESTING AREA)================================================


#============================================(END)================================================
window.mainloop()