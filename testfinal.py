
# Importing tkinter functions
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("775x775+890+10")
root.configure(background="deep sky blue")
root.title("Hockey Pool")

# draw canvas
can = Canvas(root, width=749, height=499)
can.grid(row=0, column=0, padx=10, pady=10)
image1 = Image.open("preview1.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(650, 25, 700, 75, fill="black", outline="#DDD", width=4)
can.create_line(575, 50, 645, 50, fill="#DDD", width=4)
can.create_line(600, 40, 645, 40, fill="#DDD", width=4)
can.create_line(600, 60, 645, 60, fill="#DDD", width=4)
can.create_text(675, 50, text="Pool", fill="white")

site = requests.get("https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")

if site.status_code is 200:
    content = BeautifulSoup(site.content, "html.parser")
else:
    content = -99
    
def scrape():
    if (messagebox.askyesno("Wait? This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
        content = BeautifulSoup(site.content, "html.parser")
        totalpts = 0
        for myplayer in lst: # loop to check my players
            dTag = content.find(attrs={"csk": myplayer})
            parent = dTag.findParent('tr')
            if parent==False:
                break
            playerpts = int(parent.contents[0].text) # 8th tag is total points
            totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
        print(totalpts)
    
print("Downloading Hockey Data")
site = requests.get("https://www.hockey-reference.com/leagues/NHL_2019_skaters.html")

# Defines input as a string, sorts input item
def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)

# Adds conditions to the list, gives list the addItem function; Memory variable
def addItem():
    item = entry.get()
    if (lst.count(item) == 0):
        lst.append(item)
        entry.delete(0, END)
        updatelab()

# Adds conditions to the list, gives list remItem function; Memory variable
def remItem():
    item = entry.get()
    if (lst.count(item) >= 0):
        lst.remove(item)
        entry.delete(0, END)
        updatelab()
        
def saveList():
    myfile = open("myplayers.txt", "w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")

def addPlayerOptions():
    if(content != -99):
        names = content.findAll(attrs={"data-stat": "player"})
        playerOptions = []
        for player in names:
            if(player != "None"):
                playerOptions.append(player.get('csk'))
        return playerOptions

def addPlayer(evt):
    global players
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    lst.append(name)
    
"""def comparebutton():
    root1 = Tk()
    root1.geometry("775x749+890+10")
    root1.configure(background="deep sky blue")
    root1.title("Compare Stats")
    def addPlayerOptions2():
        if(content != -99):
            names = content.findAll(attrs={"data-stat": "player"})
            playerOptions = []
            for player in names:
                if(player != "None"):
                    playerOptions.append(player.get('csk'))
            return playerOptions
    def stats(evt):
        var=listbox.get(ANCHOR)
        if var!=NONE:
            dTag=content.find(attrs={"csk":var})
            parent=dTag.findParent("tr")
            points=int(parent.contents[8].text)
            games=int(parent.contents[5].text)
            team=str(parent.contents[3].text)
            position=str(parent.contents[4].text)
            goals=int(parent.contents[6].text)
            assists=int(parent.contents[7].text)
        listbox3 = Listbox(root,height=9)
        listbox3.place(x=200, y=525)
        listbox3.insert(END, "[Stats]")
        listbox3.insert(END,"Points: " + str(points))
        listbox3.insert(END, "Games Played: " + str(games))
        listbox3.insert(END,"Team: " + team)
        listbox3.insert(END,"Position: " + position)
        listbox3.insert(END,"Goals: " + str(goals))
        listbox3.insert(END,"Assists: " + str(assists))
    OPTIONS = addPlayerOptions2()
    variable2 = StringVar(root1)
    variable2.set(OPTIONS[0]) # Default Value
    w2 = OptionMenu(root1, variable2, *OPTIONS, command=addPlayer1)
    w2.place(x=0, y=0)
    listbox3 = Listbox(root1, height=9)
    listbox3.place(x=200, y=200)"""
    
def remPlayerOptions():
    if(content != -99):
        names = content.findAll(attrs={"data-stat": "player"})
        playerOptions = []
        for player in names:
            if(player != "None"):
                playerOptions.remove(player.get('csk'))
        return playerOptions
    
def remPlayer(value):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)

def createlistbox(value):
    var=listbox.get(ANCHOR)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        games=int(parent.contents[5].text)
        team=str(parent.contents[3].text)
        age=int(parent.contents[2].text)
        position=str(parent.contents[4].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        plus=int(parent.contents[9].text)
        pim=int(parent.contents[10].text)
    listbox2 = Listbox(root,height=10)
    listbox2.place(x=200, y=525)
    listbox2.insert(END, "[Stats]")
    listbox2.insert(END,"Points: " + str(points))
    listbox2.insert(END, "Games Played: " + str(games))
    listbox2.insert(END,"Team: " + team)
    listbox2.insert(END, "Age:" + str(age))
    listbox2.insert(END,"Position: " + position)
    listbox2.insert(END,"Goals: " + str(goals))
    listbox2.insert(END,"Assists: " + str(assists))
    listbox2.insert(END, "+/-:" + str(plus))
    listbox2.insert(END, "PIM:" +str(pim))
    
def comparePlayers():
    def addPlayer(evt):
        global players
        name = variable.get()
        if players.count(name) > 0:
            return
        listbox3.insert(END, name)
        lst.append(name)
        
    def addPlayer2(evt):
        global players
        name2 = variable2.get()
        if players.count(name2) > 0:
            return
        listbox4.insert(END, name2)
        lst.append(name2)
        
    def remPlayer(value):
        var=listbox3.get(ACTIVE)
        listbox3.delete(listbox3.index(ACTIVE))
    
    def remPlayer2(value):
        var=listbox4.get(ACTIVE)
        listbox4.delete(listbox4.index(ACTIVE))
        
    def createlistbox1(value):
        print('hi')
        var1=listbox3.get(ANCHOR)
        filename1 = str(var1)
        if var1!=NONE:
            dTag=content.find(attrs={"csk":var1})
            parent=dTag.findParent("tr")
            goals=int(parent.contents[6].text)
            assists=int(parent.contents[7].text)
            points=int(parent.contents[8].text)
            gp=int(parent.contents[5].text)
            age=int(parent.contents[2].text)
            team=str(parent.contents[3].text)
            position=str(parent.contents[4].text)
            plus=int(parent.contents[9].text)
            pim=int(parent.contents[10].text)
        listbox5 = Listbox(root1, width=20, height=10)
        listbox5.place(x=30, y=300)
        listbox5.insert(END, "[Stats]")
        listbox5.insert(END, "Games Played: " + str(gp))
        listbox5.insert(END, "Age: " + str(age))
        listbox5.insert(END, "Team: " + str(team))
        listbox5.insert(END, "Position: " + str(position))
        listbox5.insert(END, "Goals: " + str(goals))
        listbox5.insert(END, "Assists: " + str(assists))
        listbox5.insert(END, "Points: " + str(points))
        listbox5.insert(END, "+/-: " + str(plus))
        listbox5.insert(END, "PIM: " +str(pim))
        
    def createlistbox2(value):
        print('gello')
        var=listbox4.get(ANCHOR)
        filename = str(var)
        if var!=NONE:
            dTag=content.find(attrs={"csk":var})
            parent=dTag.findParent("tr")
            goals=int(parent.contents[6].text)
            assists=int(parent.contents[7].text)
            points=int(parent.contents[8].text)
            gp=int(parent.contents[5].text)
            age=int(parent.contents[2].text)
            team=str(parent.contents[3].text)
            position=str(parent.contents[4].text)
            plus=int(parent.contents[9].text)
            pim=int(parent.contents[10].text)
        listbox6 = Listbox(root1, width=20, height=10)
        listbox6.place(x=270, y=300)
        listbox6.insert(END, "[Stats]")
        listbox6.insert(END, "Games Played: " + str(gp))
        listbox6.insert(END, "Age: " + str(age))
        listbox6.insert(END, "Team: " + str(team))
        listbox6.insert(END, "Position: " + str(position))
        listbox6.insert(END, "Goals: " + str(goals))
        listbox6.insert(END, "Assists: " + str(assists))
        listbox6.insert(END, "Points: " + str(points))
        listbox6.insert(END, "+/-: " + str(plus))
        listbox6.insert(END, "PIM: " +str(pim))
        
    root1 = Tk()
    root1.geometry("500x500+800+100")
    root1.configure(background="deep sky blue")
    root1.title("Compare players")

    can1 = Canvas(root1, width=480, height=150)
    can1.place(x=10, y=10)
    titleRect = can1.create_rectangle(0, 0, 480, 150, fill='medium spring green')
    text = can1.create_text(75, 20, text="Comparing Statistics", fill="black")
    
    listbox3 = Listbox(root1, width=20,height=10)
    listbox3.place(x=30, y=120)
    
    listbox3.bind("<<ListboxSelect>>", createlistbox1)
    
    listbox4 = Listbox(root1, width=20,height=10)
    listbox4.place(x=270, y=120)
    
    listbox4.bind('<<ListboxSelect>>', createlistbox2)
    
    OPTIONS = addPlayerOptions()
    variable = StringVar(root1)
    variable.set(OPTIONS[0])
    w = OptionMenu(root1, variable, *OPTIONS,command=addPlayer) 
    w.place(x=30, y=70)
    
    OPTIONS = addPlayerOptions()
    variable2 = StringVar(root1)
    variable2.set(OPTIONS[1])
    v = OptionMenu(root1, variable2, *OPTIONS, command=addPlayer2)
    v.place(x=270, y=70)
    
    listbox.bind("<<ListboxSelect>>", createlistbox1)
    listbox.bind("<<ListboxSelect>>", createlistbox2)
    
def helpbutton():
    root2=Tk()
    root2.geometry("950x500+890+10")
    root2.title("Help")
    text = Text(root2)
    text.place(x=200, y=200)
    text.insert(END, "To ADD to pool, select desired player from the pulldown bar.\nTo REMOVE player, double click on the player in the listbox.\nTo CHECK THE STATS of a player, click once on desired player in the listbox.")
    
def switchfoto():
    global photo
    fullname1 = listbox.get(ANCHOR)
    firstname = fullname.split(",")[1]
    lastname = "" [0]
    fullname2 = lastname[0:5] + first[0:2] + "01.jpg"   
    can2 = Canvas(root, width=500, height=700)
    can2.place(x=700, y=700)
    image2 = Image.open("headshots/" + fullname)
    photo2 = ImageTk.PhotoImage(image2)
   

# listbox
listbox = Listbox(root,height=10)
listbox.grid(row=1, column=0, sticky=NW, padx=10)
listbox.insert(END, "[Players]")

listbox.bind("<<ListboxSelect>>", switchfoto)
listbox.bind("<<ListboxSelect>>", createlistbox)
listbox.bind('<Double-Button>',remPlayer)

# pulldown
OPTIONS = addPlayerOptions()
variable = StringVar(root)
variable.set(OPTIONS[0]) # Default Value
w = OptionMenu(root, variable, *OPTIONS, command=addPlayer)
w.grid(row=1, column=0, sticky=NE, padx=10)
      
players = []

# Adds item in the list as string, adds site for stats
lst = []
lstprint = ""
totalpts = 0
print("Downloading Hockey Data")

# Allows player to save to computer
savebutton = Button(root, text="Save",command=saveList)
savebutton.grid(row=1, column=0, sticky=E, padx=10)

helpbtn = Button(root, text="Help", command=helpbutton)
helpbtn.place(x=395, y=550)

# Prints the list and intput from the user
mylab = Label(root,text=lstprint, anchor=W, justify=LEFT)

ptsbutton = Button(root, text="Check Points", command=scrape)
ptsbutton.place(x=11, y=710)

mypts = Label(root,text=totalpts)
mypts.place(x=11, y=735)


comparebtn = Button(root, text="Compare Players", command=comparePlayers)
comparebtn.place(x=395, y=525)

# Keeps window open
mainloop()