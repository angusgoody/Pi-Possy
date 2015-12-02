__author__ = 'Angus'

#Angus Goody
#8/10/15

#Pi Pal

#Imports-------
from tkinter import *

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

#New Sport canvas
newSportCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(newSportCanvas,text="Sport name").grid(row=0,column=0)

newSportEntry=Entry(newSportCanvas)
newSportEntry.grid(row=0,column=1)

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
colourArray=["lightgreen","lightblue","magenta","orange","lawn green","cyan","orchid","orchid","red","blue","yellow"]
colourPicked=StringVar()
colourPicked.set("lightblue")

duplicateTestingArray=[]
for name in colourArray:
    if name not in duplicateTestingArray:
        try:
            b = Radiobutton(changeThemeCanvas, text=name,
                variable=colourPicked,value=name,bg=name,justify=LEFT)
        except:
            print("Found error in colour array 1")
        else:
            duplicateTestingArray.append(name)
            b.pack(fill=X)

#Change button theme canvas
changeButtonThemeCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
buttonColourPicked=StringVar()
buttonColourPicked.set("lightgreen")

for name in duplicateTestingArray:
    try:
        b = Radiobutton(changeButtonThemeCanvas, text=name,
            variable=buttonColourPicked,value=name,bg=name,justify=LEFT)
    except:
        print("Found error in colour array 2")
    else:
        b.pack(fill=X)

    
#Arrays

sportArray=["Football","Hockey","Tennis","Basketball","Rugby"]
canvasArray=[openCanvas,newSportCanvas,changeUserNameCanvas,viewSportCanvas,changeThemeCanvas,changeButtonThemeCanvas]
themeEntry=Entry(window)

#Entry Arrays that contains all visable entrys on screen
mainEntryArray=[changeUserNameEntry,newSportEntry]





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
        

def setOpenUser(name):
    if name != "" and name != None:
        temp=""
        temp=temp+"Welcome "
        temp=temp+name
        userVar.set(temp)


def getSports():
    global sportArray
    content=getReadLines("sportFile.txt")
    if content != "" and content != None:
        counter=0
        for line in content:
            words=line.split()
            if len(words) > 0:
                line=line.rstrip()
                line=line.capitalize()
                line=str(line)
                if line not in sportArray:
                    sportArray.append(line)
                    counter=counter+1
                    

        print("Added",counter,"items to sports array")

    else:
        messagebox.showerror("Error","No sportsfile located")

def loadCreateSport():
    loadCanvas(newSportCanvas,"New Sport")

def submitNewSport():
    sport=newSportEntry.get()
    if sport != "":
        sport=sport.capitalize()
        if sport in sportArray:
            messagebox.showinfo("Exists","This sport allready exists")
        else:
            try:
                file=open("sportFile.txt","a")
            except:
                print("Function error")
            else:
                sport=sport.strip()
                file.write("\n")
                file.write(sport)
                file.close()
                sportArray.append(sport)
                
                sportsMenu.add_command(label=sport,command=lambda name=sport: sportClicked(name)) 
                messagebox.showinfo("Complete","Sport Created")
    
def addSportCommands():
    global sportArray
    for item in sportArray:
        sportsMenu.add_command(label=item,command=lambda name=item: sportClicked(name)) 
        
        
def changeUserName():
    loadCanvas(changeUserNameCanvas,"Change Info")
    global userName
    insertEntry(changeUserNameEntry,userName)
    overwriteUserNameButton.config(state=DISABLED)
    
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
    

def checkOverwrite(event):
    global userName
    changeUserNameEntry.config(state=NORMAL)
    text=changeUserNameEntry.get()
    comparison=userName

    if text == comparison:
        overwriteUserNameButton.config(state=DISABLED)
    else:
        overwriteUserNameButton.config(state=NORMAL)

#Function that loads when a sport is clicked

def sportClicked(sportName):
    print("Ready to load",sportName)
    #Add all stuff to send to canvas here
    insertViewSport(sportName)

def insertViewSport(sportName):
    global viewSportCanvas
    loadCanvas(viewSportCanvas,sportName)
    viewSportName.config(text=sportName)
   
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
   
#Initialises the theme setup process   
def initTheme():
    colour=getThemeFromFile()
    if colour != "" and colour != None:
        print("Testing theme colour...")
        result=checkColour(colour)
        if result != None and result != "":
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
    
def changeButtonTheme():
    loadCanvas(changeButtonThemeCanvas,"Change button theme")

def submitButtonTheme():
    global mainButtonColour
    chosenColour=buttonColourPicked.get()
    if chosenColour not in colourArray:
        print("Chosen colour not supported")
    else:
        mainButtonColour=chosenColour
        try:
            initHover()
        except:
            print("Error occoured")
        else:
            print("Successfull changed button theme to", chosenColour)

            temp="defaultButtonColour: "
            temp=temp+chosenColour
            #Add saving to file function here
            
            saveLineToFile("username.txt",temp,"defaultButtonColour:")
            

def saveLineToFile(file,lineToAdd,target):
    content=getReadLines(file)
    print()
    print("Initiating overwrite process -------------")
    print("File to open is:",file)
    print("Line to overwrite with is",lineToAdd)
    print("Target to replace is",target)
    contentArray=[]
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
    print("Initialising retrival from file of",target,"from",fileToSearch)
    content=getReadLines(fileToSearch)
    found=False
    for line in content:
        words=line.split()
        if target in words:
            found=True
            print("Target has been found")
            print("Returning",line)
            return line
            break

def getButtonTheme():
    global mainButtonColour
    content=getFromFile("username.txt","defaultButtonColour:")

    #Extracts button colour from line
    words=content.split()
    temp=""
    if len(words) > 1:
        if len(words) > 1:
            temp=words[1]
        if len(words) > 2:
            temp=temp+words[2]
        print()
        print("Cheking",temp,"as button colour")
        print("Testing colour now....")
        result=checkColour(temp)
        if result != None and result != "":
            print("Testing Sucess")
            mainButtonColour=result            
    else:
        print("Only 1 item found on line")

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
getSports()
addSportCommands()
initTheme()
getButtonTheme()

#Add cascades and commands
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Sports",menu=sportsMenu)


fileMenu.add_command(label="Home",command=showOpenCanvas)
fileMenu.add_separator()
fileMenu.add_command(label="New Sport",command=loadCreateSport)
fileMenu.add_command(label="Change Info",command=changeUserName)
fileMenu.add_command(label="Change Theme",command=changeTheme)
fileMenu.add_command(label="Change Button colour",command=changeButtonTheme)

fileMenu.add_separator()

#Add all sports to file menu



#Buttons
createSportButton=Button(newSportCanvas,text="Create",command=submitNewSport,relief=GROOVE)
createSportButton.grid(row=1,column=1,pady=8)

choseThemeButton=Button(changeThemeCanvas,text="Change",command=submitTheme,relief=GROOVE)
choseThemeButton.pack(pady=10)

overwriteUserNameButton=Button(changeUserNameCanvas,text="Overwrite",command=overwriteUserName,state=DISABLED,relief=GROOVE)
overwriteUserNameButton.grid(row=1,column=1,pady=8)

choseButtonThemeButton=Button(changeButtonThemeCanvas,text="Change",command=submitButtonTheme,relief=GROOVE)
choseButtonThemeButton.pack(pady=10)

#Bindings
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)

#Add button hover over functions

hoverButtonArray=[overwriteUserNameButton,choseThemeButton,createSportButton,choseButtonThemeButton] #Array for all buttons needing a hover funcction
def initHover():
    for button in hoverButtonArray:
        button.bind("<Enter>",lambda pas="a",button=button,colour=mainButtonColour: hoverIn(pas,button,colour)) #pas is event infomation with is useless but necesary to run
        button.bind("<Leave>",lambda pas="a",button=button: hoverOut(pas,button))
        
initHover()
window.mainloop()

