
#Angus Goody
#PETER Pupil generator 
#2/04/17

from tkinter import *
import random
from tkinter import font
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import threading
from multiprocessing.dummy import Pool as ThreadPool

window=Tk()
window.title("Pupil Generator")
window.geometry("500x400")



#Names
names=["Billy","Sam","Jack","Ben","James","Daniel","Ethan","Charlie","Jordan"]
#Second
second=["Smith","Turner","Jones","Taylor","Williams","Brown","White"]

grades=["A*","A","B","C","D","E","F"]
noteOptions=["Needs to work harder","Is just brilliant at everything","Needs to run faster",
"Needs to improve their performance","Is just all around bad at PE"]
#Global Vars
mainExportDir=""
mainNumberOfExports=0

#===================================================(INIT FUNCTIONS)===================================================

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
	
	
#===================================================(CLASSES)===================================================

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

class masterFrame(mainFrame):
	"""
	Class for screen that is based off the Frame class
	"""
	screenArray=[]
	lastScreen=None
	def __init__(self,parent):
		#Initialise the instance as a frame as well
		mainFrame.__init__(self,parent)
		screenClass.screenArray.append(self)
	
	def addView(self,frameToAdd):
		masterFrame.screenArray.append(frameToAdd)
		
		
	def show(self,frameToDisplay):
		"""
		This makes sure the current screen isn't reloaded
		"""
		if frameToDisplay != screenClass.lastScreen:
			for item in screenClass.screenArray:
				item.pack_forget()
			frameToDisplay.pack(expand=True, fill=BOTH)
			print("DONE")
			screenClass.lastScreen=self	

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
	def showView(self,screensToDisplay):
		if type(screensToDisplay) is list:
			screens=[]
			for item in screensToDisplay:
				if item in masterControl.viewArray:
					screens.append(item)
			if len(screens) > 0:
				for item in masterControl.viewArray:
					item.pack_forget()
				for item in screens:
					item.pack(expand=True,fill=BOTH)
		else:
			print("Please pass array to method")
	def showViewUnder(self,showScreen):
		if showScreen in masterControl.viewArray:
			showScreen.pack(expand=True,fill=BOTH)
			
class ThreadedClient(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		for x in range(1, 5):
			time.sleep(2)
			self.queue.put(msg)
	
	
def createThread(functionToRun):
	pass	
#===================================================(UI SETUP)===================================================

#==================STATUS==============
#Status bar
statusVar=StringVar()
statusVar.set("Home")

statusBaseFrame=mainFrame(window)
statusBaseFrame.pack(side=BOTTOM,fill=X)
statusBaseFrame.colour("#F951A3")

#Status master control
statusController=masterControl(statusBaseFrame)
statusController.pack(expand=True, fill=BOTH)

#Home Status View
statusMainView=mainFrame(statusController)
Label(statusMainView,textvariable=statusVar,font="Arial 15 bold").pack(expand=True)
statusMainView.colour("#A9F955")

#Loading Status View
statusLoadingView=mainFrame(statusController)
statusProgressBar = ttk.Progressbar(statusLoadingView, orient="horizontal", length=200, mode="determinate")
statusProgressBar.pack(fill=X)
statusLoadingView.colour("#F9AA5E")

#Adding Views to status control
statusController.addView(statusMainView)
statusController.addView(statusLoadingView)

#==================HOME==============

homeScreen=screenClass("Home")
homeDisplay=displayView(homeScreen)
homeDisplay.pack(expand=True,fill=BOTH)

#Choose number of pupils
numberOfPupilsFrame=mainFrame(homeDisplay)
numberOfPupilsFrameSub=mainFrame(numberOfPupilsFrame)
numberOfPupilsFrameSub.pack(expand=True)

Label(numberOfPupilsFrameSub,text="Number of Pupils").pack()
numberOfPupilsEntry=Entry(numberOfPupilsFrameSub,justify=CENTER)
numberOfPupilsEntry.pack()

#Choose Directory
homeChooseDir=mainFrame(homeDisplay)
homeChooseDirSub=mainFrame(homeChooseDir)
homeChooseDirSub.pack(expand=True)

Label(homeChooseDirSub,text="Location").pack()

homeChooseDirEntry=Entry(homeChooseDirSub,state=DISABLED)
homeChooseDirEntry.pack()

homeChooseButton=Button(homeChooseDirSub,text="Browse")
homeChooseButton.pack()

#Export Button
homeExportButtonFrame=mainFrame(homeDisplay)

exportButton=Button(homeExportButtonFrame,text="Export",width=20)
exportButton.pack(expand=True)

#Add Sections
homeDisplay.addSection("#5AB247",numberOfPupilsFrame)
homeDisplay.addSection("#62C14D",homeChooseDir)
homeDisplay.addSection("#78D367",homeExportButtonFrame)
homeDisplay.showSections()

#===================================================(FUNCTIONS)===================================================
def insertEntry(entry,message):
	"""
	This function will add text into entry
	"""
	entry.delete(0,END)
	entry.insert(END,message)

def insertEnryDisabled(entry,message):
	"""
	Function for disabled entries
	"""
	entry.config(state=NORMAL)
	insertEntry(entry, message)
	entry.config(state=DISABLED)
	
def askMessage(pre,message):
	"""
	This function will launch the tkinter
	dialog and ask a question to user
	"""
	try:
		messagebox.showinfo(pre,message)
	except:
		print(message)
	
	
def generate(amount):
	pupils=[]
	fullNames=[]
	lastPercent=-1
	counter=0
	for x in range(amount):
		firstName=random.choice(names)
		secondName=random.choice(second)
		grade=random.choice(grades)
		pbs={"100m":random.randint(10,20),"200m":random.randint(15,30)}
		notes=str(firstName)+" "+random.choice(noteOptions)
		fullName=firstName+" "+secondName
		if fullName not in fullNames:
			fullNames.append(fullName)
			pupilDict={"Name":firstName,"Second":secondName,"Grade":grade,"PB":pbs,"Notes":notes}
			pupils.append(pupilDict)
			counter+=1
			percent=int((x/amount)*100)
			
			if percent != lastPercent:
				print(percent,"%")
				lastPercent=percent
		else:
			print("Prevented duplicate")
	
	print("Created",counter,"pupils")		
	return pupils
	
def mainExport():
	numberOfPupils=numberOfPupilsEntry.get()
	try:
		numberOfPupils=int(numberOfPupils)
	except:
		askMessage("Error","Only numbers please")
	else:
		results=generate(numberOfPupils)
		file=open("generated.txt","w")
		for line in results:
			file.write(str(line))
			file.write("\n")
		file.close()
		askMessage("Complete", "Export complete")
		
	

#===================================================(SETUP)===================================================

homeScreen.show()
statusController.showView([statusMainView])
insertEnryDisabled(homeChooseDirEntry, "Default")
exportButton.config(command=mainExport)
#===================================================(END)===================================================

window.mainloop()