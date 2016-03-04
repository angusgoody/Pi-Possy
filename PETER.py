__author__ = 'Angus'

#Angus Goody
#8/10/15

#PETER Version 1.0


#Main colour variable for if userName file is not found
defaultColour="maroon2"

#Imports-------
try:
    from tkinter import *
    from tkinter import filedialog
    from tkinter import colorchooser
    import tkinter.filedialog
    from tkinter import messagebox
except:
    print("Version of python not fully supported")
    from Tkinter import *
    from tkColorChooser import askcolor
    from tkFileDialog import *

import datetime

import platform

import random

import webbrowser


#Gets infomation about OS
#Because certain widgets behave diffrently on Linux,Mac and PC
version=platform.system()
print("System platform is",version)
if version == "Darwin":
    print("Not all Features are supported on MAC")

#Sets up window---------
window=Tk()
window.geometry("450x350")
window.title("PETER")

#So window cannot be resized
window.maxsize(700,400)
window.minsize(450,350)
#Staus bar
statusVar=StringVar()
status=Label(window,text="Status",bg=defaultColour,textvariable = statusVar)
status.pack(side=BOTTOM,fill=X)

#Main variables=================
mainButtonColour="light green"
mainThemeColour=StringVar()
mainThemeColour.set("light green")
mainBackgroundColour=StringVar()

userName=""
mainEntryTextColour="black"
mainLabelTextColour="black"
numberOfTextItems=4 #The variable for how many items are contained for each pupil in the text file
mainPupilName="pupils.txt"
mainUserName="userName.txt"
currentViewPupil=[]
currentCreatePupil=[]
currentViewCanvas=StringVar()
currentViewCanvasArray=[]
groupPupilArray=[]
mainGroupName=""
totalGroupDataArray=[]
currentCanvasMessage=StringVar()

passColour="light green"
failColour="salmon"
#Toolbars====================
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub menus==================
fileMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)
pupilMenu=Menu(mainMenu)
filterMenu=Menu(mainMenu)
editMenu=Menu(mainMenu)
groupMenu=Menu(mainMenu)
subPupilMenu=Menu(pupilMenu)
helpMenu=Menu(mainMenu)
#===================================================================CANVAS'=======================


#Open canvas-------------------------------------------
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)
statusVar.set("Home")
userVar=StringVar()

openLabel=Label(openCanvas,textvariable=userVar,font= "Helvetica 16 bold")
openLabel.pack(pady=5)

viewNumberFrame=Frame(openCanvas)
viewNumberFrame.pack(pady=10)

numberVar=StringVar()
numberVar.set("0")
viewTotalPupilLabel=Label(viewNumberFrame,text="Total Pupils:",justify=CENTER)
viewTotalPupilLabel.grid(row=0,column=0,pady=5)

showNumberLabel=Label(viewNumberFrame,textvariable=numberVar)
showNumberLabel.grid(row=0,column=1)

passVar=StringVar()
passVar.set("0")
showPassLabel=Label(viewNumberFrame,text="A-C Pupils:  ",justify=LEFT)
showPassLabel.grid(row=1,column=0,pady=5)

showPassNumberLabel=Label(viewNumberFrame,textvariable=passVar)
showPassNumberLabel.grid(row=1,column=1)

failVar=StringVar()
failVar.set("0")
showFailLabel=Label(viewNumberFrame,text="D-F Pupils:  ",justify=LEFT)
showFailLabel.grid(row=2,column=0,pady=5)

showFailNumber=Label(viewNumberFrame,textvariable=failVar)
showFailNumber.grid(row=2,column=1)



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

viewAllListbox=Listbox(mainViewAllFrame,width=28)
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
viewAllBulkFrame.pack(side=LEFT,padx=6)

bulkAllPupilListbox=Listbox(viewAllBulkFrame,width=16)
bulkAllPupilListbox.pack(side=LEFT)

bulkViewAllSlider=Scrollbar(viewAllBulkFrame)
bulkViewAllSlider.pack(side=RIGHT,fill=Y)

bulkViewAllSlider.config(command=bulkAllPupilListbox.yview)
bulkAllPupilListbox.config(yscrollcommand=bulkViewAllSlider.set)




#===========RIGHT SUB FRAME============

viewFilterBulkFrame=Frame(mainListboxFrame)
viewFilterBulkFrame.pack(side=RIGHT,padx=6)

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
fieldLabel=Label(secondBulkFrame,text="Select Field:")
fieldLabel.grid(row=0,column=0)
changeLabel=Label(secondBulkFrame,text="Change to:")
changeLabel.grid(row=1,column=0)

#Entry to change vakue
bulkChangeEntry=Entry(secondBulkFrame,justify=CENTER)
bulkChangeEntry.grid(row=1,column=1)

#Canvas for creating new group
newGroupCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(newGroupCanvas,text="Group Name:").grid(row=0,column=0)

groupNameEntry=Entry(newGroupCanvas)
groupNameEntry.grid(row=0,column=1)

groupListboxFrame=Frame(newGroupCanvas)
groupListboxFrame.grid(row=2,column=1)

groupListbox=Listbox(groupListboxFrame)
groupListbox.pack(side=LEFT)

groupSlider=Scrollbar(groupListboxFrame)
groupSlider.pack(side=RIGHT,fill=Y)

groupSlider.config(command=groupListbox.yview)
groupListbox.config(yscrollcommand=groupSlider.set)

#============Show Group Canvas=========
showGroupCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

showGroupLabelVar=StringVar()

showGroupLabel=Label(showGroupCanvas,textvariable=showGroupLabelVar)
showGroupLabel.grid(row=0,column=1,pady=5)

#Sub Frame for Listbox and Slider

showGroupListboxFrame=Frame(showGroupCanvas)
showGroupListboxFrame.grid(row=1,column=1,pady=5)

showGroupSlider=Scrollbar(showGroupListboxFrame)
showGroupSlider.pack(side=RIGHT,fill=Y)

showGroupListbox=Listbox(showGroupListboxFrame)
showGroupListbox.pack(side=LEFT)

showGroupSlider.config(command=showGroupListbox.yview)
showGroupListbox.config(yscrollcommand=showGroupSlider.set)

#===================================================================ADD NEW CANVAS' HERE ONLY=======================






#===================================================================ADD NEW CANVAS' HERE ONLY=======================


#===================================================================END OF CANVAS'=======================


#===============================================ARRAYS==================

canvasArray=[filterPupilCanvas,openCanvas,changeUserNameCanvas,changeThemeCanvas,changeBackgroundCanvas,showGroupCanvas,viewPupilCanvas,viewAllCanvas,createPupilCanvas,bulkEditCanvas,newGroupCanvas]
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
overWrittenPupils=[]
deletedPupils=[]
groupNameArray=[]

groupOrderArray=[]

beforeAddedGroups=[]
afterAddedGroups=[]
# Start of Functions===========================================================


#Function to insert text into entry
def insertEntry(entry,message):
    if entry.winfo_class() == "Text":
        entry.delete("1.0",END)
    else:

        entry.delete(0,END)
    entry.insert(END,message)

def loadCanvas(canvas,message):
    global currentCanvasMessage
    global currentViewCanvas
    global currentViewCanvasArray

    currentCanvasMessage.set(message)
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
            window.minsize(700,350)
        else:
            window.minsize(450,350)


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
    loadCanvas(changeThemeCanvas, "Change Theme")

def submitTheme(colour):
    global mainThemeColour

    temp="defaultColour: "
    temp=temp+colour

    #Writing to username file to store colour
    updateTheme(colour)
    updateMenuBG(colour)
    clearFilterPupils()
    mainThemeColour.set(colour)
    saveLineToFile("userName.txt",temp,"defaultColour:")
    print("Theme changed to",colour)





def showOpenCanvas():
    leng=len(newOrderPupils)
    numberVar.set(leng)
    loadCanvas(openCanvas,"Home")
    try:
        checkGrades()
    except:
        askError("Error","Error checking grades")





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

    #Bulk widgets
    bulkArray=[
        removeAllBulkPupilsButton,
removeBulkPupilButton,
addAllBulkPupilsButton,
submitBulkEditButton,
addBulkPupilButton,
deleteBulkButton
        ]

    for item in bulkArray:
        try:
            item.config(bg=colour)
        except:
            print("Error changeing button colour")




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
    mainThemeColour.set(colour)
    if colour != "" and colour != None:
        print("Testing theme colour...")
        result=checkColour(colour)
        if result != None and result != "":
            updateMenuBG(colour)
            print("Testing Success")
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
        fileToWrite=open(file,"w")

        fileToWrite.write(lineToAdd)
        fileToWrite.write("\n")
        fileToWrite.close()
        fileToWrite.close()
        askMessage("Success","Changed infomation")

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
            askMessage("Success","Changed infomation")


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
        try:
            choice=messagebox.askyesno("Sure","Are you sure you want to overwrite theme?")
        except:
            askError("Error","Error loading dialog box")
        else:
            if choice == True:
                updateButtonBackground(colourPick)
                submitTheme(colourPick)



def colourPicker():
    try:
        colour= colorchooser.askcolor()[1]
    except:
        colour=askcolor()
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
        try:
            choice=messagebox.askyesno("Sure","Are you sure you want to overwrite background colour?")
        except:
            askError("Error","Error loading dialog")
        else:
            if choice == True:
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
                            print("Second background test Success")
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
    else:
        updateBackgroundColours("chartreuse2")



def updateBackgroundColours(colour):
    global mainBackgroundColour
    widgetArray=["Entry","Button","Text","Listbox","OptionMenu","Menu"]
    window.config(bg=colour)
    mainBackgroundColour.set(colour)
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
                pass


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
        if item.winfo_class() in widgetChoice:
            item.config(fg=variable)
        childArray=item.winfo_children()
        while len(childArray) > 0:
            for child in childArray:
                if child.winfo_class() in widgetChoice:
                    child.config(fg=variable)
                childArray=child.winfo_children()


    labArray=[fieldLabel,changeLabel,check,showFailNumber,showFailLabel,showPassNumberLabel,showPassLabel,viewTotalPupilLabel,showNumberLabel]
    for item in labArray:
        try:
            item.config(fg=variable)
        except:
            print("Label error")

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
    global overWrittenPupils
    global deletedPupils
    numberOfDisplayItems=4
    global currentViewPupil


    if fieldArray in overWrittenPupils:
        print("In overwrite pupils")
        try:
            data=fieldArray[2]
        except:
            print("Format error")
        else:
            try:
                trackNumber=data[0]
            except:
                print("Track errror")
            else:
                for pupil in newOrderPupils:
                    try:
                        pupilData=pupil[2]
                    except:
                        print("Format error in overwritten pupils")
                    else:
                        try:
                            pupilTrack=pupilData[0]
                        except:
                            print("Invalid tracking format")
                        else:
                            if pupilTrack == trackNumber:
                                fieldArray=pupil

    #Decides wether to load the pupil or not depending on curret canvas
    if fieldArray not in deletedPupils:
        valid=False
        try:
            currentCanvas=currentViewCanvasArray[0]
        except:
            print("Canvas error")
        else:
            if currentCanvas == viewPupilCanvas:
                if fieldArray == currentViewPupil:
                    valid=False
                else:
                    valid=True
            else:
                valid=True

        if valid == True:



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

                    currentViewPupil=fieldArray
                    #Display canvas

                    loadCanvas(viewPupilCanvas, "Showing Pupil")
                    #Updates current pupil

    else:
        askMessage("Deleted","This pupil has been deleted")






#The function that runs every time the keyboard is pressed to update overwrite button state

def checkIfSame(key):
    global currentViewPupil
    global overwriteArray


    tempArray=newGetInfo()

    #get track number
    try:
        data=currentViewPupil[2]
    except:
        print("Current pupil error")
    else:
        try:
            tracker=data[0]
        except:
            print("Tracker not found")
        else:
            temp=[tracker]
            tempArray.append(temp)




    pbSame=checkPBSame(currentViewPB.get())

    #Updates the PB if needed
    if pbSame != True:
        current=chosenPeronalBestToView.get()
        try:
            pos=mainPBOptions.index(current)
        except:
            print("Could not find current PB")
        else:
            try:
                pbSection=currentViewPupil[1]
            except:
                print("Format error with pupil PB data")
            else:
                pbSection[pos]=pbSame


    if tempArray == currentViewPupil and pbSame == True:
        overwritePupilButton.config(state=DISABLED)
    else:
        overwritePupilButton.config(state=NORMAL)
        overwriteArray=tempArray


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
        #Gets menu pos

        if version == "Windows":
            menuPos=1
        else:
            menuPos=0

        tempCopy=newOrderPupils
        tempCopy=sorted(tempCopy)
        for pupil in tempCopy:
            if currentViewPupil == pupil:
                break
            menuPos+=1
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
                    deletedPupils.append(currentViewPupil)

                    #Gets menu pos
                    try:
                        if version == "Windows":
                            subPupilMenu.entryconfig(menuPos,state=DISABLED)
                        else:
                            subPupilMenu.delete(menuPos)
                    except:
                        print("Error disabling pupil menu")
                    else:
                        print("Removed pupil from menu")

        else:
            print("Pupil not found")



    #OVERWRITE section
    else:
        print()
        print("=============Ready to overwrite pupil========")
        print("Old data",currentViewPupil)
        print("New data",overwriteArray)
        print()
        print(overwriteArray)
        if currentViewPupil in copyArray:
            try:
                copyArray.remove(currentViewPupil)
            except:
                print("Error removing pupil")
            else:
                copyArray.append(overwriteArray)

                #Save overwrite here
                saveNewPupils(copyArray)



def saveNewPupils(array):
    array=sorted(array)

    print("Saving new data")
    valid=False
    try:
        if type(array) is list:
            valid=True
    except:
        print("Error with argument type")
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
                                item=str(item)
                                item=item.rstrip()
                            except:
                                print("Error formating PB")
                            else:
                                file.write(item)
                                file.write("\n")

                file.close()
                askMessage("Success","Overwrite success")

                overwritePupilButton.config(state=DISABLED)

                try:
                    canvas=currentViewCanvasArray[0]
                except:
                    print("Unable to get canvas infomation")
                    canvas=None

                if canvas != bulkEditCanvas:
                    showOpenCanvas()

                overWrittenPupils.append(currentViewPupil)
        else:
            print("This array is invalid and cannot be saved")


def overWritePupilStep():
    #askMessage("Broken","This function is currently not working")
    try:
        choice=messagebox.askyesno("Sure","Are you sure you want to overwrite data?")
    except:
        askMessage("Feature not supported on OS")
    else:
        if choice == True:
            try:
                overWritePupil("not")
            except:
                askError("Error","Error overwriting pupil")


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
            else:
                showOpenCanvas()


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
    setupCreatePB()


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

    target=str(target)
    item=str(item)

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

            clearFilterPupils()
            numberOfFilterResults.set(0)
            askMessage("No results","The search returned no results")
        else:
            print("Search Success")
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
    numberOfFilterResults.set("0")



def updateMenuBG(colour):
    for widget in mainMenu.winfo_children():
        try:
            widget.config(activebackground=colour)
        except:
            print("Error changing menu BG")
    try:
        subPupilMenu.config(activebackground=colour)
    except:
        print("Pupil sub menu error")



def preViewFilterResults():
    viewFilterResults("")

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

currentViewPB=StringVar()
def newGetInfo():
    global currentViewPB
    global currentCreatePupilPBArray
    name=showPupilName.get()
    second=showPupilSecond.get()
    grade=showPupilGrade.get()
    target=viewPersonalBestEntry.get()
    currentViewPB.set(target)
    placeHolder=showPupilNotes.get(1.0,END)
    words=placeHolder.split()
    notes=""
    for item in words:
        item=item.rstrip()
        notes=notes+item
        notes+=" "


    try:
        notes=notes.rstrip()
    except:
        print("Stripping error")

    try:
        pbSection=currentViewPupil[1]
    except:
        print("Format error with pupil")
        pbSection=[]


    returnArray=[[name,second,grade,notes],pbSection]
    return(returnArray)

def getPupilInfo(canvas):


    #Bit that gets data for pupil
    dataArray=[]
    for widget in canvas.winfo_children():
        if widget.winfo_class() == "Entry" or widget.winfo_class() == "Text":
            if widget != createPupilTarget:
                try:
                    data=widget.get()
                    data=data.rstrip()
                    data.capitalize()
                except:
                    try:
                        placeHolder=widget.get("1.0",END)
                        words=placeHolder.split()
                        data=""
                        for item in words:
                            item=item.rstrip()
                            data=data+item
                            data+=" "
                        print(data)
                    except:
                        print("Error")
                    else:
                        dataArray.append(data)

                else:
                    dataArray.append(data)



    return dataArray

def setupCreatePB():
    global currentCreatePupilPBArray
    currentCreatePupilPBArray=[]
    #Set up current array
    for x in range(0,numberOfPB):
        currentCreatePupilPBArray.append(["Unknown?"])

def createPupilInfo():
    global numberOfTrackers

    global currentCreatePupilPBArray

    mainPupilArray=[]
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
            mainPupilArray.append(content)
            tempArray=[]
            for item in currentCreatePupilPBArray:
                try:
                    if item == ["Unknown?"]:
                        tempArray.append(item[0])
                    else:
                        tempArray.append(item)
                except:
                    tempArray.append("Unknown?")
            mainPupilArray.append(tempArray)

            #Add trackNumber
            temp=[numberOfTrackers]
            mainPupilArray.append(temp)
            numberOfTrackers+=1

            #Section to construct array and save to file
            savePupilToFile(mainPupilArray)

            #Adds pupil to drop down menu
            try:
                pupilData=mainPupilArray[0]
            except:
                print("Error formating")
            else:
                try:
                    firstName=pupilData[0]
                    secondName=pupilData[1]
                    temp=""
                    temp+=firstName
                    temp+=" "
                    temp+=secondName[0]
                except:
                    print("Error finding display name")
                    temp="?"
                else:

                    subPupilMenu.add_command(
                label=temp,command=lambda showArray=mainPupilArray
                : showPupil(showArray))

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
    print("Saving",array)
    global newOrderPupils
    try:
        pupilData=array[0]
        pupilPB=array[1]
    except:
        askError("Format","This pupil has format issues")
    else:
        if array not in newOrderPupils:
            newOrderPupils.append(array)
            try:
                file=open("pupils.txt","a")
            except:
                file=open("pupils.txt","w")

            file.write("=======================\n")
            for item in pupilData:
                file.write(item)
                file.write("\n")

            for item in pupilPB:
                file.write(item)
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
        oldInsertListbox(viewAllListbox, tempArray)

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
        oldInsertListbox(viewAllListbox, newOrderArray)

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
        oldInsertListbox(viewAllListbox, newOrderArray)




#Old format listox insersion
def oldInsertListbox(listbox,array):
    listbox.delete(0,END)
    for pupil in array:
        try:
            sub=pupil[0]
        except:
            print("Pupil format error old listbox")
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



            if grade in passGrades:

                pupilColour=passColour
            else:
                pupilColour=failColour

            listbox.insert(END,temp)
            listbox.itemconfig(END,bg=pupilColour)

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
            print("Pupil format error new listbox")
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

                    pupilColour=passColour
                else:
                    pupilColour=failColour


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
            dataSection=pupil[0]
        except:
            print("Pupil format error non delete")
        else:
            try:
                name=dataSection[0]
                second=dataSection[1]
                grade=dataSection[2]
            except:
                name="?"
                second="?"
                grade="?"

            temp=""
            temp+=name
            temp+=" "
            temp+=second



            if grade in passGrades:

                pupilColour=passColour
            else:
                pupilColour=failColour

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
        pupil=getPupilFromArray(words)
        try:
            data=pupil[0]
        except:
            print("Pupil format error preview")
        else:
            try:
                entrytoInsert=[previewName,previewSecond,previewGrade]
                for item in entrytoInsert:

                    item.config(state=NORMAL)
                    dataPos=entrytoInsert.index(item)
                    dataItem=data[dataPos]
                    insertEntry(item, dataItem)
                    if item == previewGrade:
                        grade=data[dataPos]
                        if grade not in passGrades:
                            item.config(fg="red")
                        else:
                            item.config(fg="black")
                    item.config(state=DISABLED)
            except:
                print("Error loading pupil preview")


def viewAllResultsStep():
    try:
        select=viewAllListbox.curselection()
    except:
        pass
    else:
        if len(select) > 0:
            viewallResults("")
        else:
            askMessage("Pupil","Please click pupil to load")

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
            print("Indexing error finding PB position")
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

#Function that adds current PB
def createAddPB():
    global currentCreatePupilPBArray
    global currentCreatePupil
    selectedArea=createPupilPersonalBestVar.get()
    textFromArray=createPupilTarget.get()
    #Works out match
    copyArray=mainPBOptions
    try:
        matchPos=copyArray.index(selectedArea)
    except:
        print("Error finding PB match array")
    else:
        try:
            currentCreatePupilPBArray[matchPos]=textFromArray
        except:
            print("Error updating PB")
        else:
            askMessage("Success","Added PB")

def checkData():
    text=createPupilTarget.get()
    words=text.split()
    if len(words) > 0:
        addNewPBButton.config(state=NORMAL)
    else:
        addNewPBButton.config(state=DISABLED)

def createPupilOptionMenuFunction(value):
    global currentCreatePupilPBArray
    checkData()
    #Value from OptionMenu if keystroke triggers function
    directValue=createPupilPersonalBestVar.get()
    textFromEntry=createPupilTarget.get()
    words=textFromEntry.split()
    if len(words) > 0:
        if value != "Select" and directValue != "Select":
            addNewPBButton.config(state=NORMAL)
    else:
        addNewPBButton.config(state=DISABLED)

    if value in mainPBOptions:
        #Works out match to diplay in Label
        try:
            match=mainPBOptions.index(value)
        except:
            print("Match finding error")
        else:
            try:
                currentItem=currentCreatePupilPBArray[match]
            except:
                print("Error occoured viewing current PB")
            else:

                if currentItem != ["Unknown?"]:
                    insertEntry(createPupilTarget,currentItem)
                else:
                    insertEntry(createPupilTarget,"")



#Function to order PB's into seperate arrays
#This new order array is used throughout rest of program
numberOfTrackers=0
def orderPB():
    global newOrderPupils
    global numberOfTrackers
    newOrderPupils=[]

    numberOfDataItems=4

    #COPYS THE pupil array
    copyArray=pupilDataArray
    trackNumber=0
    for pupil in copyArray:
        trackNumber+=1
        numberOfTrackers+=1

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


        #Adds track number
        temp=[]
        track=str(trackNumber)
        temp.append(track)

        newPupilOverall.append(newPupilData)
        newPupilOverall.append(newPupilPB)
        newPupilOverall.append(temp)

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
    try:
        temp=sorted(temp)
    except:
        print("Error sorting pupils for listbox")
    insertListbox(bulkAllPupilListbox,temp)

    #if button configs are needed
    alternateButtonConfig("Add")
    alternateButtonConfig("")
    try:
        addPBoptionsToBulkEditOptions()
    except:
        askError("Error","Option Menu error")





#Right click menu
def viewPupilPopup(event):
    data=currentViewCanvasArray[0]

    #Get sub groups
    viewPupilGroupMenu.delete(0,END)
    for item in groupNameArray:
        viewPupilGroupMenu.add_command(label=item,command=lambda x=item: addCertainPupilToGroup(x))
    #Only show menu on that canvas
    if data == viewPupilCanvas:
        viewPupilMiniMenu.post(event.x_root, event.y_root)

def showPupilTab(pupilToView):
    current=pupilToView

    try:
        data=current[0]
        pbArray=current[1]
    except:
        print("Error with pupil format")
    else:
        try:
            x=3
        except:
            pass
        else:
            #window setup
            newT=Tk()
            newWindow=Frame(newT)
            newWindow.pack(expand=True)
            newT.maxsize(450,650)
            newT.minsize(300,350)
            newT.geometry("350x350")
            Label(newWindow,text="Name:").grid(row=0,column=0)
            Label(newWindow,text="Second:").grid(row=1,column=0)
            Label(newWindow,text="Grade:").grid(row=2,column=0)


            newWindowName=Entry(newWindow)
            newWindowName.grid(row=0,column=1)

            newWindowSecond=Entry(newWindow)
            newWindowSecond.grid(row=1,column=1)

            newWindowGrade=Entry(newWindow)
            newWindowGrade.grid(row=2,column=1)



            matchArray=mainPBOptions
            position=2
            for item in pbArray:
                position+=1
                pos=pbArray.index(item)
                match=matchArray[pos]
                temp=match
                temp+=":"
                Label(newWindow,text=temp).grid(row=position,column=0)

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
                displayArray=[newWindowName,newWindowSecond,newWindowGrade]
                for item in data:

                    pos=data.index(item)
                    if pos != 3:
                        match=displayArray[pos]
                        match.delete(0,END)
                        try:
                            match.insert(END,item)
                        except:
                            match.insert("1.0",END)



            position+=1
            Label(newWindow,text="Notes:").grid(row=position,column=0)
            newNotes=Text(newWindow,height=5,width=15,wrap=WORD,font=("Helvetica", "11"))

            if version == "Windows":
                newNotes=Text(newWindow,height=5,width=15,wrap=WORD,font=("Helvetica", "11"))

            else:
                if version == "Darwin":
                    newNotes=Text(newWindow,font=("Helvetica", "12"),height=5,width=24,wrap=WORD)
                if version == "Linux":
                    newNotes=Text(newWindow,font=("Helvetica", "12"),height=5,width=18,wrap=WORD)


            newNotes.grid(row=position,column=1)

            try:
                notes=data[3]
            except:
                pass
            else:
                newNotes.insert(END,notes)


            #Sets up window colour

            colour=random.choice(colourArray)
            newWindow.config(bg=colour)
            newT.config(bg=colour)
            widgetArray=["Label"]
            for item in newWindow.winfo_children():
                if item.winfo_class() in widgetArray:
                    item.config(bg=colour)

                try:
                    item.config(highlightbackground=colour)
                except:
                    print("Widget error")





#Function that gets pupil from array
def getPupilFromArray(wordArray):
    words=wordArray
    valid1=False
    valid2=False
    for pupil in newOrderPupils:
        valid1=False
        valid2=False
        try:
            data=pupil[0]
        except:
            print("Pupil format error from array")
        else:

            if data[0] == words[0]:
                valid1=True
            if data[1] == words[1]:
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
    addBulkPupil()
    alternateButtonConfig("Add")



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
        removeListbox(bulkAllPupilListbox,removeArray)

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
    sortListbox(bulkAllPupilListbox)

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
    removeListbox(bulkFilterPupilListbox,removeArray)

#Function to check len of listboxes each button press
#Then based on length of lisbox config buttons
def alternateButtonConfig(addOrRemove):
    size=bulkAllPupilListbox.size()
    if size  < 1:
        addBulkPupilButton.config(state=DISABLED)
        addAllBulkPupilsButton.config(state=DISABLED)
    else:
        try:
            currentSelect=bulkAllPupilListbox.curselection()
        except:
            pass
        else:
            addAllBulkPupilsButton.config(state=NORMAL)
            if len(currentSelect) > 0:
                addBulkPupilButton.config(state=NORMAL)

            else:
                addBulkPupilButton.config(state=DISABLED)


    #Alternate butons
    size2=bulkFilterPupilListbox.size()
    if size2 > 0:
        removeBulkPupilButton.config(state=NORMAL)


    size=bulkFilterPupilListbox.size()
    if size < 1:
        removeBulkPupilButton.config(state=DISABLED)
        removeAllBulkPupilsButton.config(state=DISABLED)
    else:
        try:
            currentSelect=bulkFilterPupilListbox.curselection()
        except:
            pass
        else:
            removeAllBulkPupilsButton.config(state=NORMAL)

            if len(currentSelect) > 0:
                removeBulkPupilButton.config(state=NORMAL)
            else:
                removeBulkPupilButton.config(state=DISABLED)



def preAddAllBulkPupils():
    addAllBulkPupils()
    alternateButtonConfig("Add")
    sortListbox(bulkAllPupilListbox)


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
    sortListbox(bulkAllPupilListbox)
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
    temp="Would you like to overwrite these pupils"
    try:
        leng=bulkFilterPupilListbox.size()
        copyLeng=str(leng)
    except:
        print("Size Error")
    else:
        temp="Would you like to overwrite these "
        temp+=copyLeng
        temp+=" pupils"

    if leng > 0:
        contentFromEntry=bulkChangeEntry.get()
        words=contentFromEntry.split()
        if len(words) < 1:
            askMessage("Content","Please enter a value to change to")
        else:
            try:
                choice=messagebox.askyesno("Overwrite",temp)
            except:
                print("Feature not supported on:",version)
            else:
                if choice == True:
                    try:
                        submitBulkEdit()
                    except:
                        askError("Error","There was a problem editing the pupils")


    else:
        askMessage("Pupils","Please load some pupils")

def submitBulkEdit():
    field=bulkEditOptionVar.get()
    text=bulkChangeEntry.get()

    #arrays
    matchArray=mainPBOptions
    #Retrivse pupil info
    data=bulkFilterPupilListbox.get(0,END)

    #Change Grade
    if field == "Grade":
        numberPos="0 2"
    else:
        matchArray=mainPBOptions
        for item in matchArray:
            numberPos=""
            if item == field:
                index=matchArray.index(item)
                index=str(index)
                numberPos="1 "
                numberPos+=index
                break

    #The first number represents what array and second the position in array
    print("Using",numberPos,"as position")
    numberPos=numberPos.split()
    try:
        mainSectionIndex=numberPos[0]
        subSectionIndex=numberPos[1]
        mainSectionIndex=int(mainSectionIndex)
        subSectionIndex=int(subSectionIndex)
    except:
        print("Error indexing array positions")
    else:
        #Uses numberPos in pupils format

        #Changes all the selected pupils
        for item in data:
            words=item.split()
            pupil=getPupilFromArray(words)
            try:
                mainSection=pupil[mainSectionIndex]
            except:
                print("Error with pupil format")
            else:
                try:
                    subSection=mainSection[subSectionIndex]
                except:
                    print("The value does not exist")
                else:
                    mainSection[subSectionIndex]=text
        removeAllBulkPupils()

        #Save the new data to file
        saveNewPupils(newOrderPupils)






def unlockBulkOptions(event):
    content=bulkChangeEntry.get()
    words=content.split()
    if len(content) < 1:
        submitBulkEditButton.config(state=DISABLED)
    else:
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
            print("Pupil format error new array")
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
                try:
                    current=bulkAllPupilListbox.curselection()
                    if len(current) > 1:
                        bulkViewMiniMenu.entryconfig(0,label="View Pupils In Tabs")
                    else:
                        bulkViewMiniMenu.entryconfig(0,label="View Pupil")
                except:
                    pass
                bulkViewMiniMenu.post(event.x_root, event.y_root)
    elif listbox == "Remove":
        try:
            pos=bulkFilterPupilListbox.curselection()
        except:
            pass
        else:

            #This line stops the pop up menu if nothing is selected
            if len(pos) > 0:
                try:
                    current=bulkFilterPupilListbox.curselection()
                    if len(current) > 1:
                        filterViewMiniMenu.entryconfig(0,label="View Pupils In Tabs")
                    else:
                        filterViewMiniMenu.entryconfig(0,label="View Pupil")
                except:
                    pass

                #Adds items to array
                filterViewCascade.delete(0,END)
                for item in groupNameArray:
                    filterViewCascade.add_command(label=item,command=lambda listbox=bulkFilterPupilListbox, group=item: preAddGroupPupils(listbox,group))
                filterViewMiniMenu.post(event.x_root, event.y_root)

def preAddGroupPupils(listbox,group):
    try:
        indexes=listbox.get(0,END)
    except:
        print("No Listbox passed to function")
    else:
        trackArray=[]
        for item in indexes:
            try:
                words=item.split()
                pupil=getPupilFromArray(words)
                if pupil != None:
                    trackArray.append(pupil)
            except:
                print("Pupil error")

        addArrayToGroup(trackArray,group)

def toggleStatus():
    statusCol=status.cget("fg")
    statusCol.capitalize()
    if statusCol == "White" or statusCol == "white":
        status.config(fg="Black")
    else:
        status.config(fg="White")



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
        #removeAllBulkPupilsButton.config(state=DISABLED)
        removeBulkPupilButton.config(state=DISABLED)

def bulkDisableFilter(event):
    leng=bulkFilterPupilListbox.size()
    if leng > 0:
        addBulkPupilButton.config(state=DISABLED)
        removeAllBulkPupilsButton.config(state=NORMAL)
        removeBulkPupilButton.config(state=NORMAL)


def checkPBSame(currentPB):
    same=True
    currentOption=chosenPeronalBestToView.get()
    if currentOption != "Select PB":
        try:
            currentPBSecton=currentViewPupil[1]
        except:
            print("Pupil format error")
        else:
            try:
                matchPos=mainPBOptions.index(currentOption)
            except:
                print("Indexing error finding PB index")
            else:
                try:
                    match=currentPBSecton[matchPos]
                except:
                    print("Second index error")
                else:
                    if currentPB == match:
                        same=True
                    else:
                        same=False
    if same == True:
        return True
    else:
        return currentPB

def startNewFilterGroup():
    pupils=bulkFilterPupilListbox.get(0,END)
    newGroup(pupils)


def addPBoptionsToBulkEditOptions():
    global bulkEditOptionArray
    bulkEditOptionArray=[]
    copy=mainPBOptions
    bulkEditOptionArray.append("Grade")
    for item in copy:
        bulkEditOptionArray.append(item)

def checkGrades():
    passes=0
    fails=0
    matchArray=["A*","A","B","C","D","E","F"]
    for pupil in newOrderPupils:
        try:
            data=pupil[0]
        except:
            print("Pupil format error")
        else:
            try:
                grade=data[2]

            except:
                print("Indexing error")
            else:
                try:
                    pos=matchArray.index(grade)
                except:
                    pos=50
                else:
                    if pos <= 3:
                        passes+=1
                    else:
                        fails+=1

    passes=str(passes)
    fails=str(fails)
    passVar.set(passes)
    failVar.set(fails)



def newGroup(pupils):
    global groupPupilArray
    global mainGroupName
    groupPupilArray=pupils

    groupListbox.delete(0,END)

    #Load window
    loadCanvas(newGroupCanvas,"New Group")

    #Alphabetcly orders pupils
    pupils=sorted(pupils)

    #Tracks full users
    pupilArray=[]

    for item in pupils:
        words=item.split()
        pupil=getPupilFromArray(words)
        pupilArray.append(pupil)

    insertListbox(groupListbox,pupilArray)



def newFilterGroup():
    pupils=filterResults.get(0,END)
    newGroup(pupils)

#Organisees listbox into alphabetic order
def sortListbox(listbox):

    temp=[]
    content=listbox.get(0,END)
    for item in content:
        words=item.split()
        pupil=getPupilFromArray(words)
        temp.append(pupil)

    temp=sorted(temp)
    listbox.delete(0,END)
    insertListbox(bulkAllPupilListbox,temp)

#Moves serarch results to bulk edit
def addFilterToBulk():
    addArrayToBulkEdit(filterResults)




def removeListbox(listbox,removeArray):
    miniCounter=-1
    for item in removeArray:
        miniCounter+=1
        if miniCounter != 0:

            try:
                item=int(item)
                pos=item-miniCounter
            except:
                print("Pupil format error in remove listbox")
                break

        else:
            pos=item
        try:
            listbox.delete(pos)
        except:
            print("Error removing pupil from listbox")


def submitNewGroup():
    global mainGroupName
    global groupNameArray
    global groupOrderArray

    groupName=groupNameEntry.get()

    words=groupName.split()
    temp=""
    for item in words:
        copy=item.capitalize()
        temp+=copy
        temp+=" "

    groupName=temp

    mainGroupName=groupName
    words=groupName.split()

    pupilTuple=groupListbox.get(0,END)

    pupilsToAdd=[]
    for item in pupilTuple:
        pupilsToAdd.append(item)

    lengOfPupils=len(pupilsToAdd)

    #Capitalizes group name
    words=groupName.split()
    groupName=""
    for item in words:
        item=item.capitalize()
        groupName+=item
        groupName+=" "

    groupName=groupName.rstrip()
    valid=False
    if len(words) > 0:
        if groupName not in groupNameArray:
            if lengOfPupils  < 1:
                try:
                    option=messagebox.askyesno("Empty","Would you like to create an empty group?")
                except:
                    askMessage("Tkinter","Feature Not Supported")
                else:
                    if option == True:
                        valid=True
            else:
                valid=True       
                
  
            if valid == True:              
                groupPupils=pupilsToAdd
                groupPupils=sorted(groupPupils)

                #Save to file
                saveGroupToFile(groupPupils)
                groupNameArray.append(groupName)


                #Adds to the main group array
                mainAddArray=[]
                temp=[groupName]
                mainAddArray.append(temp)
                mainAddArray.append(groupPupils)

                groupOrderArray.append(mainAddArray)

                afterAddedGroups.append(mainAddArray)

                updateGroupMenu()
                askMessage("Complete","Saved New group")

        else:
            askMessage("Duplicate","This group allready exists")

    else:
        askMessage("Name","Please enter a group name")


def checkBulkEntry(event):
    content=bulkChangeEntry.get()
    words=content.split()
    if len(words) < 1:
        submitBulkEditButton.config(state=DISABLED)
    else:
        option=bulkEditOptionVar.get()
        if option != "Select field":
            submitBulkEditButton.config(state=NORMAL)



def submitBulkDelete():
    removeArray=[]
    size=bulkFilterPupilListbox.size()
    if size < 1:
        askMessage("Pupils","Please load pupils to delete first")
    else:
        try:
            choice=messagebox.askyesno("Delete","Are you sure you want to delete these pupils?")
        except:
            askMessage("Error","This function is not supported on this OS")
        else:
            if choice == True:
                global newOrderPupils
                content=bulkFilterPupilListbox.get(0,END)
                pupilArray=[]
                track=-1
                for item in content:
                    track+=1
                    removeArray.append(track)
                    words=item.split()
                    pupil=getPupilFromArray(words)
                    pupilArray.append(pupil)

                for pupil in pupilArray:
                    try:
                        newOrderPupils.remove(pupil)
                        deletedPupils.append(pupil)
                    except:
                        print("Could not find pupil to delete")


                #Removes pupil from bulk listbox
                print(removeArray)
                removeListbox(bulkFilterPupilListbox,removeArray)
                saveNewPupils(newOrderPupils)



def deletePupilFromMenu():
    deletePupilStep()

def saveGroupToFile(array):
    groupName=mainGroupName

    lineAray=[]
    try:
        fileOpen=open("groups.txt","a")
    except:
        print("No group file creating new one")
        fileOpen=open("groups.txt","w")
        fileOpen.write("==============================\n")
        fileOpen.write("GroupName123: ")
        fileOpen.write(groupName)
        fileOpen.write("\n")

        #Save pupils
        for pupil in array:
            words=pupil.split()
            try:
                first=words[0]
                second=words[1]
            except:
                print("File writing error")
            else:
                fileOpen.write(first)
                fileOpen.write(" ")
                fileOpen.write(second)
                fileOpen.write("\n")

        fileOpen.close()

    #If the file does exist overwrite it
    else:
        fileOpen.write("==============================\n")
        fileOpen.write("GroupName123: ")
        fileOpen.write(groupName)
        fileOpen.write("\n")

        #Save pupils
        for pupil in array:
            words=pupil.split()
            try:
                first=words[0]
                second=words[1]
            except:
                print("File writing error")
            else:
                fileOpen.write(first)
                fileOpen.write(" ")
                fileOpen.write(second)
                fileOpen.write("\n")

        fileOpen.close()

def getGroupsFromFile():

    overAllArray=[]

    content=getReadLines("groups.txt")
    if content != None:
        print()
        print("=====Starting group retrival======")
        groupCounter=0
        lineCounter=-1

        for line in content:
            lineCounter+=1
            if line == "==============================\n":
                currentGroupArray=[]

                groupCounter+=1
                try:
                    nameLine=content[lineCounter+1]
                except:
                    pass
                else:
                    words=nameLine.split()
                    try:
                        leng=len(words)
                        temp=""
                        for x in range(1,leng):
                            current=words[x]
                            try:
                                current=current.capitalize()
                            except:
                                print("Capital error")
                            temp+=current
                            temp+=" "
                        groupName=temp
                        groupName=groupName.rstrip()
                    except:
                        pass
                        groupName="???"
                    else:
                        print("Found group of name",groupName)
                        temp=[groupName]
                        currentGroupArray.append(temp)


                        currentPupils=[]
                        for x in range(lineCounter+2,len(content)):
                            try:
                                current=content[x]
                                current=current.rstrip()
                            except:
                                print("Indexing error")
                            else:
                                if current != "==============================":
                                    currentPupils.append(current)
                                else:
                                    #New group has been found
                                    break

                        #Adds pupils
                        currentPupils=sorted(currentPupils)
                        currentGroupArray.append(currentPupils)

                overAllArray.append(currentGroupArray)

        overAllArray=sorted(overAllArray)
        return overAllArray

def themeOrBackgroundUpdate(themeOrBackground):
    if themeOrBackground == "Background":
        cursor=colourListBox.curselection()
        try:
            data=colourListBox.get(cursor)
        except:
            print("Error getting data from theme listbox")

    elif themeOrBackground == "Theme":
        cursor=backgroundListBox.curselection()
        try:
            data=backgroundListBox.get(cursor)
        except:
            print("Error getting data from background listbox")


def showHomeMiniMenu(event):

    #Check if current is home screen
    try:
        currentCanvas=currentViewCanvasArray[0]
    except:
        currentCanvas="?"
    else:
        if currentCanvas == openCanvas:
            homeScreenMiniMenu.entryconfig(0,state=DISABLED)
        else:
            homeScreenMiniMenu.entryconfig(0,state=NORMAL)

    homeScreenMiniMenu.post(event.x_root, event.y_root)

def preOpenCanvas(event):
    showOpenCanvas()



#====================================================BINDING FUNCTIONS============
def bindHoverIn(widget):

    #Checks if text will be same as background colour
    backgroundColour=mainBackgroundColour.get()
    theme=mainThemeColour.get()
    if theme != backgroundColour:
        try:
            widget.config(fg=mainThemeColour.get())
        except:
            print("Error changing widget colour")
    else:
        try:
            widget.config(fg="black")
        except:
            print("Error changing widget colour")


def bindHoverOut(widget):
    try:
        widget.config(fg=mainLabelTextColour)
    except:
        print("Error changing widget")


def bindArray(array):
    for item in array:
        item.bind("<Enter>",lambda event, widget=item:bindHoverIn(widget) )
        item.bind("<Leave>",lambda event, widget=item: bindHoverOut(widget))

def checkFailBinding(event):
    fails=failVar.get()
    passes=passVar.get()
    try:
        fails=int(fails)
        passes=int(passes)
    except:
        pass
    else:
        if fails > passes:
            status.config(bg=failColour)
            statusVar.set("Majority of pupils below C")
        elif fails < passes:
            status.config(bg=passColour)
            statusVar.set("Majority of pupils C or above")
        else:
            status.config(bg="gold")
            statusVar.set("Same amount of pupils below and above C")

def normalStatusBind(widget):
    status.config(bg=mainThemeColour.get())
    statusVar.set(currentCanvasMessage.get())
    changeNumberColour(widget)

def changeNumberColour(widget):
    widget.config(fg=mainLabelTextColour)

def bindLabelArray():
    array=[showNumberLabel,showPassNumberLabel,showFailNumber]
    for item in array:
        try:
            if item == showNumberLabel:
                item.bind("<Button-1>",checkFailBinding)
            item.bind("<Leave>",lambda event, widget=item :normalStatusBind(widget))
        except:
            print("Binding error")



def statusHoverIn(event):
    try:
        current=currentViewCanvasArray[0]
    except:
        pass
    else:
        if current != openCanvas:
            statusVar.set("Double Click To Go Home")

def statusHoverOut(event):
    statusVar.set(currentCanvasMessage.get())

#Functions that launch when double click home screen widgets
def preUserName(event):
    changeUserName()

def preViewAll(event):
    showAllPupils()

#Functions for single click home screen widgets
def viewPassStatus(event):
    passes=passVar.get()
    temp="Currently there are "
    temp+=passes
    temp+=" pupils C grade and above"
    statusVar.set(temp)
def viewFailStatus(event):
    fails=failVar.get()
    temp="Currently there are "
    temp+=fails
    temp+=" pupils below grade C"
    statusVar.set(temp)

def sortPasses(event):
    askMessage("Not ready","This function is coming soon")
def sortFails(event):
    askMessage("Not ready","This function is coming soon")

def initNewGroups():
    global groupOrderArray
    global groupNameArray
    if groupOrderArray != None and groupOrderArray != "":
        leng=len(groupOrderArray)
        if leng > 0:
            for group in groupOrderArray:
                try:
                    name=group[0]
                    pupils=group[1]
                except:
                    print("Indexing error")
                else:
                    #Name section
                    try:
                        groupName=name[0]
                    except:
                        print("Name error")
                    else:
                        valid=True
                        if groupName not in groupNameArray:
                            groupNameArray.append(groupName)


                        else:
                            print("Stopped duplicate")
                            valid=False

                    #Add to menu bar
                    if valid == True:
                        addGroupMenuBar(groupName,pupils)

#Adds new groups to menu bar
def addGroupMenuBar(name,pupils):
    groupMenu.add_command(
label=name,command=lambda  showName= name ,showArray=pupils
: showGroup(showName,showArray))


#Shows group on screen
showMessage=True
def showGroup(name,pupils):
    global showMessage
    loadCanvas(showGroupCanvas,"Viewing Group")
    showGroupLabelVar.set(name)
    corrupt=False
    #Gets actual pupil infomation
    realArray=[]
    corruptArray=[]

    for pupil in pupils:
        words=pupil.split()
        actual=getPupilFromArray(words)
        if actual != None and actual != "":
            realArray.append(actual)
        else:
            corruptArray.append(pupil)
            corrupt=True
    insertGroupListbox(pupils)
    if corrupt == True:

        #Asks to overwrite old pupils
        if showMessage == True:
            try:
                option=messagebox.askyesno("Overwrite","Would you like to remove pupils no longer in this group")
            except:
                askMessage("Tkinter","Error with Python feature not supported")
            else:
                if option == True:
                    showMessage=False
                    overwriteGroup()




def insertGroupListbox(array):
    showGroupListbox.delete(0,END)
    array=sorted(array)
    for pupil in array:
        words=pupil.split()
        real=getPupilFromArray(words)
        if real != None:
            try:
                data=real[0]
            except:
                print("Format error")
            else:
                grade=data[2]
                grade=str(grade)
                grade=grade.capitalize()
                passGrades=["A*","A","B","C"]

                try:
                    name=data[0]
                    second=data[1]
                except:
                    print("Name error")
                else:
                    temp=""
                    temp+=name
                    temp+=" "
                    temp+=second

                    #add to listbox
                    showGroupListbox.insert(END,temp)
                    if grade in passGrades:
                        showGroupListbox.itemconfig(END,bg=passColour)
                    else:
                        showGroupListbox.itemconfig(END,bg=failColour)


def overwriteGroup():
    global groupOrderArray
    print()
    print("================Overwriting Group==========")

    #Gets fields to overwrite
    overwriteName=showGroupLabelVar.get()
    overwritePupils=showGroupListbox.get(0,END)
    overwriePupilArray=[]

    #Converts pupils into array format
    for pupil in overwritePupils:
        overwriePupilArray.append(pupil)

    sameData=False


    #Check if data has been changed
    for section in groupOrderArray:
        try:
            nameSection=section[0]
            pupilSection=section[1]
            groupName=nameSection[0]

        except:
            print("Error with group format before")
        else:
            if groupName == overwriteName:

                if pupilSection == overwriePupilArray:
                    sameData=True

    if sameData == True:
        askMessage("Same","The Data has not been changed")
    else:

        #Makes changes
        found=False
        for section in groupOrderArray:
            try:
                nameSection=section[0]
                pupilSection=section[1]

                groupName=nameSection[0]
            except:
                print("Error with group format while changing")
            else:

                if groupName == overwriteName:
                    found=True
                    section[1]=overwriePupilArray
                    print("Changed with",overwritePupils)
                    break
                else:
                    print(groupName,"vs",overwriteName)



        if found == True:
            #Saves the new array here
            actualOverWriteGroup()
        else:
            askMessage("Found","Data could not be changed")

def actualOverWriteGroup():
    success=True
    try:
        file=open("groups.txt","w")
    except:
        askError("Error","An Error occoured opening file")
    else:
        for group in groupOrderArray:
            file.write("==============================\n")
            try:
                nameSection=group[0]
                pupilSection=group[1]

                groupName=nameSection[0]
            except:
                print("Format error")
                success=False
            else:
                temp="GroupName123: "
                temp+=groupName
                file.write(temp)
                file.write("\n")

                #Add pupils
                for pupil in pupilSection:
                    file.write(pupil)
                    file.write("\n")
        file.close()
        if success == True:
            try:
                current=currentViewCanvasArray[0]
            except:
                pass
            else:
                if current == showGroupCanvas:
                    askMessage("Success","Overwrite success")
        else:
            askMessage("Error","Group was not changed")



def showHelp():
    openLink("https://drive.google.com/folderview?id=0B_HDzRT6N--LUzVzMTlPN2ZwTEU&usp=sharing")


def showWebsite():
    openLink("http://angusgoody.wix.com/pipossy#!peter/bge9x")


def openLink(link):
    try:
        temp="Are you sure you want to load this link"
        option=messagebox.askyesno("Sure",temp)
    except:
        askError("Error","Error launching link")
    else:
        if option == True:
            try:
                webbrowser.open_new(link)
            except:
                askError("Error","Error opening link")

def removeGroupPupil():
    pupil=showGroupListbox.curselection()
    removeListbox(showGroupListbox,pupil)

def deleteGroup():
    global groupOrderArray
    print("===========Delete Group========")

    try:
        option=messagebox.askyesno("Sure","Are you sure you want to delete group?")
    except:
        askMessage("Python","Python module error")
    else:
        found=False
        if option == True:
            overwriteName=showGroupLabelVar.get()
            success=True

            #Removes group from array and then saves data
            counter=-1
            for item in groupOrderArray:
                counter+=1
                try:
                    groupNameSection=item[0]
                    groupName=groupNameSection[0]
                except:
                    print("Group Format error")
                else:
                    if groupName == overwriteName:
                        found=True
                        try:
                            groupOrderArray.remove(item)
                        except:
                            success=False
                        else:

                            #Saving new data bit
                            actualOverWriteGroup()

                            #Remove from menu bar
                            try:
                                groupNameArray.remove(groupName)
                            except:
                                print("Could not delete group from array")

                            updateGroupMenu()

                            showOpenCanvas()

            if found == False:
                askMessage("Can not find","Group cannot be deleted")


def addCertainPupilToGroup(name):

    print(name)
    try:
        data=currentViewPupil[0]
    except:
        print("Format error")
    else:
        temp=""
        try:
            pupilName=data[0]
            second=data[1]
        except:
            print("Indexing error")
        else:
            temp+=pupilName
            temp+=" "
            temp+=second

            for item in groupOrderArray:
                try:
                    nameSection=item[0]
                    pupilSection=item[1]

                    groupName=nameSection[0]
                except:
                    print("Error indexing")
                else:
                    if groupName == name:
                        if temp not in pupilSection:
                            pupilSection.append(temp)
                            actualOverWriteGroup()
                            askMessage("Success","New pupil added to group")
                        else:
                            askMessage("Duplicate","This pupil is allready in this group")
                    else:
                        print(groupName,"vs",name)

def preSubmitNewGroup(event):
    submitNewGroup()

def preOpenNewPupilTab():
    showPupilTab(currentViewPupil)

def viewBulkPupil(listbox):
    try:
        current=listbox.curselection()
    except:
        print("Error with listbox")
    else:
        if len(current) == 1:
            loadDoubleClick(listbox)
        else:
            leng=len(current)
            if leng > 20:
                askMessage("Too Many","No more than 20 pupils can be opened at once")
            else:
                try:
                    temp="Would you like to open these "
                    leng=len(current)
                    leng=str(leng)
                    temp+=leng
                    temp+=" pupils in new tabs"
                    option=messagebox.askyesno("Open",temp)
                except:
                    askMessage("Error","Python Tkinter Error")
                else:
                    if option == True:
                        for item in current:
                            try:
                                viewPupil=listbox.get(item)
                                words=viewPupil.split()
                                pupil=getPupilFromArray(words)
                                if pupil != None:
                                    showPupilTab(pupil)
                            except:
                                print("Error loading pupil tab")
def addArrayToGroup(array,group):

    addCounter=0
    for item in array:
        try:
            dataSection=item[0]
        except:
            print("Error formating pupil")
        else:
            try:
                temp=""
                temp+=dataSection[0]
                temp+=" "
                temp+=dataSection[1]
            except:
                print("Name could not be found")
            else:
                #Add to group array
                for section in groupOrderArray:
                    try:
                        nameSection=section[0]
                        pupilSection=section[1]

                        groupName=nameSection[0]
                    except:
                        print("Formatting error")
                    else:
                        if groupName == group:
                            if temp not in pupilSection:
                                pupilSection.append(temp)
                                addCounter+=1
                            else:
                                print("Pupil allready in group")


    leng=len(array)
    copy=addCounter
    copy=str(copy)
    leng=str(leng)

    temp="Added "
    temp+=copy
    temp+=" pupils out of "
    temp+=leng
    temp+=" to group"
    askMessage("Success",temp)

    #Saves the new groups to file
    actualOverWriteGroup()


def changeSelectType(event):
    matchArray=["browse",'extended','multiple']
    bulkAllPupilListbox.selection_clear(0, END)
    bulkFilterPupilListbox.selection_clear(0, END)
    try:
        index=selectTypeOptions.index(event)
    except:
        print("Error changing")
    else:
        try:
            match=matchArray[index]
        except:
            print("Index error")
        else:
            bulkAllPupilListbox.config(selectmode=match)
            bulkFilterPupilListbox.config(selectmode=match)


def addGroupToBulk():
    addArrayToBulkEdit(showGroupListbox)

#New function to add items to filter bulk listbox and add remove them from view all bulk listbox
def addArrayToBulkEdit(listbox):
    try:
        content=listbox.get(0,END)
    except:
        print("No listbox function")
    else:

        #Clears the space
        removeAllBulkPupils()

        bulkAllContent=bulkAllPupilListbox.get(0,END)
        miniCounter=0

        removeArray=[]
        for item in bulkAllContent:
            if item in content:
                removeArray.append(miniCounter)
            miniCounter+=1

        removeListbox(bulkAllPupilListbox,removeArray)

        #Get pupils from search results
        pupilsToAdd=[]
        for item in content:
            words=item.split()
            pupil=getPupilFromArray(words)
            pupilsToAdd.append(pupil)

        #Adds to bulk menu
        insertListbox(bulkFilterPupilListbox,pupilsToAdd)

        #Show bulk canvas
        loadBulkEdit()

def updateGroupMenu():
    global groupOrderArray
    groupMenu.delete(3,END)
    copy=sorted(groupOrderArray)
    for item in copy:
        try:
            nameSection=item[0]
            name=nameSection[0]
            pupilSection=item[1]
        except:
            print("Group Format Error")
        else:
            addGroupMenuBar(name,pupilSection)


def removePupilNewGroup():
    try:
        currentPos=groupListbox.curselection()
    except:
        print("Listbox error")
    else:
        removeListbox(groupListbox,currentPos)


def postMenu(event,listbox,menu):
    try:
        current=listbox.curselection()
    except:
        print("Listbox error")
    else:
        if len(current) > 0:
            menu.post(event.x_root, event.y_root)

def clearGroupEntry():
    groupListbox.delete(0,END)
#====================================================END OF BINDING FUNCTIONS============


#####################################ADD NEW FUNCTIONS UNDER HERE##################








#####################################ADD NEW FUNCTIONS ABOVE HERE##################
#Add cascades and commands=====================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)
mainMenu.add_cascade(label="Pupils",menu=pupilMenu)
mainMenu.add_cascade(label="Filter",menu=filterMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="Groups",menu=groupMenu)
mainMenu.add_cascade(label="Help",menu=helpMenu)

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

#Help Menus
helpMenu.add_command(label="Help Guides",command=showHelp)
helpMenu.add_command(label="Website",command=showWebsite)


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
#Updates optionMenu
addPBoptionsToBulkEditOptions()
bulkEditOptionMenu=OptionMenu(secondBulkFrame,bulkEditOptionVar,*bulkEditOptionArray,command=unlockBulkOptions)
bulkEditOptionMenu.grid(row=0,column=1)


#Config for option Menus
if version != "Darwin" and version != "Windows":
    showPupilPersonalBestOptions.config(width=15)
    createPupilPersonalBestOption.config(width=15)

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

deleteBulkButton=Button(secondBulkFrame,text="Delete Selected",width=15,relief=FLAT,command=submitBulkDelete)
deleteBulkButton.grid(row=3,column=1,pady=3)

#Buttons for Groups
submitGroupButton=Button(newGroupCanvas,text="Create",command=submitNewGroup,relief=FLAT,width=12)
submitGroupButton.grid(row=1,column=1,pady=5)

overwriteGroupButton=Button(showGroupCanvas,text="Save",command=overwriteGroup,relief=FLAT,width=12)
overwriteGroupButton.grid(row=2,column=1,pady=5)

deleteGroupButton=Button(showGroupCanvas,text="Delete Group",command=deleteGroup,relief=FLAT,width=12)
deleteGroupButton.grid(row=3,column=1,pady=5)

clearGroupEntryButton=Button(newGroupCanvas,text="Clear",command=clearGroupEntry,relief=FLAT,width=12)
clearGroupEntryButton.grid(row=3,column=1,pady=5)
#=============Checkbuttons==========

#OptionMenu for bulk selection type
selectTypeOptions=["Normal","Drag","Multi"]
selectTypeVar=StringVar()
selectTypeVar.set("Select")
selectTypeOptionMenu=OptionMenu(mainListboxFrame,selectTypeVar,*selectTypeOptions,command=changeSelectType)
if version == "Darwin":
    selectTypeOptionMenu.config(width=12)
else:
    selectTypeOptionMenu.config(width=7)
selectTypeOptionMenu.pack(pady=12)



#Right click Menus---------------

#Menu for view pupil
viewPupilMiniMenu = Menu(currentViewPupil, tearoff=0)
viewPupilMiniMenu.add_command(label="Open pupil in new tab",command=preOpenNewPupilTab)
viewPupilMiniMenu.add_separator()

#Cascade menu
viewPupilGroupMenu=Menu(viewPupilMiniMenu)
viewPupilMiniMenu.add_cascade(label="Add To Group",menu=viewPupilGroupMenu)
viewPupilMiniMenu.add_separator()
viewPupilMiniMenu.add_command(label="Toggle text position",command=toggleTextPos)
viewPupilMiniMenu.add_separator()
viewPupilMiniMenu.add_command(label="Delete Pupil",command=deletePupilFromMenu)



#Bulk edit listboxes add mini menu
bulkViewMiniMenu=Menu(bulkEditCanvas,tearoff=0)
bulkViewMiniMenu.add_command(label="View Pupil",command=lambda :viewBulkPupil(bulkAllPupilListbox))
bulkViewMiniMenu.add_separator()
bulkViewMiniMenu.add_command(label="Add Pupil",command=preAddBulkPupil)
bulkViewMiniMenu.add_command(label="Add All",command=addAllBulkPupils)

#Bulk edit listboxes remove mini menu
filterViewMiniMenu=Menu(bulkEditCanvas,tearoff=0)
filterViewMiniMenu.add_command(label="View Pupil",command=lambda :viewBulkPupil(bulkFilterPupilListbox))
filterViewMiniMenu.add_separator()
filterViewMiniMenu.add_command(label="Remove Pupil",command=preRemoveBulkPupil)
filterViewMiniMenu.add_command(label="Remove All",command=removeAllBulkPupils)
filterViewMiniMenu.add_separator()
filterViewMiniMenu.add_command(label="New Group",command=startNewFilterGroup)
filterViewCascade=Menu(filterViewMiniMenu)
filterViewMiniMenu.add_cascade(label="Add To Group",menu=filterViewCascade)

#Filter mini menus
filterPupilsMiniMenu=Menu(filterPupilCanvas,tearoff=0)
filterPupilsMiniMenu.add_command(label="View Pupil",command=preViewFilterResults)
filterPupilsMiniMenu.add_separator()
filterPupilsMiniMenu.add_command(label="New Group",command=newFilterGroup)
filterPupilsMiniMenu.add_command(label="Edit All",command=addFilterToBulk)

#Change theme mini menu
themeMiniMenu=Menu(changeThemeCanvas,tearoff=0)
themeMiniMenu.add_command(label="Change Theme",command=updateThemeStep)

#Change background mini menu
backgroundMiniMenu=Menu(changeBackgroundCanvas,tearoff=0)
backgroundMiniMenu.add_command(label="Change Background",command=updateBackgroundStep)

#Home screen mini menu
homeScreenMiniMenu=Menu(openCanvas,tearoff=0)

#Create Group Mini meun
createGroupMiniMenu=Menu(groupListbox)
createGroupMiniMenu.add_command(label="Remove Pupil",command=removePupilNewGroup)


#Sub menu of homescreen
personalMenu=Menu(homeScreenMiniMenu)
personalMenu.add_command(label="Change Info",command=changeUserName)
personalMenu.add_command(label="Change Theme",command=changeTheme)
personalMenu.add_command(label="Change Background",command=changeBackground)

homeScreenMiniMenu.add_command(label="Home",command=showOpenCanvas)
homeScreenMiniMenu.add_separator()
homeScreenMiniMenu.add_cascade(label="Personalise",menu=personalMenu)
homeScreenMiniMenu.add_command(label="New Filter",command=newFilter)
homeScreenMiniMenu.add_command(label="Bulk Edit",command=loadBulkEdit)
homeScreenMiniMenu.add_command(label="New Pupil",command=showCreatePupil)
homeScreenMiniMenu.add_command(label="Help",command=showHelp)

showHelp
#View Group mini menu
showGroupMiniMenu=Menu(showGroupCanvas,tearoff=0)
showGroupMiniMenu.add_command(label="View Pupil",command=lambda :loadDoubleClick(showGroupListbox))
showGroupMiniMenu.add_command(label="Remove From Group",command=removeGroupPupil)
showGroupMiniMenu.add_command(label="Edit Group",command=addGroupToBulk)

#Bindings-------------------------
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)
filterResults.bind('<Double-Button-1>', viewFilterResults)
viewAllListbox.bind('<Double-Button-1>', viewallResults)
viewAllListbox.bind('<ButtonRelease-1>', pupilGradeClick)
viewAllListbox.bind('<Up>', pupilGradeClick)
viewAllListbox.bind('<Down>', pupilGradeClick)
bulkAllPupilListbox.bind("<Double-Button-1>",prePreAddBulkPupil)
bulkFilterPupilListbox.bind("<Double-Button-1>",prePreRemoveBulkPupil)
bulkAllPupilListbox.bind("<Button-1>",bulkDisableViewAll)
bulkFilterPupilListbox.bind("<Button-1>",bulkDisableFilter)
status.bind("<Double-Button-1>",preOpenCanvas)

#Menu for groups
groupMenu.add_command(label="New Group",command=lambda: loadCanvas(newGroupCanvas,"New Group"))
groupMenu.add_separator()

#Mac and PC right click bindings are diffrent
if version == "Darwin":
    window.bind("<Button-2>", viewPupilPopup)
    bulkAllPupilListbox.bind("<Button-2>",preBulkViewAllMenu)
    bulkFilterPupilListbox.bind("<Button-2>",preBulkFilterMenu)
    filterResults.bind("<Button-2>",lambda event: postMenu(event,filterResults,filterPupilsMiniMenu))
    colourListBox.bind("<Button-2>",lambda event: postMenu(event,colourListBox,themeMiniMenu))
    backgroundListBox.bind("<Button-2>",lambda event: postMenu(event,backgroundListBox,backgroundMiniMenu))
    status.bind("<Button-2>",showHomeMiniMenu)
    showGroupListbox.bind("<Button-2>",lambda event: postMenu(event,showGroupListbox,showGroupMiniMenu))
    groupListbox.bind("<Button-2>",lambda event: postMenu(event,groupListbox,createGroupMiniMenu))
else:
    window.bind("<Button-3>", viewPupilPopup)
    bulkAllPupilListbox.bind("<Button-3>",preBulkViewAllMenu)
    bulkFilterPupilListbox.bind("<Button-3>",preBulkFilterMenu)
    filterResults.bind("<Button-2>",lambda event: postMenu(event,filterResults,filterPupilsMiniMenu))
    colourListBox.bind("<Button-2>",lambda event: postMenu(event,colourListBox,themeMiniMenu))
    backgroundListBox.bind("<Button-2>",lambda event: postMenu(event,backgroundListBox,backgroundMiniMenu))
    status.bind("<Button-3>",showHomeMiniMenu)
    showGroupListbox.bind("<Button-3>",lambda event: postMenu(event,showGroupListbox,showGroupMiniMenu))
    groupListbox.bind("<Button-3>",lambda event: postMenu(event,groupListbox,createGroupMiniMenu))



showPupilName.bind("<KeyRelease>",checkIfSame)
showPupilSecond.bind("<KeyRelease>",checkIfSame)
showPupilGrade.bind("<KeyRelease>",checkIfSame)
showPupilNotes.bind("<KeyRelease>",checkIfSame)
viewPersonalBestEntry.bind("<KeyRelease>",checkIfSame)
createPupilTarget.bind("<KeyRelease>",createPupilOptionMenuFunction)
bulkChangeEntry.bind("<KeyRelease>",checkBulkEntry)
status.bind("<Enter>",statusHoverIn)
status.bind("<Leave>",statusHoverOut)

openLabel.bind("<Double-Button-1>",preUserName)
viewTotalPupilLabel.bind("<Double-Button-1>",preViewAll)
showPassNumberLabel.bind("<Button-1>",viewPassStatus)
showFailNumber.bind("<Button-1>",viewFailStatus)
showPassLabel.bind("<Double-Button-1>",sortPasses)
showFailLabel.bind("<Double-Button-1>",sortFails)



#=======Returns===========

setOpenUser(getUserName())
getPupilsFromFile("pupils.txt")

#Order array
orderPB()

#Returns to gather infomation or initiate functions

addPupilsMenu(newOrderPupils)
addBinding(createPupilCanvas, createPupilInfoStep)
addBinding(filterPupilCanvas,searchPupilStep)
addBinding(newGroupCanvas,preSubmitNewGroup)
initBackground()
initTheme()
showOpenCanvas()
addJustify(viewPupilCanvas,True)
checkGrades()
groupOrderArray=getGroupsFromFile()
if groupOrderArray != None:
    for item in groupOrderArray:
        beforeAddedGroups.append(item)
else:
    groupOrderArray=[]
initNewGroups()
bindArray([openLabel,viewTotalPupilLabel,showPassLabel,showFailLabel,showNumberLabel,showFailNumber,showPassNumberLabel])
bindLabelArray()

#Runs program
window.mainloop()
