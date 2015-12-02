__author__ = 'Angus'

#Angus Goody
#8/10/15

#Pi Pal version 3.1

#Imports-------
from tkinter import *
import datetime



#Sets up window---------
window=Tk()
window.geometry("420x320")
window.title("PiPal")

#Staus bar
statusVar=StringVar()
status=Label(window,text="Status",bg="lightblue",textvariable = statusVar)
status.pack(side=BOTTOM,fill=X)

 #Main variables
mainButtonColour="light green"
userName=""

#Toolbars-------------
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub menus
fileMenu=Menu(mainMenu)
sportsMenu=Menu(mainMenu)

#Canvas'-------------------------



#Open canvas
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)
statusVar.set("Home")
userVar=StringVar()

openLabel=Label(openCanvas,textvariable=userVar,font= "Helvetica 16 bold")
openLabel.grid(row=0,column=1)

#Change user canvas
changeUserNameCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(changeUserNameCanvas,text="Username:").grid(row=0,column=0)

changeUserNameEntry=Entry(changeUserNameCanvas,font = "Helvetica 12 bold", justify="center")
changeUserNameEntry.grid(row=0,column=1)

#Canvas to view sport file 
viewSportCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(viewSportCanvas,text="Sport:").grid(row=0,column=0)

viewSportName=Label(viewSportCanvas)
viewSportName.grid(row=0,column=1)

#Change Theme canvas
changeThemeCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
colourArray=["lightgreen","lightblue","magenta","orange","lawn green","cyan","orchid","orchid","gold"]

    
    
colourPicked=StringVar()
colourPicked.set("lightblue")

duplicateTestingArray=[]
for name in colourArray:
    if name not in duplicateTestingArray:
        try:
            b = Radiobutton(changeThemeCanvas, text=name.capitalize(),
                variable=colourPicked,value=name,bg=name,justify=LEFT)
        except:
            print("Found error in colour array 1")
        else:
            duplicateTestingArray.append(name)
            b.pack(fill=X)

#Adjusts the size of the window to view colours
if len(duplicateTestingArray) > 8:
    colourSpaceDiffrence=len(duplicateTestingArray) - 8
    colourSpaceDiffrence=colourSpaceDiffrence*80
    colourSpaceDiffrence=str(colourSpaceDiffrence)
    temp="420x"
    temp=temp+colourSpaceDiffrence
    window.geometry(temp)
    
    
#Arrays

sportArray=["Football","Hockey","Tennis","Basketball","Rugby"]
canvasArray=[openCanvas,changeUserNameCanvas,viewSportCanvas,changeThemeCanvas]
themeEntry=Entry(window)

#Entry Arrays that contains all visable entrys on screen
mainEntryArray=[changeUserNameEntry]





#Function to insert text into entry
def insertEntry(entry,message):
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
                    if len(wordsOnLine) > 1:
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

        userName=userName.capitalize()
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
    saveLineToFile("username.txt",temp,"userName123:")
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

def submitTheme():
    global colourPicked
    if colourPicked.get() in colourArray:
        updateTheme(colourPicked.get())  
        temp="defaultColour: "
        temp=temp+colourPicked.get()
        print("Temp is:",temp)
        
        #Writing to username file to store colour
        saveLineToFile("username.txt",temp,"defaultColour:")
        print("Theme changed to",colourPicked.get())
                

            
        

def showOpenCanvas():
    loadCanvas(openCanvas,"Home")

def updateTheme(colour):
    if colour not in colourArray:
        print("Unrecognised colour, trying colour anyway")
    else:
        colourPicked.set(colour)
    for item in mainEntryArray:

        try:
            item.config(bg=colour)
        except:
            item.config(bg="lightblue")

    try:
        status.config(bg=colour)
    except:
        print("Error with changing status colour")
        print("Using default colours because of unsupported colours:",colour)
        status.config(bg="lightblue")
           

def getThemeFromFile():
    targetLine=getFromFile("username.txt","defaultColour:")
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
            print("Testing sucess")
            updateTheme(colour)
        else:
            print("Testing of",colour,"failure using default")
            updateTheme("lightblue")
            

def hoverIn(event,button,colour):
    state=button.cget("state")
    if state == "normal" or state == "Normal":
        button.config(bg=colour)

def hoverOut(event,button):
    button.config(bg=window.cget("bg"))
    


            

def saveLineToFile(file,lineToAdd,target):
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
            file.write(lineToAdd)
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

# End of Functions===========================================================


#Return functions
setOpenUser(getUserName())
initTheme()

#Add cascades and commands
mainMenu.add_cascade(label="File",menu=fileMenu)


fileMenu.add_command(label="Home",command=showOpenCanvas)
fileMenu.add_separator()
fileMenu.add_command(label="Change Info",command=changeUserName)
fileMenu.add_command(label="Change Theme",command=changeTheme)

fileMenu.add_separator()

#Buttons

choseThemeButton=Button(changeThemeCanvas,text="Change",command=submitTheme,relief=GROOVE)
choseThemeButton.pack(pady=10)

overwriteUserNameButton=Button(changeUserNameCanvas,text="Overwrite",command=overwriteUserName,state=DISABLED,relief=GROOVE)
overwriteUserNameButton.grid(row=1,column=1,pady=8)


#Bindings
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)

window.mainloop()

