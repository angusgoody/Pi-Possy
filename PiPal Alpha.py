__author__ = 'Angus'

#Angus Goody
#8/10/15

#Pi Pal version 4.3

#Imports-------
from tkinter import *
import datetime
from tkinter import colorchooser
import platform
import tkinter.filedialog
import random

version=platform.system()
print("System platform is",version)
#Sets up window---------
window=Tk()
window.geometry("450x350")
window.title("PiPal")

#Staus bar
statusVar=StringVar()
status=Label(window,text="Status",bg="lightblue",textvariable = statusVar)
status.pack(side=BOTTOM,fill=X)

 #Main variables=================
mainButtonColour="light green"
userName=""
encryptionKey=8
mainEntryTextColour="black"
mainLabelTextColour="black"
numberOfTextItems=5 #The variable for how many items are contained for each pupil in the text file
#Toolbars====================
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub menus==================
fileMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)
pupilMenu=Menu(mainMenu)
filterMenu=Menu(mainMenu)
#===================================================================CANVAS'=======================


#Open canvas-------------------------------------------
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)
statusVar.set("Home")
userVar=StringVar()

openLabel=Label(openCanvas,textvariable=userVar,font= "Helvetica 16 bold")
openLabel.grid(row=0,column=1)

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
colourPicked.set("lightblue")

colourListBox=Listbox(changeThemeCanvas)
colourListBox.pack(side=LEFT)

#Slider for listbox
colourSlider=Scrollbar(changeThemeCanvas)
colourSlider.pack(side=RIGHT,fill=Y)

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
backgroundSlider.pack(side=RIGHT,fill=Y)

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
Label(viewPupilCanvas,text="Target:").grid(row=3,column=0)
Label(viewPupilCanvas,text="Notes:").grid(row=4,column=0)


showPupilName=Entry(viewPupilCanvas)
showPupilName.grid(row=0,column=1,pady=2)

showPupilSecond=Entry(viewPupilCanvas)
showPupilSecond.grid(row=1,column=1,pady=2)

showPupilGrade=Entry(viewPupilCanvas)
showPupilGrade.grid(row=2,column=1,pady=2)

showPupilTarget=Entry(viewPupilCanvas)
showPupilTarget.grid(row=3,column=1,pady=2)

if version == "Windows":
    showPupilNotes=Text(viewPupilCanvas,height=5,width=15,wrap=WORD)
else:
    if version == "Darwin":
        showPupilNotes=Text(viewPupilCanvas,font=("Helvetica", "12"),height=5,width=24,wrap=WORD)
    if version == "Linux":
        showPupilNotes=Text(viewPupilCanvas,font=("Helvetica", "12"),height=5,width=18,wrap=WORD)
        

showPupilNotes.grid(row=4,column=1,pady=2)

#Canvas for viewing all students-----------------------------------
viewAllCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

viewAllListbox=Listbox(viewAllCanvas,width=25)
viewAllListbox.pack(side=LEFT)

viewAllSlider=Scrollbar(viewAllCanvas)
viewAllSlider.pack(side=RIGHT,fill=Y)

viewAllSlider.config(command=viewAllListbox.yview)
viewAllListbox.config(yscrollcommand=viewAllSlider.set)
#Canvas for creating new pupil--------------------------------------

createPupilCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(createPupilCanvas,text="First Name:").grid(row=0,column=0)
Label(createPupilCanvas,text="Second Name:").grid(row=1,column=0)
Label(createPupilCanvas,text="Grade").grid(row=2,column=0)
Label(createPupilCanvas,text="Target:").grid(row=3,column=0)
Label(createPupilCanvas,text="Notes:").grid(row=4,column=0)

createPupilName=Entry(createPupilCanvas)
createPupilName.grid(row=0,column=1,pady=2)

createPupilSecond=Entry(createPupilCanvas)
createPupilSecond.grid(row=1,column=1,pady=2)

createPupilGrade=Entry(createPupilCanvas)
createPupilGrade.grid(row=2,column=1,pady=2)

createPupilTarget=Entry(createPupilCanvas)
createPupilTarget.grid(row=3,column=1,pady=2)

if version == "Windows":
    createPupilNotes=Text(createPupilCanvas,height=5,width=15,wrap=WORD)
else:
    if version == "Linux":
        createPupilNotes=Text(createPupilCanvas,font=("Helvetica", "12"),height=5,width=18,wrap=WORD)
    else:
        createPupilNotes=Text(createPupilCanvas,font=("Helvetica", "12"),height=5,width=24,wrap=WORD)

createPupilNotes.grid(row=4,column=1,pady=2)

#Canvas for filtering pupils-------------------------------------------------------
filterPupilCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(filterPupilCanvas,text="Field:").grid(row=0,column=0)
Label(filterPupilCanvas,text="Search:").grid(row=1,column=0,pady=5)
Label(filterPupilCanvas,text="Results:").grid(row=3,column=0,pady=5)

filterVariable=StringVar()

filterPupilOption=OptionMenu(filterPupilCanvas,filterVariable,"Name","Second","Grade","Target","All")
filterPupilOption.grid(row=0,column=1,pady=5)
filterVariable.set("All")

filterPupilEntry=Entry(filterPupilCanvas)
filterPupilEntry.grid(row=1,column=1,padx=4)

filterResults=Listbox(filterPupilCanvas,bg="lightgrey")
filterResults.grid(row=3,column=1,pady=4)

#===================================================================END OF CANVAS'=======================
#Arrays
letterArray=['b', 'p', 'K', 'C', 'A', 'e', ' ', '0', '(', '?', 'B', '{', 'l', 'o', 'X', 'q', '|', ')', '3', '"', 'a', 'I', '}', '~', 'V', '%', '\x0c', '`', 'L', '4', 'D', 'z', 't', 'u', '#', 'M', '<', '+', 'T', '8', 'R', ':', '\t', 'E', 'Z', '9', '2', '@', 'h', 'y', "'", '=', 's', ';', 'x', '¦', 'G', '&', 'c', 'N', '6', 'S', '>', '5', '.', '_', '-', '/', 'Q', 'd', 'm', 'O', 'J', 'W', '¬', 'Y', ',', 'k', 'n', '1', '[', '7', 'H', 'j', 'r', '*', ']', 'i', 'P', '!', '\x0b', 'F', '$', '\\', 'U', 'g', 'f', '^', 'v', 'w']

sportArray=["Football","Hockey","Tennis","Basketball","Rugby"]
canvasArray=[filterPupilCanvas,openCanvas,changeUserNameCanvas,changeThemeCanvas,changeBackgroundCanvas,viewPupilCanvas,viewAllCanvas,createPupilCanvas]
themeEntry=Entry(window)
pupilDataArray=[]
filterPupilArray=[]

# Start of Functions===========================================================


#Function to insert text into entry
def insertEntry(entry,message):
    if entry.winfo_class() == "Text":
        entry.delete("1.0",END)
    else:
        entry.delete(0,END)
    entry.insert(END,message)

def loadCanvas(canvas,message):
    for item in canvasArray:
        if item != canvas:
            item.pack_forget()
    canvas.pack(expand=True)
    statusVar.set(message)

#Function that returns lines read
def getReadLines(fileToRead):
    try:
        fileToRead=str(fileToRead)
        file=open(fileToRead,"r")
    except:
        print("Error when opening",fileToRead)
    else:
        content=file.readlines()
        return content
        file.close()

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
        statusVar.set("Home")
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
    loadCanvas(openCanvas,"Home")

def updateTheme(colour):
    if colour != None:
        colourPicked.set(colour)
        widgetArray=["Button"]
        for item in canvasArray:
            for widget in item.winfo_children():
                if widget.winfo_class() in widgetArray:
                    try:
                        widget.config(bg=colour)
                    except:
                        print("Error changing widget info") 


    try:
        status.config(bg=colour)
    except:
        print("Error with changing status colour")
        print("Using default colours because of unsupported colours:",colour)
        status.config(bg="lightblue")


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
            return "lightblue"

    print("Error when getting info from file function using defaults")
    return "lightblue"

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
            updateTheme("lightblue")





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
        try:
            now = datetime.datetime.now()
            now=str(now)
        except:
            print("Error getting current date")
        else:
            print("Time stamp created")
            temp="Recovery File created on "
            temp=temp+now
            temp=temp+"\n"
            file.write(temp)
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
            print("Error opening",file,"to read info")
        else:
            
            fileToWrite.write(lineToAdd)
            fileToWrite.write("\n")
            for item in contentArray:
                fileToWrite.write(item)

            fileToWrite.close()
            try:
                messagebox.showinfo("Sucess","Changed infomation")
            except:
                print("Changed info")
            print()


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

#Function that can encrypt or decrypt a string using a key
def encOrDec(line,key,option):
    finArray=[]
    trackCounter=0
    for letter in line:
        trackCounter+=1
        if letter not in letterArray:
            finArray.append(letter)
            print(letter,"is not supported")
        else:
            letterLeng=len(letterArray)
            position=letterArray.index(letter)
            if option == "dec":
                newPos=position-key-trackCounter
            else:
                newPos=position+key+trackCounter
            while newPos > letterLeng:
                newPos=newPos-letterLeng
            if newPos == letterLeng:
                newPos=0
            try:
                newLetter=letterArray[newPos]
            except:
                print("Error indexing in encryption")
            else:
                finArray.append(newLetter)

    temp=""
    for item in finArray:
        temp=temp+item

    return temp


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
    widgetArray=["Entry","Button","Text","Listbox","OptionMenu"]
    window.config(bg=colour)
    for item in canvasArray:
        item.config(bg=colour)
        for widget in item.winfo_children():
            if widget.winfo_class() not in widgetArray:
                try:
                    widget.config(bg=colour)
                except:
                    print("Error changing widget info")
            widget.config(highlightbackground=colour)
            

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

    for item in canvasArray:
        for widget in item.winfo_children():
            if widget.winfo_class() == widgetChoice:
                widget.config(fg=variable)
    return variable


def toggleLabelTextColour():
    global mainLabelTextColour
    mainLabelTextColour=toggleText(mainLabelTextColour,"Label")


def getPupilsFromFile():
    placeFiller="Unknown?"
    print("Getting Pupil data---------------")
    data=getReadLines("pupils.txt")
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

                pupilDataArray.append(tempUserArray)


#This function will take all pupil infomation and create a drop down menu with them all.

def addPupilsMenu(array):


    for array in array:
        tempArray=[]
        for item in array:
            tempArray.append(item)
        try:
            field1=tempArray[0]
            field2=tempArray[1]
            field3=tempArray[2]
            field4=tempArray[3]
            field5=tempArray[4]
        except:
            print("Indexing error")
        else:
            temp=""
            temp+=field1
            temp+=" "
            tup=field2
            temp+=tup[0]
            displayName=temp

            #Menu bit

            pupilMenu.add_command(
            label=displayName,command=lambda item1=field1,
            item2=field2,
            item3=field3,
            item4=field4,
            item5=field5
            : showPupil(item1,item2,item3,item4,item5))


def showPupil(item1,item2,item3,item4,item5):
    overwritePupilButton.config(state=DISABLED)

    global currentViewPupil
    currentViewPupil=[]
    currentViewPupil.append(item1)
    currentViewPupil.append(item2)
    currentViewPupil.append(item3)
    currentViewPupil.append(item4)
    currentViewPupil.append(item5)
    #Bindings

    showPupilName.bind("<KeyRelease>",checkIfSame)
    showPupilSecond.bind("<KeyRelease>",checkIfSame)
    showPupilGrade.bind("<KeyRelease>",checkIfSame)
    showPupilTarget.bind("<KeyRelease>",checkIfSame)
    showPupilNotes.bind("<KeyRelease>",checkIfSame)

    loadCanvas(viewPupilCanvas, "Showing Pupil")

    insertEntry(showPupilName, item1)
    insertEntry(showPupilSecond, item2)
    insertEntry(showPupilGrade, item3)
    insertEntry(showPupilTarget, item4)
    insertEntry(showPupilNotes, item5)

#The function that runs every time the keyboard is pressed to update overwrite button state

def checkIfSame(key):
    global currentViewPupil
    global overwriteArray

    newFirst=showPupilName.get()
    newSecond=showPupilSecond.get()
    newGrade=showPupilGrade.get()
    newTarget=showPupilTarget.get()
    newNotes=showPupilNotes.get("1.0",END)
    newNotes=newNotes.rstrip()

    tempArray=[]
    tempArray.append(newFirst)
    tempArray.append(newSecond)
    tempArray.append(newGrade)
    tempArray.append(newTarget)
    tempArray.append(newNotes)

    overwriteArray=tempArray
    if tempArray == currentViewPupil:
        overwritePupilButton.config(state=DISABLED)
    else:
        overwritePupilButton.config(state=NORMAL)

def overWritePupil(deleteOrNot):
    global overwriteArray
    found=False
    pCounter=0
    for item in pupilDataArray:

        if item == currentViewPupil:
            pupilDataArray.remove(item)
            found=True
            break

        pCounter+=1

    #Get menu name
        
    deleteOrNot.capitalize()
    if deleteOrNot == "Delete":
        saveNewPupils(pupilDataArray)
        loadCanvas(openCanvas,"Home")
        clearFilterPupils()
        try:
            first=currentViewPupil[0]
            second=currentViewPupil[1]
        except:
            print("ERROR")
            temp=""
        else:
            temp=""
            temp+=first
            temp+=" "
            second=(second)
            temp+=second[0]
        try:
            pupilMenu.delete(temp)
        except:
            print("Error deleting pupil from menu")
    else:
        if found == True:
            pupilDataArray.insert(pCounter,overwriteArray)
            saveNewPupils(pupilDataArray)


def saveNewPupils(array):
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
                for item in array:
                    file.write("=======================\n")
                    for line in item:
                        file.write(line)
                        file.write("\n")

                file.close()
                try:
                    messagebox.showinfo("Success","Overwrite success restart to update")
                except:
                    print("Overwrite success")
                overwritePupilButton.config(state=DISABLED)


def overWritePupilStep():
    overWritePupil("not")

def deletePupilStep():
    try:
        option=messagebox.askyesno("Sure?","Are you sure you want to delete customer?")
    except:
        option=tkiner.filedialog.messagebox.askyesno("Sure?","Are you sure you want to delete customer?")
        
    else:
        if option == True:
            overWritePupil("Delete")

def showAllPupils():
    colour=status.cget("bg")
    colour2=window.cget("bg")
    viewAllListbox.config(selectbackground=colour2)
    loadCanvas(viewAllCanvas, "Viewing all pupils")
    viewAllListbox.delete(0,END)

    counter=1
    for item in pupilDataArray:
        try:
            name=item[0]
            second=item[1]
            temp=""
            temp+=name
            temp+=" "
            temp+=second
            viewAllListbox.insert(END,temp)
        except:
            print("ERROR")
        else:
            if counter % 2 == 0:
                cl=colour
                viewAllListbox.itemconfig(END,bg=cl)

            
        counter+=1

def showCreatePupil():
    loadCanvas(createPupilCanvas,"Create Pupil")

def newFilter():
    loadCanvas(filterPupilCanvas,"Filter Pupils")
    clearFilterResultsButton.config(bg=filterPupilCanvas.cget("bg"))
    clearFilterResultsButton.config(activebackground=filterPupilCanvas.cget("bg"))
    cl=status.cget("bg")
    cl2=window.cget("bg")
    filterResults.config(selectbackground=cl2)
    if version == "Windows":
        filterPupilOption.config(bg=cl)
    filterPupilOption.config(activebackground=cl)

def searchPupils():
    global filterPupilArray
    resultArray=[]
    area=filterVariable.get()
    target=filterPupilEntry.get()
    target=str(target)
    if target != "" and target != None:
        tempSearchArray=["Name","Second","Grade","Target","All"]
        if area == "All":
            pos="*"
        else:
            try:
                pos=tempSearchArray.index(area)
            except:
                print("Error finding field to search")
                pos="*"

        found=False
        #Searches all fields    
        if pos == "*":
            for pupil in pupilDataArray:
                for item in pupil:
                    if target in item:
                        found=True
                        resultArray.append(pupil)
                        break

        #Searches selected fields                
        else:
            for pupil in pupilDataArray:
                try:
                    dataItem=pupil[pos]
                except:
                    print("Pupil data item not found")
                else:
                    if target in dataItem:
                        found=True
                        resultArray.append(pupil)

        if found == False:
            try:
                messagebox.showinfo("None","No results were found")
            except:
                print("No results Found")

        else:
            filterResults.delete(0,END)
            counter=0
            col=status.cget("bg")
            for name in resultArray:
                try:
                    temp=""
                    first=name[0]
                    second=name[1]
                    temp+=first
                    temp+=" "
                    temp+=second
                except:
                    print("ERROR")
                else:
                    filterResults.insert(END,temp)
                    if counter % 2 == 0:
                        filterResults.itemconfig(END,bg=col)
                    else:
                        filterResults.itemconfig(END,bg="white")
                        
                    counter+=1
            filterPupilArray=resultArray
        

def clearFilterPupils():
    filterResults.delete(0,END)

def viewFilterResults(event):
    global filterPupilArray
    print(" ")
    index = filterResults.curselection()
    try:
        picked=filterResults.get(index)
    except:
        pass
    else:
        words=picked.split()
        for pupil in filterPupilArray:
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
            showPupil(pupil[0],pupil[1],pupil[2],pupil[3],pupil[4])
        except:
            print("Error loading pupil")
        

def updateMenuBG(colour):
    menuArray=[]
    for widget in mainMenu.winfo_children():
        try:
            widget.config(activebackground=colour)
        except:
            print("Error changing menu BG")
            

# End of Functions===========================================================

#Add cascades and commands=====================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)
mainMenu.add_cascade(label="Pupils",menu=pupilMenu)
mainMenu.add_cascade(label="Filter",menu=filterMenu)

#File Menu
fileMenu.add_command(label="Home",command=showOpenCanvas)
fileMenu.add_separator()
fileMenu.add_command(label="New Pupil",command=showCreatePupil)
fileMenu.add_separator()


#View Menu
viewMenu.add_command(label="Toggle Text Colour",command=toggleLabelTextColour)
viewMenu.add_separator()
viewMenu.add_command(label="Change Info",command=changeUserName)
viewMenu.add_command(label="Change Theme",command=changeTheme)
viewMenu.add_command(label="Change Background",command=changeBackground)

#Pupil Menu
pupilMenu.add_command(label="View All",command=showAllPupils)
pupilMenu.add_separator()

#Filter Menu
filterMenu.add_command(label="New Filter",command=newFilter)

#=======Returns===========
setOpenUser(getUserName())
getPupilsFromFile()
addPupilsMenu(pupilDataArray)

#Buttons================

#Buttons for theme change
choseThemeButton=Button(changeThemeCanvas,text="Change",command=updateThemeStep,relief=GROOVE)
choseThemeButton.pack(side=BOTTOM,fill=X,padx=8,pady=5)

colourPickerButton=Button(changeThemeCanvas,text="Colour Picker",command=colourPicker,relief=GROOVE)
colourPickerButton.pack(side=BOTTOM,pady=5,fill=X,padx=8)

#Overwrite username button
overwriteUserNameButton=Button(changeUserNameCanvas,text="Overwrite",command=overwriteUserName,state=DISABLED,relief=GROOVE)
overwriteUserNameButton.grid(row=1,column=1,pady=8)

#Button for change background

choseThemeButton=Button(changeBackgroundCanvas,text="Change",command=updateBackgroundStep,relief=GROOVE)
choseThemeButton.pack(side=BOTTOM,fill=X,padx=8,pady=5)

backgroundColourPickerButton=Button(changeBackgroundCanvas,text="Colour Picker",command=backgroundColourPicker,relief=GROOVE)
backgroundColourPickerButton.pack(side=BOTTOM,pady=5,fill=X,padx=8)

#Button for overwriting and deleting data
overwritePupilButton=Button(viewPupilCanvas,text="Overwrite",state=DISABLED,command=overWritePupilStep,relief=GROOVE,width=15)
overwritePupilButton.grid(row=5,column=1,pady=9)

deletePupilButton=Button(viewPupilCanvas,text="Delete",command=deletePupilStep,relief=GROOVE,width=15)
deletePupilButton.grid(row=6,column=1,pady=4)

#Button for filtering pupils
filterPupilButton=Button(filterPupilCanvas,text="Search",relief=GROOVE,width=13,command=searchPupils)
filterPupilButton.grid(row=2,column=1,pady=9)

clearFilterResultsButton=Button(filterPupilCanvas,text="Clear",relief=FLAT,command=clearFilterPupils)
clearFilterResultsButton.grid(row=3,column=2)

#Buttons for creating pupil
createPupilButton=Button(createPupilCanvas,text="Create",width=15)
createPupilButton.grid(row=5,column=1,pady=7)

#Bindings-------------------------
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)
filterResults.bind('<Double-Button-1>', viewFilterResults)
#This function needs to be here because it changes colours of buttons that would otherwise be under it
initBackground()
initTheme()

#print(pupilDataArray)

window.mainloop()
