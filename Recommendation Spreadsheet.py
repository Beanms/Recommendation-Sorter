# have menu to add rec, comment on rec/ rate rec, remove rec, different genres of rec, edit rec add rec progress
import pickle
import os

def initialise():
    global filmLA
    global filmA
    global filmNS

    global seriesLA
    global seriesA
    global seriesNS

    global musicAR
    global musicAL
    global musicS
    global musicNS

    global bookAU
    global bookSE
    global bookSI

    global hobby

    global project

    folder_path = r'C:\Users\dylan\Rec files'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    try:
        f = open(r"C:\Users\dylan\Rec files\\filmLA.txt", "rb")
        filmLA = pickle.load(f)
    except:
        filmLA = []
        f = open(r"C:\Users\dylan\Rec files\\filmLA.txt", "wb")
        pickle.dump(filmLA, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\filmA.txt", "rb")
        filmA = pickle.load(f)
    except:
        filmA = []
        f = open(r"C:\Users\dylan\Rec files\\filmA.txt", "wb")
        pickle.dump(filmA, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\filmNS.txt", "rb")
        filmNS = pickle.load(f)
    except:
        filmNS = []
        f = open(r"C:\Users\dylan\Rec files\\filmNS.txt", "wb")
        pickle.dump(filmNS, f)
    finally:
        f.close()



    try:
        f = open(r"C:\Users\dylan\Rec files\\seriesLA.txt", "rb")
        seriesLA = pickle.load(f)
    except:
        seriesLA = []
        f = open(r"C:\Users\dylan\Rec files\\seriesLA.txt", "wb")
        pickle.dump(seriesLA, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\seriesA.txt", "rb")
        seriesA = pickle.load(f)
    except:
        seriesA = []
        f = open(r"C:\Users\dylan\Rec files\\seriesA.txt", "wb")
        pickle.dump(seriesA, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\seriesNS.txt", "rb")
        seriesNS = pickle.load(f)
    except:
        seriesNS = []
        f = open(r"C:\Users\dylan\Rec files\\seriesNS.txt", "wb")
        pickle.dump(seriesNS, f)
    finally:
        f.close()



    try:
        f = open(r"C:\Users\dylan\Rec files\\musicAR.txt", "rb")
        musicAR = pickle.load(f)
    except:
        musicAR = []
        f = open(r"C:\Users\dylan\Rec files\\musicAR.txt", "wb")
        pickle.dump(musicAR, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\musicAL.txt", "rb")
        musicAL = pickle.load(f)
    except:
        musicAL = []
        f = open(r"C:\Users\dylan\Rec files\\musicAL.txt", "wb")
        pickle.dump(musicAL, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\musicS.txt", "rb")
        musicS = pickle.load(f)
    except:
        musicS = []
        f = open(r"C:\Users\dylan\Rec files\\musicS.txt", "wb")
        pickle.dump(musicS, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\musicNS.txt", "rb")
        musicNS = pickle.load(f)
    except:
        musicNS = []
        f = open(r"C:\Users\dylan\Rec files\\musicNS.txt", "wb")
        pickle.dump(musicNS, f)
    finally:
        f.close()



    try:
        f = open(r"C:\Users\dylan\Rec files\\bookAU.txt", "rb")
        bookAU = pickle.load(f)
    except:
        bookAU = []
        f = open(r"C:\Users\dylan\Rec files\\bookAU.txt", "wb")
        pickle.dump(bookAU, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\bookSE.txt", "rb")
        bookSE = pickle.load(f)
    except:
        bookSE = []
        f = open(r"C:\Users\dylan\Rec files\\bookSE.txt", "wb")
        pickle.dump(bookSE, f)
    finally:
        f.close()
    try:
        f = open(r"C:\Users\dylan\Rec files\\bookSI.txt", "rb")
        bookSI = pickle.load(f)
    except:
        bookSI = []
        f = open(r"C:\Users\dylan\Rec files\\bookSI.txt", "wb")
        pickle.dump(bookSI, f)
    finally:
        f.close()



    try:
        f = open(r"C:\Users\dylan\Rec files\\hobby.txt", "rb")
        hobby = pickle.load(f)
    except:
        hobby = []
        f = open(r"C:\Users\dylan\Rec files\\hobby.txt", "wb")
        pickle.dump(hobby, f)
    finally:
        f.close()



    try:
        f = open(r"C:\Users\dylan\Rec files\\project.txt", "rb")
        project = pickle.load(f)
    except:
        project = []
        f = open(r"C:\Users\dylan\Rec files\\project.txt", "wb")
        pickle.dump(project, f)
    finally:
        f.close()


def mainMenu():
    print("""
1. Add
2. Edit
3. Progress
4. Comment
5. Rate
6. Remove
7. Exit""")
    
    while True:
        option = input("> ")

        if option == "1" or option.upper() == "ADD":
            addRec()
        elif option == "2" or option.upper() == "EDIT":
            editRec()
        elif option == "3" or option.upper() == "PROGRESS":
            addProg()
        elif option == "4" or option.upper() == "COMMENT":
            addCom()
        elif option == "5" or option.upper() == "RATE":
            rateRec()
        elif option == "6" or option.upper() == "REMOVE":
            removeRec()
        elif option == "7" or option.upper() == "EXIT":
            exit()
        elif option.upper() == "KILL":
            path = r"C:\Users\dylan\Rec files\\"
            for file_name in os.listdir(path):
                file = path + file_name
                if os.path.isfile(file):
                    os.remove(file)
            os.rmdir(path)
            mainMenu()
            

def addRec():
    print("""
1. Film
2. Series
3. Music
4. Book
5. Hobby
6. Project
7. Back""")

    while True:
        addOption = input("> ")

        if addOption == "1" or addOption.upper() == "FILM":
            film()
        elif addOption == "2" or addOption.upper() == "SERIES":
            series()
        elif addOption == "3" or addOption.upper() == "MUSIC":
            music()
        elif addOption == "4" or addOption.upper() == "BOOK":
            book()
        elif addOption == "5" or addOption.upper() == "HOBBY":
            hobby()
        elif addOption == "6" or addOption.upper() == "PROJECT":
            project()
        elif addOption == "7" or addOption.upper() == "BACK":
            mainMenu()

def saveArray(type, file):
    f = open(r"C:\Users\dylan\Rec files\\" + f"{file}.txt", "wb")
    pickle.dump(type, f)
    f.close()

def saveName(name, type):
    f = open(r"C:\Users\dylan\Rec files\\" + f"{type}.txt", "a")
    f.write(f"{name.upper()}\n")
    f.close()
 
def film():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Live Action
3. Animated
4. Not Sure
5. Back""")

        filmOption = input(">")

        if filmOption == "1" or filmOption.upper() == "NAME":
            film()
        elif filmOption == "2" or filmOption.upper() == "LIVE ACTION":
            saveName(name, "Live Action Film")
            filmLA.append(name)
            saveArray(filmLA, "filmLA")
            mainMenu()
        elif filmOption == "3" or filmOption.upper() == "ANIMATED":
            saveName(name, "Animated Film")
            filmA.append(name)
            saveArray(filmA, "filmA")
            mainMenu()
        elif filmOption == "4" or filmOption.upper() == "NOT SURE":
            saveName(name, "Not Sure Film")
            filmNS.append(name)
            saveArray(filmNS, "filmNS")
            mainMenu()
        elif filmOption == "5" or filmOption.upper() == "BACK":
            addRec()

def series():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Live Action
3. Animated
4. Not Sure
5. Back""")

        seriesOption = input(">")

        if seriesOption == "1" or seriesOption.upper() == "NAME":
            series()
        elif seriesOption == "2" or seriesOption.upper() == "LIVE ACTION":
            saveName(name, "Live Action Series")
            seriesLA.append(name)
            saveArray(seriesLA, "seriesLA")
            mainMenu()
        elif seriesOption == "3" or seriesOption.upper() == "ANIMATED":
            saveName(name, "Animated Series")
            seriesA.append(name)
            saveArray(seriesA, "seriesA")
            mainMenu()
        elif seriesOption == "4" or seriesOption.upper() == "NOT SURE":
            saveName(name, "Not Sure Series")
            seriesNS.append(name)
            saveArray(seriesNS, "seriesNS")
            mainMenu()
        elif seriesOption == "5" or seriesOption.upper() == "BACK":
            addRec()

def music():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Artist
3. Album
4. Single
5. Not Sure
6. Back""")

        musicOption = input(">")

        if musicOption == "1" or musicOption.upper() == "NAME":
            music()
        elif musicOption == "2" or musicOption.upper() == "ARTIST":
            saveName(name, "Artist Music")
            musicAR.append(name)
            saveArray(musicAR, "musicAR")
            mainMenu()
        elif musicOption == "3" or musicOption.upper() == "ALBUM":
            saveName(name, "Album Music")
            musicAL.append(name)
            saveArray(musicAL, "musicAL")
            mainMenu()
        elif musicOption == "4" or musicOption.upper() == "SINGLE":
            saveName(name, "Single Music")
            musicS.append(name)
            saveArray(musicS, "musicS")
            mainMenu()
        elif musicOption == "5" or musicOption.upper() == "NOT SURE":
            saveName(name, "Not Sure Music")
            musicNS.append(name)
            saveArray(musicNS, "musicNS")
            mainMenu()
        elif musicOption == "6" or musicOption.upper() == "BACK":
            addRec()

def book():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Live Action
3. Animated
4. Not Sure
5. Back""")

        bookOption = input(">")

        if bookOption == "1" or bookOption.upper() == "NAME":
            book()
        elif bookOption == "2" or bookOption.upper() == "LIVE ACTION":
            saveName(name, "Live Action Book")
            bookAU.append(name)
            saveArray(bookAU, "bookAU")
            mainMenu()
        elif bookOption == "3" or bookOption.upper() == "ANIMATED":
            saveName(name, "Animated Book")
            bookSE.append(name)
            saveArray(bookSE, "bookSE")
            mainMenu()
        elif bookOption == "4" or bookOption.upper() == "NOT SURE":
            saveName(name, "Not Sure Book")
            bookSI.append(name)
            saveArray(bookSI, "bookSI")
            mainMenu()
        elif bookOption == "5" or bookOption.upper() == "BACK":
            addRec()

def hobby():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Save
3. Back""")

        hobbyOption = input(">")

        if hobbyOption == "1" or hobbyOption.upper() == "NAME":
            hobby()
        elif hobbyOption == "2" or hobbyOption.upper() == "SAVE":
            saveName(name, "Hobby")
            hobby.append(name)
            saveArray(hobby, "hobby")
            mainMenu()
        elif hobbyOption == "3" or hobbyOption.upper() == "BACK":
            addRec()

def project():
    name = input("""
Add Name:
> """)
    
    while True:
        print(f"""
1. Current Name: {name}
2. Save
3. Back""")

        projectOption = input(">")

        if projectOption == "1" or projectOption.upper() == "NAME":
            project()
        elif projectOption == "2" or projectOption.upper() == "SAVE":
            saveName(name, "Project")
            project.append(name)
            saveArray(project, "project")
            mainMenu()
        elif projectOption == "3" or projectOption.upper() == "BACK":
            addRec()

initialise()
while True:
    mainMenu()