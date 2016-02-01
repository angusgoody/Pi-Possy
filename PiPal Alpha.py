__author__ = 'Angus'

#Angus Goody
#8/10/15

#PETER Version 1.0


#Main colour variable for if userName file is not found
defaultColour="cyan"

#Imports-------

from tkinter import *
import datetime
from tkinter import colorchooser
import platform
import tkinter.filedialog
import random
from tkinter import filedialog


version=platform.system()
print("System platform is",version)
if version == "Darwin":
    print("Not all Features are supported on MAC")
#Sets up window---------
window=Tk()
window.geometry("450x350")
window.title("PETER")


#Staus bar
statusVar=StringVar()
status=Label(window,text="Status",bg=defaultColour,textvariable = statusVar)
status.pack(side=BOTTOM,fill=X)

#Main variables=================
mainButtonColour="light green"

userName=""
encryptionKey=8
mainEntryTextColour="black"
mainLabelTextColour="black"
numberOfTextItems=4 #The variable for how many items are contained for each pupil in the text file
mainPupilName="pupils.txt"
mainUserName="userName.txt"
currentViewPupil=[]
currentCreatePupil=[]
currentViewCanvas=StringVar()
currentViewCanvasArray=[]

#Toolbars====================
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub menus==================
fileMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)
pupilMenu=Menu(mainMenu)
filterMenu=Menu(mainMenu)
editMenu=Menu(mainMenu)

subPupilMenu=Menu(pupilMenu)
#===================================================================CANVAS'=======================


#Open canvas-------------------------------------------
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)
statusVar.set("Home")
userVar=StringVar()

openLabel=Label(openCanvas,textvariable=userVar,font= "Helvetica 16 bold")
openLabel.pack()

viewNumberFrame=Frame(openCanvas)
viewNumberFrame.pack(pady=10)

numberVar=StringVar()
numberVar.set("0")
Label(viewNumberFrame,text="Number of pupils:").grid(row=0,column=0)
Label(viewNumberFrame,textvariable=numberVar).grid(row=0,column=1)





#Change user canvas----------------------------------------------
changeUserNameCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(changeUserNameCanvas,text="Username:").grid(row=0,column=0)

changeUserNameEntry=Entry(changeUserNameCanvas,font = "Helvetica 12 bold", justify="center")
changeUserNameEntry.grid(row=0,column=1,pady=7)

overwriteArray=[]
currentViewPupil=[]
colourArray = [
'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
'indian red', 'saddle brown', 'sandy brown',
'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
'pale violet red', 'maroon', 'medium violet red', 'violet red',
'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
'thistle', 'snow2', 'snow3',
'snow4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
'purple1', 'purple2', 'purple3', 'purple4',window.cget("bg")]

#Change Theme canvas-----------------------------------------------
changeThemeCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)


colourPicked=StringVar()
colourPicked.set(defaultColour)

colourListBox=Listbox(changeThemeCanvas)
colourListBox.pack(side=LEFT)

#Slider for listbox
colourSlider=Scrollbar(changeThemeCanvas)
colourSlider.pack(side=LEFT,fill=Y)

colourSlider.config(command=colourListBox.yview)
colourListBox.config(yscrollcommand=colourSlider.set)


duplicateTestingArray=[]
for name in colourArray:
    if name not in duplicateTestingArray:
        try:
            colourListBox.insert(END,name)
            colourListBox.itemconfig(END, bg=name)

        except:
            print("Found error in colour array 1")
        else:
            duplicateTestingArray.append(name)

#Change Background canvas------------------------------------------
changeBackgroundCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

backgroundListBox=Listbox(changeBackgroundCanvas)
backgroundListBox.pack(side=LEFT)

#Slider for listbox
backgroundSlider=Scrollbar(changeBackgroundCanvas)
backgroundSlider.pack(side=LEFT,fill=Y)

backgroundSlider.config(command=backgroundListBox.yview)
backgroundListBox.config(yscrollcommand=backgroundSlider.set)

for colour in duplicateTestingArray:
    try:
        backgroundListBox.insert(END,colour)
        backgroundListBox.itemconfig(END,bg=colour)
    except:
        print("Error in colour array")

#Canvas for viewing pupils-----------------------------------------------
viewPupilCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(viewPupilCanvas,text="First Name:").grid(row=0,column=0)
Label(viewPupilCanvas,text="Second Name:").grid(row=1,column=0)
Label(viewPupilCanvas,text="Grade").grid(row=2,column=0)
Label(viewPupilCanvas,text="Personal Best:").grid(row=3,column=0)

displayPersonalBestVar=StringVar()
displayPersonalBest=Label(viewPupilCanvas,textvariable=displayPersonalBestVar)
displayPersonalBest.grid(row=4,column=0)

Label(viewPupilCanvas,text="Notes:").grid(row=5,column=0)


showPupilName=Entry(viewPupilCanvas)
showPupilName.grid(row=0,column=1,pady=2)

showPupilSecond=Entry(viewPupilCanvas)
showPupilSecond.grid(row=1,column=1,pady=2)

showPupilGrade=Entry(viewPupilCanvas)
showPupilGrade.grid(row=2,column=1,pady=2)

chosenPeronalBestToView=StringVar()
chosenPeronalBestToView.set("Select PB")

if version == "Windows":
    showPupilNotes=Text(viewPupilCanvas,height=5,width=15,wrap=WORD,font=("Helvetica", "11"))

else:
    if version == "Darwin":
        showPupilNotes=Text(viewPupilCanvas,font=("Helvetica", "12"),height=5,width=24,wrap=WORD)
    if version == "Linux":
        showPupilNotes=Text(viewPupilCanvas,font=("Helvetica", "12"),height=5,width=18,wrap=WORD)



viewPersonalBestEntry=Entry(viewPupilCanvas,state=DISABLED)
viewPersonalBestEntry.grid(row=4,column=1)


showPupilNotes.grid(row=5,column=1,pady=2)
#Canvas for viewing all pupils-----------------------------------
viewAllCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

mainViewAllFrame=Frame(viewAllCanvas)
mainViewAllFrame.pack(side=LEFT,fill=Y,padx=9)

secondViewAllFrame=Frame(viewAllCanvas)
secondViewAllFrame.pack(side=RIGHT,fill=Y)

#Second Frame
Label(secondViewAllFrame,text="Preview").grid(row=0,column=1,pady=15)

Label(secondViewAllFrame,text="Name").grid(row=1,column=0)
Label(secondViewAllFrame,text="Second").grid(row=2,column=0)
Label(secondViewAllFrame,text="Grade").grid(row=3,column=0)

previewName=Entry(secondViewAllFrame)
previewName.grid(row=1,column=1)

previewSecond=Entry(secondViewAllFrame)
previewSecond.grid(row=2,column=1)

previewGrade=Entry(secondViewAllFrame)
previewGrade.grid(row=3,column=1)


#Main Frame
bottomViewAllFrame=Frame(mainViewAllFrame)
bottomViewAllFrame.pack(side=BOTTOM,pady=4)

viewAllListbox=Listbox(mainViewAllFrame,width=25)
viewAllListbox.pack(side=LEFT)

viewAllSlider=Scrollbar(mainViewAllFrame)
viewAllSlider.pack(side=LEFT,fill=Y)

viewAllSlider.config(command=viewAllListbox.yview)
viewAllListbox.config(yscrollcommand=viewAllSlider.set)

pupilOptions=["Grade","A-Z (First name)","A-Z (Second name)"]
optionVar=StringVar()


#Canvas for creating new pupil--------------------------------------

createPupilCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(createPupilCanvas,text="First Name:").grid(row=0,column=0)
Label(createPupilCanvas,text="Second Name:").grid(row=1,column=0)
Label(createPupilCanvas,text="Grade").grid(row=2,column=0)
Label(createPupilCanvas,text="Personal Best:").grid(row=4,column=0)
Label(createPupilCanvas,text="Notes:").grid(row=5,column=0)

createPupilName=Entry(createPupilCanvas)
createPupilName.grid(row=0,column=1,pady=2)

createPupilSecond=Entry(createPupilCanvas)
createPupilSecond.grid(row=1,column=1,pady=2)

createPupilGrade=Entry(createPupilCanvas)
createPupilGrade.grid(row=2,column=1,pady=2)

createPupilTarget=Entry(createPupilCanvas)
createPupilTarget.grid(row=4,column=1,pady=2)



if version == "Windows":
    createPupilNotes=Text(createPupilCanvas,height=5,width=15,wrap=WORD,font=("Helvetica","11"))

else:
    if version == "Linux":
        createPupilNotes=Text(createPupilCanvas,font=("Helvetica", "12"),height=5,width=18,wrap=WORD)
    else:
        createPupilNotes=Text(createPupilCanvas,font=("Helvetica", "12"),height=5,width=24,wrap=WORD)

createPupilNotes.grid(row=5,column=1,pady=2)

#Canvas for filtering pupils-------------------------------------------------------
filterPupilCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(filterPupilCanvas,text="Field:").grid(row=0,column=0)
Label(filterPupilCanvas,text="Search:").grid(row=1,column=0,pady=5)
Label(filterPupilCanvas,text="Results:").grid(row=3,column=0,pady=5)

numberOfFilterResults=StringVar()
Label(filterPupilCanvas,textvariable=numberOfFilterResults).grid(row=4,column=1,pady=5)

filterVariable=StringVar()

filterPupilOption=OptionMenu(filterPupilCanvas,filterVariable,"All","First Name","Second Name","Grade","Personal Best")
filterPupilOption.grid(row=0,column=1,pady=5)
filterVariable.set("All")

filterPupilEntry=Entry(filterPupilCanvas)
filterPupilEntry.grid(row=1,column=1,padx=4)



filterFrame=Frame(filterPupilCanvas)
filterFrame.grid(row=3,column=1)

filterResults=Listbox(filterFrame)
filterResults.pack(side=LEFT)

filterResultsScroll=Scrollbar(filterFrame)
filterResultsScroll.pack(side=LEFT,fill=Y)

filterResultsScroll.config(command=filterResults.yview)
filterResults.config(yscrollcommand=filterResultsScroll.set)

#Canvas for bulk edit =======================

bulkEditCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)


#==================================LEFT FRAME==================


#Frame for Listboxes================

mainListboxFrame=Frame(bulkEditCanvas)
mainListboxFrame.pack(side=LEFT,padx=5)



#===========LEFT SUB FRAME============
viewAllBulkFrame=Frame(mainListboxFrame)
viewAllBulkFrame.pack(side=LEFT)

bulkAllPupilListbox=Listbox(viewAllBulkFrame,width=16)
bulkAllPupilListbox.pack(side=LEFT)

bulkViewAllSlider=Scrollbar(viewAllBulkFrame)
bulkViewAllSlider.pack(side=RIGHT,fill=Y)

bulkViewAllSlider.config(command=bulkAllPupilListbox.yview)
bulkAllPupilListbox.config(yscrollcommand=bulkViewAllSlider.set)




#===========RIGHT SUB FRAME============

viewFilterBulkFrame=Frame(mainListboxFrame)
viewFilterBulkFrame.pack(side=RIGHT)

bulkFilterPupilListbox=Listbox(viewFilterBulkFrame,width=16)
bulkFilterPupilListbox.pack(side=LEFT)

bulkFilterSlider=Scrollbar(viewFilterBulkFrame)
bulkFilterSlider.pack(side=RIGHT,fill=Y)

bulkFilterSlider.config(command=bulkFilterPupilListbox.yview)
bulkFilterPupilListbox.config(yscrollcommand=bulkFilterSlider.set)

#==================================RIGHT FRAME==================
secondBulkFrame=Frame(bulkEditCanvas)
secondBulkFrame.pack(side=RIGHT,padx=5)

#Labels
Label(secondBulkFrame,text="Select Field:").grid(row=0,column=0)
Label(secondBulkFrame,text="Change to:").grid(row=1,column=0)

#Entry to change vakue
bulkChangeEntry=Entry(secondBulkFrame,justify=CENTER)
bulkChangeEntry.grid(row=1,column=1)



#===================================================================END OF CANVAS'=======================


#===============================================ARRAYS==================

canvasArray=[filterPupilCanvas,openCanvas,changeUserNameCanvas,changeThemeCanvas,changeBackgroundCanvas,viewPupilCanvas,viewAllCanvas,createPupilCanvas,bulkEditCanvas]
themeEntry=Entry(window)
pupilDataArray=[]
filterPupilArray=[]
passGrades=["A*","A","B","C"]
mainPBOptions=["100m","Long Jump","200m","Javelin","Hurdles"]
numberOfPB=len(mainPBOptions)
numberOfTextItems+=numberOfPB
newAddedPupils=[]
menuPupils=[]
newOrderPupils=[]
# Start of Functions===========================================================


#Function to insert text into entry
def insertEntry(entry,message):
    if entry.winfo_class() == "Text":
        entry.delete("1.0",END)
    else:

        entry.delete(0,END)
    entry.insert(END,message)

def loadCanvas(canvas,message):
    global currentViewCanvas
    global currentViewCanvasArray

    currentViewCanvasArray=[]
    if canvas != currentViewCanvas:
        for item in canvasArray:
            if item != canvas:
                item.pack_forget()
        canvas.pack(expand=True)
        currentViewCanvas.set(canvas)
        currentViewCanvasArray.append(canvas)
        statusVar.set(message)
        if canvas == bulkEditCanvas:
            window.geometry("700x350")
        else:
            window.geometry("450x350")


#====================================New added funtions======================



#Function that returns lines read
def getReadLines(fileToRead):
    try:
        fileToRead=str(fileToRead)
        file=open(fileToRead,"r")
    except:
        print("Error when opening",fileToRead)
    else:
        content=file.readlines()
        file.close()
        return content


#The main function that retrives the users name from the file
def getUserName():
    global userName
    content=getReadLines("userName.txt")
    possibleWords=[]
    foundValid=False

    if content != "" and content != None:
        if len(content) > 0:
            for line in content:
                wordsOnLine=line.split()
                for item in wordsOnLine:
                    possibleWords.append(item)

                if "userName123:" in wordsOnLine:
                    foundValid=True
                    print("Valid userName format")
                    if len(wordsOnLine) > 2:
                        userName=wordsOnLine[1]
                        userName=userName+" "
                        secondName=wordsOnLine[2]
                        secondName=secondName.capitalize()
                        userName+=secondName
                    elif len(wordsOnLine) > 1:
                        userName=wordsOnLine[1]
                        if userName != "" and userName != " ":
                            userName=userName

                        else:
                            print("UserName in file is a space")
                            userName="User"
                    else:
                        print("No name has been used in file")
                        userName="User"

                    break


            if foundValid == False:
                print("A valid format has not been found looking for alternitives")
                if len(possibleWords) > 0:
                    sortedwords = sorted(possibleWords, key=len)
                    chosenWord=sortedwords[0]
                    if ":" in chosenWord and len(possibleWords) > 1:
                        chosenWord=possibleWords[1]

                    print("Using",chosenWord,"as name")
                    userName=chosenWord

                else:
                    userName="User"

        else:
            print("No content found in userName file")
            userName="User"

        nameArray=[]
        wordsInName=userName.split()
        for word in wordsInName:
            word=word.capitalize()
            nameArray.append(word)

        tempUser=""
        for name in nameArray:
            tempUser+=name
            tempUser+=" "
        tempUser=tempUser.rstrip()
        userName=tempUser
        print("Using",userName,"as username")
        return userName


    else:
        return "User"


#The function that takes the name from the text file and displays it on the home screen
def setOpenUser(name):
    if name != "" and name != None:
        temp="Welcome "
        temp=temp+name
        userVar.set(temp)

#The Function that is launched when the change username function loads from file menu
def changeUserName():
    loadCanvas(changeUserNameCanvas,"Change Info")
    global userName
    insertEntry(changeUserNameEntry,userName)
    overwriteUserNameButton.config(state=DISABLED)

#Function that saves a new username when the user changes it
def overwriteUserName():
    global userName
    userName1=changeUserNameEntry.get()
    temp="userName123: "
    temp=temp+userName1
    saveLineToFile("userName.txt",temp,"userName123:")
    insertEntry(changeUserNameEntry,userName1)
    updateWelcomeScreen(userName1)
    userName=userName1
    overwriteUserNameButton.config(state=DISABLED)

#The function that is launched every letter the user types when changing the username
#It compares the new username they type to the original one and if the new one is the same
#As the old one the overwrite button becomes disabled

def checkOverwrite(event):
    global userName
    changeUserNameEntry.config(state=NORMAL)
    text=changeUserNameEntry.get()
    comparison=userName

    if text == comparison:
        overwriteUserNameButton.config(state=DISABLED)
    else:
        overwriteUserNameButton.config(state=NORMAL)


def changeTheme():
    loadCanvas(changeThemeCanvas, "Theme")

def submitTheme(colour):


    temp="defaultColour: "
    temp=temp+colour

    #Writing to username file to store colour
    updateTheme(colour)
    updateMenuBG(colour)
    clearFilterPupils()
    saveLineToFile("userName.txt",temp,"defaultColour:")
    print("Theme changed to",colour)





def showOpenCanvas():
    leng=len(newOrderPupils)
    numberVar.set(leng)
    loadCanvas(openCanvas,"Home")

def newUpdate(themeORBackground,colour):
    themeArray=["Button","OptionMenu"]
    backgroundArray=["Entry","Button","Text"]

    #Change Theme
    if themeORBackground == "Theme":
        print("=============Ready to update theme==========")



    #Change Background
    elif themeORBackground == "Background":
        print("Ready to update background")


def updateTheme(colour):
    if colour != None:
        colourPicked.set(colour)
        widgetArray=["Button","OptionMenu"]
        for item in canvasArray:
            childArray=item.winfo_children()
            while len(childArray) > 0:
                for widget in childArray:
                    if widget.winfo_class() in widgetArray:
                        try:
                            widget.config(bg=colour)
                        except:
                            print("Error changing widget info")

                    childArray=widget.winfo_children()


    #Change status  widget colours
    try:
        status.config(bg=colour)
    except:
        print("Error with changing status colour")
        print("Using default colours because of unsupported colours:",colour)
        status.config(bg=defaultColour)


def getThemeFromFile():
    targetLine=getFromFile("userName.txt","defaultColour:")
    found=False
    if targetLine != "" and targetLine != None:
        segments=targetLine.split()
        if len(targetLine) > 1:
            try:
                colour=segments[1]
                if len(segments) > 2:
                    colour=colour+segments[2]
            except:
                print("Indexing error")
            else:
                found=True
                return colour

        if found == False:
            print("Colour retival has failed using default colour")
            return defaultColour

    print("Error when getting info from file function using defaults")
    return defaultColour

#Initialises the theme setup process
def initTheme():
    colour=getThemeFromFile()
    if colour != "" and colour != None:
        print("Testing theme colour...")
        result=checkColour(colour)
        if result != None and result != "":
            updateMenuBG(colour)
            print("Testing sucess")
            updateTheme(colour)
            updateButtonBackground(colour)
        else:
            print("Testing of",colour,"failure using default")
            updateTheme(defaultColour)





def saveLineToFile(file,lineToAdd,target):
    lineToAdd=lineToAdd.rstrip()
    content=getReadLines(file)
    print()
    print("Initiating overwrite process -------------")
    print("File to open is:",file)
    print("Line to overwrite with is",lineToAdd)
    print("Target to replace is",target)
    contentArray=[]

    #If there is a problem with the file a new one is created
    if content == "" or content == None:
        print("An error occoured opening",file,"creating new one")
        file=open(file,"w")
        file.close()
    else:

        for line in content:
            words=line.split()
            if target in words:
                print("Found target")
            else:
                contentArray.append(line)

        try:
            fileToWrite=open(file,"w")
        except:
            print("Error opening",file,"to write info")
        else:

            fileToWrite.write(lineToAdd)
            fileToWrite.write("\n")
            for item in contentArray:
                fileToWrite.write(item)

            fileToWrite.close()
            askMessage("Sucess","Changed infomation")


def writeArrayToFile(fileName,array):
    try:
        file=open(fileName,"w")
    except:
        askError("Error", "Error opening file")
    else:
        for line in array:
            file.write(line)
            file.write("\n")
        file.close()
        print("Writing complete")


def getFromFile(fileToSearch,target):
    print()
    print("Initialising retrival -------------------")
    print("The retrival target is",target)
    print("The File that is been searched is",fileToSearch)
    content=getReadLines(fileToSearch)
    if content != None and content != "":
        found=False
        for line in content:
            words=line.split()
            if target in words:
                found=True
                print("Target has been found")
                print("Returning",line)
                print()
                return line
                break
    else:
        return ""


def checkColour(colour):
    tempEntry=Entry(window)
    words=colour.split()
    try:
        tempEntry.config(bg=colour)
    except:
        print(colour,"is not valid")
        if len(words) > 1:
            try:
                col=words[1]
                tempEntry.config(bg=col)
            except:
                print("Error changing colour")
            else:
                return col

    else:
        return colour

def updateWelcomeScreen(name):
    setOpenUser(name)

def updateThemeStep():
    index = colourListBox.curselection()
    try:
        colourPick=colourListBox.get(index)
    except:
        pass
    else:
        updateButtonBackground(colourPick)
        submitTheme(colourPick)



def colourPicker():
    colour= colorchooser.askcolor()[1]
    if colour != None and colour != "":
        submitTheme(colour)



def changeBackground():
    loadCanvas(changeBackgroundCanvas, "Change Background")

def backgroundColourPicker():
    colour= colorchooser.askcolor()[1]
    if colour != "" and colour != None:
        submitBackgroundTheme(colour)

def submitBackgroundTheme(colour):

    updateBackgroundColours(colour)

    temp="defaultBackground: "
    temp=temp+colour
    temp=temp+"\n"
    saveLineToFile("userName.txt", temp, "defaultBackground:")
    print("Saved background theme to file")


def updateBackgroundStep():
    index = backgroundListBox.curselection()
    try:
        colourPick=backgroundListBox.get(index)
    except:
        pass
    else:
        submitBackgroundTheme(colourPick)

def getBackgroundFromFile():
    testEntry=Entry(window)
    targetLine=getFromFile("userName.txt", "defaultBackground:")
    if targetLine != None and targetLine != "":
        words=targetLine.split()
        if len(words) > 2:
            try:
                colour=words[1]
                second=words[2]
                temp=""
                temp=temp+colour
                temp=temp+" "
                temp=temp+second
                colour=temp
            except:
                print("Indexing background error")
            else:
                try:
                    testEntry.config(bg=colour)
                except:
                    print("Background test failed trying other options Colour tested:",colour)
                    try:
                        temp=words[1]
                    except:
                        print("Indexing error using default")
                        colour=window.cget("bg")
                    else:
                        colour=temp
                        try:
                            testEntry.config(bg=colour)
                        except:
                            print("Second background test failed trying last option Colour tested:",colour)
                            try:
                                colour=words[2]
                            except:
                                print("Indexing error in colours")
                            else:
                                try:
                                    testEntry.config(bg=colour)
                                except:
                                    print("Last colour failure using defualt")
                                    colour=window.cget("bg")
                                else:
                                    colour=colour

                        else:
                            print("Second background test sucess")
                            colour=temp
        else:
            tempEntry=Entry(window)
            valid=False
            for item in words:
                try:
                    tempEntry.config(bg=item)
                except:

                    valid=False
                else:
                    print("Colour",item,"worked")
                    valid=True
                    colour=item
                    break

            if valid == False:
                colour=window.cget("bg")

        return colour


def initBackground():
    col=getBackgroundFromFile()
    print("Using",col,"as colour")
    if col != None and col != "":
        updateBackgroundColours(col)


def updateBackgroundColours(colour):
    widgetArray=["Entry","Button","Text","Listbox","OptionMenu","Menu"]
    window.config(bg=colour)

    for item in canvasArray:
        item.config(bg=colour)
        for widget in item.winfo_children():
            if widget.winfo_class() not in widgetArray:
                try:
                    widget.config(bg=colour)
                except:
                    print("Error changing widget info")
                else:
                    if widget.winfo_class() == "Frame":
                        arr=widget.winfo_children()
                        while len(arr) > 0:
                            for item in arr:
                                if item.winfo_class() not in widgetArray:
                                    try:
                                        item.config(bg=colour)
                                    except:
                                        print("Error changing",item.winfo_class())
                                    else:
                                       arr=item.winfo_children()
                                    try:
                                        widget.config(highlightbackground=colour)
                                    except:
                                        pass
                                else:
                                    arr=item.winfo_children()
                                try:
                                    item.config(highlightbackground=colour)
                                except:
                                    print("Highlight error")
            try:
                widget.config(highlightbackground=colour)
            except:
                print("Widget error changing highlight colour",widget)


def updateButtonBackground(colour):
    for item in canvasArray:
                for widget in item.winfo_children():
                    if widget.winfo_class() == "Button":
                        try:
                            widget.config(bg=colour)
                            widget.config(activebackground=colour)
                        except:
                            print("Error updating widgets")


#The Function that toggles the text for a certain widget saving the need for one on every widget
def toggleText(variable,widgetChoice):

    if variable == "black":
        variable="white"
    elif variable == "white":
        variable="black"

    for item in window.winfo_children():
        print(item.winfo_class())
        if item.winfo_class() in widgetChoice:
            item.config(fg=variable)
        childArray=item.winfo_children()
        while len(childArray) > 0:
            for child in childArray:
                if child.winfo_class() in widgetChoice:
                    child.config(fg=variable)
                childArray=child.winfo_children()


    return variable


def toggleLabelTextColour():
    global mainLabelTextColour
    mainLabelTextColour=toggleText(mainLabelTextColour,["Label"])


def getPupilsFromFile(file):
    global newAddedPupils
    global pupilDataArray
    duplicates=0
    added=0


    placeFiller="Unknown?"
    print("Getting Pupil data---------------")
    data=getReadLines(file)
    if data != None and data != "":
        lineCounter=0
        for line in data:
            lineCounter+=1
            tempUserArray=[]
            if line == "=======================\n":
                for x in range(0,numberOfTextItems):
                    try:
                        lineData=data[lineCounter+x]
                        lineData=lineData.rstrip()
                    except:
                        tempUserArray.append(placeFiller)
                    else:
                        if lineData != "=======================":
                            tempUserArray.append(lineData)
                        else:
                            tempUserArray.append(" ")

                if tempUserArray in pupilDataArray:
                    duplicates+=1
                else:
                    pupilDataArray.append(tempUserArray)
                    newAddedPupils.append(tempUserArray)
                    added+=1

    print("Added",added,"pupils")
    print("Prevented",duplicates,"duplicates")


#This function will take all pupil infomation and create a drop down menu with them all.

def addPupilsMenu(array):
    array=sorted(array)
    duplicateArray=[]
    for pupil in array:
        if pupil not in duplicateArray:
            duplicateArray.append(pupil)
            try:
                pupilInfo=pupil[0]
                pupilPB=pupil[1]
            except:
                print("INDEX ERROR")
            else:
                try:
                    name=pupilInfo[0]
                    second=pupilInfo[1]
                    grade=pupilInfo[2]
                    notes=pupilInfo[3]
                except:
                    print("Error")
                else:
                    try:
                        temp=""
                        temp+=name
                        temp+=" "
                        tup=second
                        temp+=tup[0]
                        displayName=temp
                    except:
                        print("Error creating display name")
                    else:
                        subPupilMenu.add_command(
                        label=displayName,command=lambda showArray=pupil
                        : showPupil(showArray))







def showPupil(fieldArray):
    numberOfDisplayItems=4
    global currentViewPupil

    if currentViewPupil != fieldArray:


        displayPersonalBestVar.set("")
        chosenPeronalBestToView.set("Select PB")
        overwritePupilButton.config(state=DISABLED)
        insertEntry(viewPersonalBestEntry,"")

        try:
            pupilData=fieldArray[0]
            pbArray=fieldArray[1]
        except:
            askError("Error","Error viewing pupil")
        else:
            try:
                name=pupilData[0]
                second=pupilData[1]
                grade=pupilData[2]
                notes=pupilData[3]

            except:
                print("INDEXING ERROR SHOWING PUPIL")
            else:
                insertEntry(showPupilName, name)
                insertEntry(showPupilSecond, second)
                insertEntry(showPupilGrade,  grade)
                insertEntry(showPupilNotes, notes)

                #Display canvas
                loadCanvas(viewPupilCanvas, "Showing Pupil")
                #Updates current pupil
                currentViewPupil=fieldArray





#The function that runs every time the keyboard is pressed to update overwrite button state

def checkIfSame(key):
    global currentViewPupil
    global overwriteArray

    tempArray=getPupilInfo(viewPupilCanvas)
    overwriteArray=tempArray
    if tempArray == currentViewPupil:
        overwritePupilButton.config(state=DISABLED)
    else:
        overwritePupilButton.config(state=NORMAL)


def overWritePupil(deleteOrNot):
    global currentViewPupil
    global overwriteArray

    copyArray=newOrderPupils
    found=False
    pCounter=0

    #Overwrite and delete section
    foundPupil=False

    for pupil in newOrderPupils:
        try:
            dataSection=pupil[0]
            pbSection=pupil[1]
        except:
            askError("Error","Error with pupil format")
        else:
            if currentViewPupil == pupil:
                print("Pupil found in database")
                break


    #DELETE SECTION
    if deleteOrNot == "Delete":
        print("=============Ready to delete pupil========")
        if currentViewPupil in copyArray:
            try:
                copyArray.remove(currentViewPupil)
            except:
                print("Error removing pupil")
            else:
                if currentViewPupil in copyArray:
                    print("Pupil is still in array")
                else:

                    #Code here to delete pupil
                    saveNewPupils(copyArray)

        else:
            print("Pupil not found")



    #OVERWRITE section
    else:
        print("=============Ready to overwrite pupil========")
        print(overwriteArray)
        if currentViewPupil in copyArray:
            try:
                copyArray.remove(currentViewPupil)
            except:
                print("Error removing pupil")
            else:
                copyArray.append(currentViewPupil)

                #Save overwrite here
                saveNewPupils(copyArray)



def saveNewPupils(array):
    print("Saving new data")
    valid=False
    try:
        if len(array) > 0:
            valid=True
    except:
        print("Not an array passed to function")
    else:
        if valid == True:
            try:
                file=open("pupils.txt","w")
            except:
                print("Error opening file")
            else:
                for pupil in array:
                    #Write pupils to file here
                    try:
                        fileData=pupil[0]
                        filePB=pupil[1]
                    except:
                        print("Error with pupil format")
                    else:
                        file.write("=======================\n")

                        #Write Data here
                        for item in fileData:
                            try:
                                item=item.rstrip()
                            except:
                                print("Error formating line")
                            else:
                                file.write(item)
                                file.write("\n")

                        #Write PB section
                        for item in filePB:
                            try:
                                item=item.rstrip()
                            except:
                                print("Error formating line")
                            else:
                                file.write(item)
                                file.write("\n")

                file.close()
                askMessage("Success","Overwrite success restart to update")
                overwritePupilButton.config(state=DISABLED)
                showOpenCanvas()


def overWritePupilStep():
    askMessage("Broken","This function is currently not working")
    """
    try:
        overWritePupil("not")
    except:
        askError("Error","Error overwriting pupil")
    """

def deletePupilStep():
    try:
        option=messagebox.askyesno("Sure?","Are you sure you want to delete this Pupil?")

    except:
        print("Error with tkinter")

    else:
        if option == True:
            try:
                overWritePupil("Delete")
            except:
                askError("Deleting","An error occoured deleting pupil")


def showAllPupils():
    optionVar.set("Order by")
    colour=status.cget("bg")
    colour2=window.cget("bg")

    if version == "Windows":
        orderPupilOption.config(bg=colour)
    else:
        orderPupilOption.config(bg=colour2)
    orderPupilOption.config(activebackground=colour)


    entrytoInsert=[previewName,previewSecond,previewGrade]
    for item in entrytoInsert:
        item.config(state=NORMAL)
        insertEntry(item, "")
        item.config(state=DISABLED)

    loadCanvas(viewAllCanvas, "Viewing all pupils")
    viewAllListbox.delete(0,END)

    if len(newOrderPupils) > 0:
        insertListbox(viewAllListbox, newOrderPupils)



def showCreatePupil():
    loadCanvas(createPupilCanvas,"Create Pupil")
    #Initial setup
    addNewPBButton.config(state=DISABLED)
    createPupilPersonalBestVar.set("Select")


def newFilter():
    loadCanvas(filterPupilCanvas,"Filter Pupils")
    clearFilterResultsButton.config(bg=filterPupilCanvas.cget("bg"))
    clearFilterResultsButton.config(activebackground=filterPupilCanvas.cget("bg"))
    cl=status.cget("bg")
    cl2=window.cget("bg")
    if version == "Windows":
        filterPupilOption.config(bg=cl)
    filterPupilOption.config(activebackground=cl)


def checkPupil(pupil,target,item):

    found=False
    results=[]

    #Direct Checking
    if target == item:
        results.append(pupil)
        found=True
    elif target in item:
        results.append(pupil)
        found=True

    #Capital checking
    if found == False:
        copyTarget=target.capitalize()
        copyItem=item.capitalize()

        if copyItem == copyTarget:
            found=True
        elif copyTarget in copyItem:
            found=True

    return found

#Main search Function updated for Version 7.0
def searchPupils():
    global newOrderPupils
    #Sets up arrays for results
    resultArray=[]

    areaToSearch=filterVariable.get()
    target=filterPupilEntry.get()
    target=str(target)
    if target == None:
        askMessage("Enter","Please enter something")
    else:
        matchSearchArray=["First Name","Second Name","Grade","Personal Best","All"]
        matchPos=matchSearchArray.index(areaToSearch)
        matchArea=matchSearchArray[matchPos]
        if matchArea in matchSearchArray:

            #PB section
            if matchArea == "Personal Best":
                for pupil in newOrderPupils:
                    try:
                        section=pupil[1]
                    except:
                        print("Search Error")
                    else:
                        for item in section:
                            found=checkPupil(pupil,target,item)
                            if found == True:
                                resultArray.append(pupil)


            elif matchArea == "All":
                for pupil in newOrderPupils:
                    for section in pupil:
                        for item in section:
                            found=checkPupil(pupil,target,item)
                            if found == True:
                                resultArray.append(pupil)

            #Other fields
            else:
                try:
                    index=matchSearchArray.index(matchArea)
                    match=matchSearchArray[index]
                except:
                    print("Not a valid field to search")
                else:
                    for pupil in newOrderPupils:
                        try:
                            section=pupil[0]
                        except:
                            print("Error with pupil format")
                        else:
                            try:
                                subSection=section[index]
                            except:
                                print("Error with pupil sub format")
                            else:
                                found=checkPupil(pupil,target,subSection)
                                if found == True:
                                    resultArray.append(pupil)


        #Tells user if no results
        if len(resultArray) < 1:
            askMessage("No results","The search returned no results")
            clearFilterPupils()
            filterResults.insert(END,"No results")
            numberOfFilterResults.set(0)
        else:
            print("Search Sucess")
            #Section to show results

            filterResults.delete(0,END)
            counter=0
            col=status.cget("bg")
            filterPupilArray=[]

            #Remove duplicates
            for item in resultArray:
                if item not in filterPupilArray:
                    filterPupilArray.append(item)

            #Shows results on screen
            filterPupilArray=sorted(filterPupilArray)
            insertListbox(filterResults, filterPupilArray)

            #Displays number of results

            leng=len(filterPupilArray)
            leng=str(leng)
            numberOfFilterResults.set(leng)

def clearFilterPupils():
    filterResults.delete(0,END)



def updateMenuBG(colour):
    menuArray=[]
    childArray=mainMenu.winfo_children()
    while len(childArray) > 0:
        for widget in childArray:
            try:
                widget.config(activebackground=colour)
            except:
                print("Error changing menu BG")

            childArray=widget.winfo_children()


def viewFilterResults(event):

    try:
        doubleClick(filterResults, newOrderPupils)
    except:
        print("Error loading pupil")



def viewallResults(event):
    if viewAllListbox.size() > 0:
        try:
            doubleClick(viewAllListbox, newOrderPupils)
        except:
            askError("Error", "Error loading double click pupil")

def doubleClick(listbox,array):
    currentView=listbox.curselection()
    currentitem=listbox.get(currentView)
    for item in array:
        try:
            pupilData=item[0]
        except:
            print("Pupil indexing error")
        else:
            words=currentitem.split()
            try:
                valid1=False
                valid2=False
                if pupilData[0] == words[0]:
                    valid1=True
                if pupilData[1] == words[1]:
                    valid2=True
                if valid1 == True and valid2 == True:
                    break
            except:
                print("ERROR")

    try:
        showPupil(item)
    except:
        print("Error with show pupil function")


def getPupilInfo(canvas):

    #Bit that gets data for pupil
    dataArray=[]
    for widget in canvas.winfo_children():
        if widget.winfo_class() == "Entry" or widget.winfo_class() == "Text":
            try:
                data=widget.get()
                data=data.rstrip()
                data.capitalize()
            except:
                try:
                    data=widget.get("1.0",END)
                    data=data.rstrip()
                except:
                    print("Error")
                else:
                    dataArray.append(data)

            else:
                dataArray.append(data)

    #Bit that gets PB's for pupil
    PBArray=[]

def createPupilInfo():

    content=getPupilInfo(createPupilCanvas)

    #Add optionMenu bit here

    leng=len(content)
    valid=True
    try:
        for x in range(0,leng-1):
            current=content[x]
            if current == "" or current == None:
                valid=False
                break
    except:
        print("Error checking content")

    else:
        if valid == False:
            askMessage("Info", "All fields except notes must be filled")
        else:
            print("Fine")

            savePupilToFile(content)

            #clear canvas
            clearCanvas(createPupilCanvas)
            showOpenCanvas()


def clearCanvas(canvas):
    for widget in canvas.winfo_children():
        if widget.winfo_class() == "Entry":
            widget.delete(0,END)
        if widget.winfo_class() == "Notes":
            widget.delete("1.0",END)

def savePupilToFile(array):
    global pupilDataArray
    if array not in pupilDataArray:
        pupilDataArray.append(array)
        try:
            file=open("pupils.txt","a")
        except:
            file=open("pupils.txt","w")

        file.write("=======================\n")
        for line in array:
            file.write(line)
            file.write("\n")


        askMessage("Success","Pupil created")


    else:
        askMessage("Duplicate","This pupil allready exists")






#Function to add binding to all entry widgets on canvas

def addBinding(canvas,function):
    for widget in canvas.winfo_children():
        if widget.winfo_class() == "Entry" or widget.winfo_class() == "Text":
            try:
                widget.bind("<Return>",function)
            except:
                print("Error binding widget")

def createPupilInfoStep(event):
    createPupilInfo()


def optionCommand(value):
    tempArray=[]

    #Order by First Name
    if value == "A-Z (First name)":
        tempArray=sorted(newOrderPupils)
        insertListbox(viewAllListbox, tempArray)

    #Order by Second Name
    if value == "A-Z (Second name)":
        firstSort=[]
        mainArray=[]
        for pupil1 in newOrderPupils:
            try:
                pupil=pupil1[0]
            except:
                print("Pupil format error")
            else:
                personalArray=[]
                try:
                    name=pupil[0]
                    second=pupil[1]
                    grade=pupil[2]
                except:
                    print("Indexing error")
                    name="?"
                    second="?"
                    grade="?"

                personalArray.append(second)
                personalArray.append(name)
                personalArray.append(grade)
                firstSort.append(personalArray)

        sortArray=sorted(firstSort)
        temp1=[]

        #Reveses Array
        for item in sortArray:
            personalArray=[]
            try:
                second=item[0]
                first=item[1]
                grade=item[2]
            except:
                print("Indexing error")
                second="?"
                first="?"
                grade="?"

            personalArray.append(first)
            personalArray.append(second)
            personalArray.append(grade)
            mainArray.append(personalArray)

        newOrderArray=[]
        for item in mainArray:
            data=getPupilFromNewArray(item)
            newOrderArray.append(data)
        insertListbox(viewAllListbox, newOrderArray)

   #Order by Grades
    if value == "Grade":
        grades=["A*","A","B","C","D","E","F"]
        firstArray=[]
        mainArray=[]

        invalidGrades=[]
        for pupil1 in newOrderPupils:
            try:
                pupil=pupil1[0]
            except:
                print("Pupil Format error")
            else:
                personalArray=[]
                try:
                    name=pupil[0]
                    second=pupil[1]
                    grade=pupil[2]
                except:
                    print("Indexing error")
                    name="?"
                    second="?"
                    grade="?"


                if grade in grades:
                    try:
                        pos=grades.index(grade)
                    except:
                        print("Indexing error")
                        pos=grade

                else:
                    tm=[]
                    pos="*"
                    try:
                        name=pupil[0]
                        second=pupil[1]
                        grade=pupil[2]
                    except:
                        name="?"
                        second="?"
                        grade="?"

                    tm.append(grade)
                    tm.append(name)
                    tm.append(second)
                    invalidGrades.append(tm)

                if pos != "*":
                    personalArray.append(pos)
                    personalArray.append(name)
                    personalArray.append(second)
                    firstArray.append(personalArray)


        sortArray=sorted(firstArray)
        for pupil in invalidGrades:
            sortArray.append(pupil)
        #Reversing array
        for item in sortArray:
            personalArray=[]
            try:
                grade=grades[item[0]]
                name=item[1]
                second=item[2]
            except:
                try:
                    name=item[1]
                except:
                    name="?"
                try:
                    second=item[2]
                except:
                    second="?"
                try:
                    grade=item[0]
                except:
                    grade="?"

            personalArray.append(name)
            personalArray.append(second)
            personalArray.append(grade)
            mainArray.append(personalArray)


        newOrderArray=[]
        for item in mainArray:
            data=getPupilFromNewArray(item)
            newOrderArray.append(data)
        insertListbox(viewAllListbox, newOrderArray)




#Function ot insert array into lisbox
def insertListbox(listbox,array):
    #Find items in listbox
    listboxData=[]
    listboxes=[listbox]
    if listbox == bulkAllPupilListbox:
        listboxes.append(bulkFilterPupilListbox)

    for item in listboxes:
        try:
            leng=item.size()
        except:
            print("Not listbox format")
        else:
            for x in range(0,leng):
                try:
                    current=item.get(x)
                except:
                    print("Indexing error inserting listbox")
                else:
                    listboxData.append(current)


    for pupil in array:
        try:
            sub=pupil[0]
        except:
            print("Pupil format error")
        else:
            try:
                name=sub[0]
                second=sub[1]
                grade=sub[2]
            except:
                name="?"
                second="?"
                grade="?"

            temp=""
            temp+=name
            temp+=" "
            temp+=second


            if temp not in listboxData:

                if grade in passGrades:

                    pupilColour="light green"
                else:
                    pupilColour="salmon"

                listbox.insert(END,temp)
                listbox.itemconfig(END,bg=pupilColour)

def insertListboxNonDelete(listbox,array):

    listboxData=[]
    try:
        leng=listbox.size()
    except:
        print("Not listbox format")
    else:
        for x in range(0,leng):
            try:
                current=listbox.get(x)
            except:
                print("Indexing error inserting listbox")
            else:
                listboxData.append(current)

    for pupil in array:
        try:
            name=pupil[0]
            second=pupil[1]
            grade=pupil[2]
        except:
            name="?"
            second="?"
            grade="?"

        temp=""
        temp+=name
        temp+=" "
        temp+=second



        if grade in passGrades:

            pupilColour="light green"
        else:
            pupilColour="salmon"

        if temp not in listboxData:
            listbox.insert(END,temp)
            listbox.itemconfig(END,bg=pupilColour)

def searchPupilStep(event):
    searchPupils()

def pupilGradeClick(event):
    index = viewAllListbox.curselection()
    try:
        picked=viewAllListbox.get(index)
    except:
        pass
    else:
        words=picked.split()
        for pupil in pupilDataArray:
            valid1=False
            valid2=False
            try:
                if pupil[0] == words[0]:
                    valid1=True
                if pupil[1] == words[1]:
                    valid2=True

                if valid1 == True and valid2 == True:
                    break
            except:
                print("ERROR")


        try:
            entrytoInsert=[previewName,previewSecond,previewGrade]
            for item in entrytoInsert:

                item.config(state=NORMAL)
                dataPos=entrytoInsert.index(item)
                data=pupil[dataPos]
                insertEntry(item, data)
                if item == previewGrade:
                    grade=pupil[dataPos]
                    if grade not in passGrades:
                        item.config(fg="red")
                    else:
                        item.config(fg="black")
                item.config(state=DISABLED)
        except:
            print("Error loading pupil")

def viewAllResultsStep():
    viewallResults("")

def askMessage(pre,message):

    try:
        messagebox.showinfo(pre,message)
    except:
        print(message)
def viewPersonalBest(value):
    global currentViewPupil

    try:
        pbArray=currentViewPupil[1]
    except:
        print("Pupil indexing error")
    else:
        firstMatchArray=mainPBOptions
        secondMatchArray=pbArray
        try:
            pos=mainPBOptions.index(value)
        except:
            print("Indexing error")
        else:
            try:
                match=secondMatchArray[pos]
            except:
                print("Error finding PB")
            else:
                temp=value
                temp+=":"
                displayPersonalBestVar.set(temp)
                viewPersonalBestEntry.config(state=NORMAL)
                insertEntry(viewPersonalBestEntry, match)



def askError(pre,message):
    try:
        messagebox.showerror(pre,message)
    except:
        print(message)

def createAddPB():
    global currentCreatePupil
    createPupilPersonalBestVar
    print("Current",createPupilPersonalBestVar.get())

def createPupilOptionMenuFunction(value):
    textFromEntry=createPupilTarget.get()
    words=textFromEntry.split()
    if len(words) > 0:
        if value != "Select":
            addNewPBButton.config(state=NORMAL)
    else:
        addNewPBButton.config(state=DISABLED)


#Function to order PB's into seperate arrays
#This new order array is used throughout rest of program
def orderPB():
    global newOrderPupils
    newOrderPupils=[]

    numberOfDataItems=4

    #COPYS THE pupil array
    copyArray=pupilDataArray
    for pupil in copyArray:

        #Sets up pupil arrays
        newPupilOverall=[]
        newPupilData=[]
        newPupilPB=[]

        #Adds main data
        for x in range(0,numberOfDataItems):
            try:
                currentItem=pupil[x]
            except:
                newPupilData.append("???")
            else:
                newPupilData.append(currentItem)

        #Adds main PB
        range1=numberOfDataItems
        range2=range1+numberOfPB
        for y in range(range1,range2):
            try:
                currentPB=pupil[y]
            except:
                newPupilPB.append("???")
            else:
                newPupilPB.append(currentPB)


        newPupilOverall.append(newPupilData)
        newPupilOverall.append(newPupilPB)

        #Saves to new array here
        newOrderPupils.append(newPupilOverall)





def changeOptionWidth(widget):
    if version == "Windows":
        widget.config(width=13)
    else:
        widget.config(width=20)

def loadBulkEdit():
    loadCanvas(bulkEditCanvas, "Bulk Edit")
    temp=newOrderPupils
    temp=sorted(temp)
    insertListbox(bulkAllPupilListbox,temp)

    #if button configs are needed
    alternateButtonConfig("Add")
    alternateButtonConfig("")


#Right click menu
def viewPupilPopup(event):
    data=currentViewCanvasArray[0]

    #Only show menu on that canvas
    if data == viewPupilCanvas:
        viewPupilMiniMenu.post(event.x_root, event.y_root)

def showPupilTab():
    global currentViewPupil
    current=currentViewPupil
    try:
        data=current[0]
        pbArray=current[1]
    except:
        print("Error with pupil format")
    else:

        #window setup
        newT=Tk()
        newWindow=Frame(newT)
        newWindow.pack(expand=True)

        newT.geometry("300x300")
        Label(newWindow,text="Name").grid(row=0,column=0)
        Label(newWindow,text="Second").grid(row=1,column=0)
        Label(newWindow,text="Grade").grid(row=2,column=0)
        Label(newWindow,text="Notes").grid(row=3,column=0)

        newWindowName=Entry(newWindow)
        newWindowName.grid(row=0,column=1)

        newWindowSecond=Entry(newWindow)
        newWindowSecond.grid(row=1,column=1)

        newWindowGrade=Entry(newWindow)
        newWindowGrade.grid(row=2,column=1)

        newWindowNotes=Entry(newWindow)
        newWindowNotes.grid(row=3,column=1)

        matchArray=mainPBOptions
        position=3
        for item in pbArray:
            position+=1
            pos=pbArray.index(item)
            match=matchArray[pos]
            Label(newWindow,text=match).grid(row=position,column=0)

            tempEntry=Entry(newWindow)
            tempEntry.delete(0,END)
            tempEntry.insert(END,item)
            tempEntry.grid(row=position,column=1)

        try:
            displayName=data[0]
        except:
            print("Error finding display name")
        else:
            newT.title(displayName)
            displayArray=[newWindowName,newWindowSecond,newWindowGrade,newWindowNotes]
            for item in data:
                pos=data.index(item)
                match=displayArray[pos]
                match.delete(0,END)
                match.insert(END,item)



#Function that gets pupil from array
def getPupilFromArray(wordArray):
    words=wordArray
    for pupil in pupilDataArray:
        valid1=False
        valid2=False
        if pupil[0] == words[0]:
            valid1=True
        if pupil[1] == words[1]:
            valid2=True
        try:

            if valid1 == True and valid2 == True:
                break
        except:
            print("ERROR")

    if valid1 == True and valid2 == True:
        return pupil

def prePreAddBulkPupil(event):
    preAddBulkPupil()

def preAddBulkPupil():
    try:
        addBulkPupil()
        alternateButtonConfig("Add")
    except:
        print("Error passing function for bulk edit")


def addBulkPupil():
    pos=bulkAllPupilListbox.curselection()
    leng=len(pos)
    removeArray=[]
    if leng > 0 and leng < 2:
        if len(pos) > 0:
            item=getListboxItem(pos, bulkAllPupilListbox)
            try:
                words=item.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkFilterPupilListbox, temp)
                bulkAllPupilListbox.delete(pos)
                try:

                    bulkAllPupilListbox.selection_set(pos)
                except:
                    bulkAllPupilListbox.selection_set("end")


            except:
                print("Error loading pupil")

    else:

        for item in pos:
            selectedItem=getListboxItem(item, bulkAllPupilListbox)

            try:
                words=selectedItem.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkFilterPupilListbox, temp)
                removeArray.append(item)
                try:

                    bulkAllPupilListbox.selection_clear(0,END)
                except:
                    print("Selection error")

            except:
                print("Error loading pupil")

        miniCounter=-1
        #Removes from listboxes after they have been added
        for item in removeArray:
            miniCounter+=1
            if miniCounter != 0:
                pos=item-miniCounter

            else:
                pos=item
            try:
                bulkAllPupilListbox.delete(pos)
            except:
                print("Error removing pupil from listbox")

def getListboxItem(pos,listbox):
    try:
        item=listbox.get(pos)
    except:
        askError("Error", "Error retrieving listbox item")
        return "? ?"
    else:
        return item

def prePreRemoveBulkPupil(event):
    preRemoveBulkPupil()

def preRemoveBulkPupil():
    removeBulkPupil()
    alternateButtonConfig("")

def removeBulkPupil():
    pos=bulkFilterPupilListbox.curselection()
    leng=len(pos)
    removeArray=[]
    if leng > 0 and leng < 2:
        if len(pos) > 0:
            item=getListboxItem(pos, bulkFilterPupilListbox)
            try:
                words=item.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkAllPupilListbox, temp)
                bulkFilterPupilListbox.delete(pos)
                try:
                    bulkFilterPupilListbox.selection_set(pos)
                except:
                    bulkFilterPupilListbox.selection_set("end")


            except:
                print("Error loading pupil for filter")
    else:

        for item in pos:
            selectedItem=getListboxItem(item, bulkFilterPupilListbox)

            try:
                words=selectedItem.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkAllPupilListbox, temp)
                removeArray.append(item)
                try:
                    bulkFilterPupilListbox.selection_clear(0,END)
                except:
                    print("Selection error")

            except:
                print("Error loading pupil")

    miniCounter=-1
    #Removes from listboxes after they have been added
    for item in removeArray:
        miniCounter+=1
        if miniCounter != 0:
            pos=item-miniCounter

        else:
            pos=item
        try:
            bulkFilterPupilListbox.delete(pos)
        except:
            print("Error removing pupil from listbox")

#Function to check len of listboxes each button press
#Then based on length of lisbox config buttons
def alternateButtonConfig(addOrRemove):
    size=bulkAllPupilListbox.size()
    if size  < 1:
        addBulkPupilButton.config(state=DISABLED)
        addAllBulkPupilsButton.config(state=DISABLED)
    else:
        addBulkPupilButton.config(state=NORMAL)
        addAllBulkPupilsButton.config(state=NORMAL)

    #Alternate butons
    size2=bulkFilterPupilListbox.size()
    if size2 > 0:
        removeBulkPupilButton.config(state=NORMAL)


    size=bulkFilterPupilListbox.size()
    if size < 1:
        removeBulkPupilButton.config(state=DISABLED)
        removeAllBulkPupilsButton.config(state=DISABLED)
    else:
        removeBulkPupilButton.config(state=NORMAL)
        removeAllBulkPupilsButton.config(state=NORMAL)

    #Alternate
    size2=bulkAllPupilListbox.size()
    if size2 > 0:
        addBulkPupilButton.config(state=NORMAL)

def preAddAllBulkPupils():
    addAllBulkPupils()
    alternateButtonConfig("Add")


def addAllBulkPupils():
    try:
        items=bulkAllPupilListbox.get(0,END)
    except:
        print("Error getting pupils fom listbox")
    else:
        for currentItem in items:
            try:
                words=currentItem.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkFilterPupilListbox,temp)
                bulkAllPupilListbox.delete(END)
            except:
                askError("Error","Error adding pupils")
                break

def preRemoveAllBulkPupils():
    removeAllBulkPupils()
    alternateButtonConfig("")

def removeAllBulkPupils():
    try:
        items=bulkFilterPupilListbox.get(0,END)
    except:
        print("Error getting pupils fom listbox")
    else:
        for currentItem in items:
            try:
                words=currentItem.split()
                pupil=getPupilFromArray(words)
                temp=[]
                temp.append(pupil)
                insertListboxNonDelete(bulkAllPupilListbox,temp)
                bulkFilterPupilListbox.delete(END)
            except:
                askError("Error","Error removing pupils")
                break


def preSubmitBulkEdit():
    try:
        submitBulkEdit()
    except:
        askError("Error","Error saving pupils")

def submitBulkEdit():
    field=bulkEditOptionVar.get()
    text=bulkChangeEntry.get()
    print(text)
    print(field)

    #Retrivse pupil info
    data=bulkFilterPupilListbox.get(0,END)
    pupilInfoArray=[]
    for item in data:
        words=item.split()
        pupil=getPupilFromArray(words)
        pupilInfoArray.append(pupil)

    matchArray=bulkEditOptionArray
    pos=matchArray.index(field)
    for pupil in pupilInfoArray:
        pupil[pos]=text

    print(pupilInfoArray)
    try:
        option=messagebox.askyesno("Overwrite","Do you want to overwrite these pupils?")
    except:
        print("Tkinter error")
    else:
        if option == "Yes":
            print("Ready to delete")

    #Saves new files
    #for item in pupilInfoArray:




def unlockBulkOptions(event):
    if event != "Select Field":
        submitBulkEditButton.config(state=NORMAL)

def addAllBind(canvas,function):
    for item in canvas.winfo_children():
        childArray=widget.winfo_children()
        while len(arr) > 0:
            for item in arr:
                print()

def getPupilFromNewArray(wordArray):
    for item in newOrderPupils:
        try:
            pupil=item[0]
        except:
            print("Pupil format error")
        else:
            try:
                valid1=False
                valid2=False
                valid3=False
                if pupil[0] == wordArray[0]:
                    valid1=True
                if pupil[1] == wordArray[1]:
                    valid2=True
                if pupil[2] == wordArray[2]:
                    valid3=True

                if valid1 == True and valid2 == True and valid3 == True:
                    break
            except:
                print("Error indexing pupil")


    return(item)

def addJustify(canvas,centerOrNot):

    if centerOrNot == True:
        changeArray=["Entry"]
        for item in canvas.winfo_children():

            if item.winfo_class() in changeArray:
                item.config(justify=CENTER)

            childArray=item.winfo_children()
            while len(childArray) > 0:
                for child in childArray:
                    if child.winfo_class() in changeArray:
                        print(child.winfo_class())
                        child.config(justify=CENTER)

                childArray=child.winfo_children()

    else:
        changeArray=["Entry"]
        for item in canvas.winfo_children():

            if item.winfo_class() in changeArray:
                item.config(justify=LEFT)

            childArray=item.winfo_children()
            while len(childArray) > 0:

                for child in childArray:
                    if child.winfo_class() in changeArray:
                        print(child.winfo_class())
                        child.config(justify=LEFT)

                childArray=child.winfo_children()

#Function to toggle alignment of text in the view pupil canvas
toggleSide=StringVar()
toggleSide.set("Center")
def toggleTextPos():
    global toggleSide
    if toggleSide.get() == "Center":
        toggleSide.set("Left")
        addJustify(viewPupilCanvas,False)
    else:
        addJustify(viewPupilCanvas,True)
        toggleSide.set("Center")


def preBulkViewAllMenu(event):
    bulkEditMenu("Add",event)

def preBulkFilterMenu(event):
    bulkEditMenu("Remove",event)

def bulkEditMenu(listbox,event):
    if listbox == "Add":
        try:
            pos=bulkAllPupilListbox.curselection()
        except:
            pass
        else:

            #This line stops the pop up menu if nothing is selected
            if len(pos) > 0:
                bulkViewMiniMenu.post(event.x_root, event.y_root)
    elif listbox == "Remove":
        try:
            pos=bulkFilterPupilListbox.curselection()
        except:
            pass
        else:

            #This line stops the pop up menu if nothing is selected
            if len(pos) > 0:
                filterViewMiniMenu.post(event.x_root, event.y_root)

def toggleStatus():
    statusCol=status.cget("fg")
    statusCol.capitalize()
    if statusCol == "White" or statusCol == "white":
        status.config(fg="Black")
    else:
        status.config(fg="White")


def bulkCheckCommand():
    value=bulkCheckVar.get()
    if value == 1:
        bulkAllPupilListbox.config(selectmode='extended')
        bulkFilterPupilListbox.config(selectmode='extended')
    else:
        bulkAllPupilListbox.selection_clear(0, END)
        bulkAllPupilListbox.config(selectmode="browse")

        bulkFilterPupilListbox.selection_clear(0, END)
        bulkFilterPupilListbox.config(selectmode="browse")


def loadDoubleClick(listbox):
    try:
        doubleClick(listbox, newOrderPupils)
    except:
        askError("Error","Error loading pupil")

def bulkDisableViewAll(event):
    leng=bulkAllPupilListbox.size()
    if leng > 0:
        addAllBulkPupilsButton.config(state=NORMAL)
        addBulkPupilButton.config(state=NORMAL)
        removeAllBulkPupilsButton.config(state=DISABLED)
        removeBulkPupilButton.config(state=DISABLED)

def bulkDisableFilter(event):
    leng=bulkFilterPupilListbox.size()
    if leng > 0:
        addAllBulkPupilsButton.config(state=DISABLED)
        addBulkPupilButton.config(state=DISABLED)
        removeAllBulkPupilsButton.config(state=NORMAL)
        removeBulkPupilButton.config(state=NORMAL)
#Command that is used by listboxes in bulk edit to view pupils

#Add cascades and commands=====================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)
mainMenu.add_cascade(label="Pupils",menu=pupilMenu)
mainMenu.add_cascade(label="Filter",menu=filterMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
#File Menu
fileMenu.add_command(label="Home",command=showOpenCanvas)
fileMenu.add_separator()
fileMenu.add_command(label="New Pupil",command=showCreatePupil)
fileMenu.add_separator()



#View Menu
viewMenu.add_command(label="Toggle Text Colour",command=toggleLabelTextColour)
viewMenu.add_command(label="Toggle Bar Text Colour",command=toggleStatus)

viewMenu.add_separator()
viewMenu.add_command(label="Change Info",command=changeUserName)
viewMenu.add_command(label="Change Theme",command=changeTheme)
viewMenu.add_command(label="Change Background",command=changeBackground)

#Pupil Menu
pupilMenu.add_command(label="View All",command=showAllPupils)
pupilMenu.add_command(label="New Pupil",command=showCreatePupil)
pupilMenu.add_separator()
pupilMenu.add_cascade(label="Pupils",menu=subPupilMenu)

#Filter Menu
filterMenu.add_command(label="New Filter",command=newFilter)

#Edit menu
editMenu.add_command(label="Bulk Edit",command=loadBulkEdit)




#=============================Option Menu===============

#Options for ordering
orderPupilOption=OptionMenu(bottomViewAllFrame,optionVar,*pupilOptions,command=optionCommand)
orderPupilOption.pack(side=BOTTOM,pady=9)
optionVar.set("Order by")

#Options for PB
personalBestOptions=mainPBOptions
showPupilPersonalBestOptions=OptionMenu(viewPupilCanvas,chosenPeronalBestToView,*personalBestOptions,command=viewPersonalBest)
changeOptionWidth(showPupilPersonalBestOptions)
showPupilPersonalBestOptions.grid(row=3,column=1,pady=2)

#Create pupil options
createPupilOptions=mainPBOptions
createPupilPersonalBestVar=StringVar()
createPupilPersonalBestVar.set("Select")
createPupilPersonalBestOption=OptionMenu(createPupilCanvas,createPupilPersonalBestVar,*createPupilOptions,command=createPupilOptionMenuFunction)
changeOptionWidth(createPupilPersonalBestOption)
createPupilPersonalBestOption.grid(row=3,column=1,pady=2)

#Bulk edit options
bulkEditOptionVar=StringVar()
bulkEditOptionVar.set("Select field")
bulkEditOptionArray=["Grade"]
bulkEditOptionMenu=OptionMenu(secondBulkFrame,bulkEditOptionVar,*bulkEditOptionArray,command=unlockBulkOptions)
bulkEditOptionMenu.grid(row=0,column=1)

#==============================Buttons===================


#Buttons for theme change
choseThemeButton=Button(changeThemeCanvas,text="Change",command=updateThemeStep,relief=FLAT)
choseThemeButton.pack(side=BOTTOM,fill=X,padx=8,pady=5)

colourPickerButton=Button(changeThemeCanvas,text="Colour Picker",command=colourPicker,relief=FLAT)
colourPickerButton.pack(side=BOTTOM,pady=5,fill=X,padx=8)

#Overwrite username button
overwriteUserNameButton=Button(changeUserNameCanvas,text="Overwrite",command=overwriteUserName,state=DISABLED,relief=FLAT)
overwriteUserNameButton.grid(row=1,column=1,pady=8)

#Button for change background

choseThemeButton=Button(changeBackgroundCanvas,text="Change",command=updateBackgroundStep,relief=FLAT)
choseThemeButton.pack(side=BOTTOM,fill=X,padx=8,pady=5)

backgroundColourPickerButton=Button(changeBackgroundCanvas,text="Colour Picker",command=backgroundColourPicker,relief=FLAT)
backgroundColourPickerButton.pack(side=BOTTOM,pady=5,fill=X,padx=8)

#Button for overwriting and deleting data
overwritePupilButton=Button(viewPupilCanvas,text="Overwrite",state=DISABLED,command=overWritePupilStep,relief=FLAT,width=15)
overwritePupilButton.grid(row=6,column=1,pady=9)

deletePupilButton=Button(viewPupilCanvas,text="Delete",command=deletePupilStep,relief=FLAT,width=15)
deletePupilButton.grid(row=7,column=1,pady=4)

#Button for filtering pupils
filterPupilButton=Button(filterPupilCanvas,text="Search",relief=FLAT,width=13,command=searchPupils)
filterPupilButton.grid(row=2,column=1,pady=9)

clearFilterResultsButton=Button(filterPupilCanvas,text="Clear",relief=FLAT,command=clearFilterPupils)
clearFilterResultsButton.grid(row=3,column=2)

#Buttons for creating pupil
createPupilButton=Button(createPupilCanvas,text="Create",width=15,command=createPupilInfo,relief=FLAT)
createPupilButton.grid(row=6,column=1,pady=7)

#Button for adding PB on create canvas
addNewPBButton=Button(createPupilCanvas,text="Add",command=createAddPB,relief=FLAT)
addNewPBButton.grid(row=4,column=2,padx=9)

#Buttons for view all pupils
viewAllPupilButton=Button(secondViewAllFrame,text="View",command=viewAllResultsStep,relief=FLAT)
viewAllPupilButton.grid(row=4,column=1,pady=6)

#Bulk edit buttons
addBulkPupilButton=Button(mainListboxFrame,text="Add",width=10,command=preAddBulkPupil,relief=FLAT)
addBulkPupilButton.pack()

removeBulkPupilButton=Button(mainListboxFrame,text="Remove",width=10,command=preRemoveBulkPupil,relief=FLAT)
removeBulkPupilButton.pack()

removeAllBulkPupilsButton=Button(mainListboxFrame,text="Remove All",width=10,command=preRemoveAllBulkPupils,relief=FLAT)
removeAllBulkPupilsButton.pack(side=BOTTOM)

addAllBulkPupilsButton=Button(mainListboxFrame,text="Add All",width=10,command=preAddAllBulkPupils,relief=FLAT)
addAllBulkPupilsButton.pack(side=BOTTOM)


submitBulkEditButton=Button(secondBulkFrame,text="Change",width=15,command=preSubmitBulkEdit,state=DISABLED,relief=FLAT)
submitBulkEditButton.grid(row=2,column=1,pady=5)

deleteBulkButton=Button(secondBulkFrame,text="Delete Selected",width=15,relief=FLAT)
deleteBulkButton.grid(row=3,column=1,pady=3)


#=============Checkbuttons==========
bulkCheckVar=IntVar()
check=Checkbutton(mainListboxFrame,text="Select",command=bulkCheckCommand,variable=bulkCheckVar,state=NORMAL)
check.pack(pady=10)



#Right click Menus---------------

#Menu for view pupil
viewPupilMiniMenu = Menu(currentViewPupil, tearoff=0)
viewPupilMiniMenu.add_command(label="Open pupil in new tab",command=showPupilTab)
viewPupilMiniMenu.add_command(label="Toggle text position",command=toggleTextPos)

#Bulk edit listboxes add mini menu
bulkViewMiniMenu=Menu(bulkEditCanvas,tearoff=0)
bulkViewMiniMenu.add_command(label="View Pupil",command=lambda :loadDoubleClick(bulkAllPupilListbox))
bulkViewMiniMenu.add_separator()
bulkViewMiniMenu.add_command(label="Add Pupil",command=preAddBulkPupil)
bulkViewMiniMenu.add_separator()
bulkViewMiniMenu.add_command(label="Add All",command=addAllBulkPupils)

#Bulk edit listboxes remove mini menu
filterViewMiniMenu=Menu(bulkEditCanvas,tearoff=0)
filterViewMiniMenu.add_command(label="View Pupil",command=lambda :loadDoubleClick(bulkFilterPupilListbox))
filterViewMiniMenu.add_separator()
filterViewMiniMenu.add_command(label="Remove Pupil",command=preRemoveBulkPupil)
filterViewMiniMenu.add_separator()
filterViewMiniMenu.add_command(label="Remove All",command=removeAllBulkPupils)

#Bindings-------------------------
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)
filterResults.bind('<Double-Button-1>', viewFilterResults)
viewAllListbox.bind('<Double-Button-1>', viewallResults)
viewAllListbox.bind('<ButtonRelease-1>', pupilGradeClick)
viewAllListbox.bind('<Up>', pupilGradeClick)
viewAllListbox.bind('<Down>', pupilGradeClick)

#Mac and PC right click bindings are diffrent
if version == "Darwin":
    window.bind("<Button-2>", viewPupilPopup)
    bulkAllPupilListbox.bind("<Button-2>",preBulkViewAllMenu)
    bulkFilterPupilListbox.bind("<Button-2>",preBulkFilterMenu)
else:
    window.bind("<Button-3>", viewPupilPopup)
    bulkAllPupilListbox.bind("<Button-3>",preBulkViewAllMenu)
    bulkFilterPupilListbox.bind("<Button-3>",preBulkFilterMenu)


showPupilName.bind("<KeyRelease>",checkIfSame)
showPupilSecond.bind("<KeyRelease>",checkIfSame)
showPupilGrade.bind("<KeyRelease>",checkIfSame)
showPupilNotes.bind("<KeyRelease>",checkIfSame)

bulkAllPupilListbox.bind("<Double-Button-1>",prePreAddBulkPupil)
bulkFilterPupilListbox.bind("<Double-Button-1>",prePreRemoveBulkPupil)

bulkAllPupilListbox.bind("<Button-1>",bulkDisableViewAll)
bulkFilterPupilListbox.bind("<Button-1>",bulkDisableFilter)

createPupilTarget.bind("<KeyRelease>",createPupilOptionMenuFunction)

#These function needs to be here because it changes colours of buttons that would otherwise be under it

#=======Returns===========

setOpenUser(getUserName())
getPupilsFromFile("pupils.txt")

#Order array
orderPB()

#Returns to gather infomation or initiate functions

addPupilsMenu(newOrderPupils)
addBinding(createPupilCanvas, createPupilInfoStep)
addBinding(filterPupilCanvas,searchPupilStep)
initBackground()
initTheme()
showOpenCanvas()
addJustify(viewPupilCanvas,True)

newUpdate("Theme","red")
#Runs program
window.mainloop()
