__author__ = 'Angus'

#Angus Goody
#8/10/15

#Pi Pal version 4.2

#Imports-------
from tkinter import *
import datetime
from tkinter import colorchooser


#Sets up window---------
window=Tk()
window.geometry("420x320")
window.title("PiPal")

#Staus bar
statusVar=StringVar()
status=Label(window,text="Status",bg="lightblue",textvariable = statusVar)
status.pack(side=BOTTOM,fill=X)

 #Main variables=================
mainButtonColour="light green"
userName=""
encryptionKey=8

#Toolbars====================
mainMenu=Menu(window)
window.config(menu=mainMenu)

#Sub menus==================
fileMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)
#Canvas'=====================


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
'purple1', 'purple2', 'purple3', 'purple4']

#Change Theme canvas
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

#Change Background canvas
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
    
    
#Arrays
letterArray=['b', 'p', 'K', 'C', 'A', 'e', ' ', '0', '(', '?', 'B', '{', 'l', 'o', 'X', 'q', '|', ')', '3', '"', 'a', 'I', '}', '~', 'V', '%', '\x0c', '`', 'L', '4', 'D', 'z', 't', 'u', '#', 'M', '<', '+', 'T', '8', 'R', ':', '\t', 'E', 'Z', '9', '2', '@', 'h', 'y', "'", '=', 's', ';', 'x', '¦', 'G', '&', 'c', 'N', '6', 'S', '>', '5', '.', '_', '-', '/', 'Q', 'd', 'm', 'O', 'J', 'W', '¬', 'Y', ',', 'k', 'n', '1', '[', '7', 'H', 'j', 'r', '*', ']', 'i', 'P', '!', '\x0b', 'F', '$', '\\', 'U', 'g', 'f', '^', 'v', 'w']

sportArray=["Football","Hockey","Tennis","Basketball","Rugby"]
canvasArray=[openCanvas,changeUserNameCanvas,changeThemeCanvas,changeBackgroundCanvas]
themeEntry=Entry(window)

#Entry Arrays that contains all visable entrys on screen
mainEntryArray=[changeUserNameEntry]

# Start of Functions===========================================================


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
    saveLineToFile("userName.txt",temp,"defaultColour:")
    print("Theme changed to",colour)
                

            
        

def showOpenCanvas():
    loadCanvas(openCanvas,"Home")

def updateTheme(colour):
    if colour not in colourArray:
        print("Colour not in colour array")
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
            print("Testing sucess")
            updateTheme(colour)
            updateButtonBackground(colour)
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
        if len(words) > 1:
            try:
                colour=words[1]
            except:
                print("Indexing background error")
            else:
                
                try:
                    testEntry.config(bg=colour)
                except:
                    print("Background test failed trying other options")
                    try:
                        temp=colour
                        temp=temp+" "
                        temp=temp+words[2]
                    except:
                        colour=window.cget("bg")
                    else:
                        colour=temp
                        try:
                            testEntry.config(bg=colour)
                        except:
                            print("Second background test failed")
                            colour=window.cget("bg")
                        else:
                            print("Second background test sucess")
                            colour=temp
        else:
            colour=window.cget("bg")
        
        return colour                
            
 
def initBackground():
    col=getBackgroundFromFile()
    print("Using",col,"as colour")
    if col != None and col != "":
        updateBackgroundColours(col)          
        
   
def updateBackgroundColours(colour):
    window.config(bg=colour)
    for item in canvasArray:
        item.config(bg=colour)
        for widget in item.winfo_children():
            if widget.winfo_class() != "Entry" and widget.winfo_class() != "Button" :
                widget.config(bg=colour)
            widget.config(highlightbackground=colour)

def updateButtonBackground(colour):
    for item in canvasArray:
                for widget in item.winfo_children():
                    if widget.winfo_class() == "Button":
                        widget.config(bg=colour)
                        
mainColour="black"                        
def toggleTextColour():
    global mainColour
    if mainColour == "black":
        mainColour="white"
    elif mainColour == "white":
        mainColour="black"
    
    for item in canvasArray:
        for widget in item.winfo_children():
            if widget.winfo_class() == "Entry":
                widget.config(fg=mainColour)

        
# End of Functions===========================================================


#Return functions===================
setOpenUser(getUserName())


#Add cascades and commands=====================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)

#File Menu
fileMenu.add_command(label="Home",command=showOpenCanvas)
fileMenu.add_separator()
fileMenu.add_command(label="Change Info",command=changeUserName)
fileMenu.add_command(label="Change Theme",command=changeTheme)
fileMenu.add_command(label="Change Background",command=changeBackground)
fileMenu.add_separator()

#View Menu
viewMenu.add_command(label="Toggle Text Colour",command=toggleTextColour)


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



#Bindings
changeUserNameEntry.bind("<KeyRelease>",checkOverwrite)

initBackground() #This function needs to be here because it changes colours of buttons that would otherwise be under it
initTheme()
window.mainloop()

