######### Creator: Nolan Spencer
######### Last edit: 1/24/2021
######### CURRENT PROBLEMS:
# NO userinput validation, Heavily reliant on wordfile and im not sure if all words are in there
#
###################################
def findword(arg):
    wordfile = open("words2.txt", "r")
    userstrlength = len(arg)
    #print("This is the userstrlength: ")
    #print(userstrlength)
    #print("\n")

    #opening word file then assigning length of userinputstr to a new variable for comparison

    for line in wordfile:
        linelist = [char for char in line]
        linelength = len(line) - 1
        corrlen = False
        if(userstrlength == linelength):
            corrlen = True
                #print("This is the lengths: " + userstrlength +" This is linelength: " + linelength + "\n")
        lettercnt = 0
        if(corrlen == True):
            for i in range(userstrlength):
                for j in range(linelength):
                    #print("This is arg[i]" + arg[i] + "\n")
                    #print("This is line[j]" + line[j] + "\n")
                    if (arg[i] == linelist[j]):
                        linelist[j] = ''
                        lettercnt = lettercnt + 1
                        #print(linelist)
                        #print("This is Line: " + line + "\n")
                        #print("This is lettercnt: ")
                        #print(lettercnt)
                        #print("\n")
                        break


        if(lettercnt == userstrlength):
            #print("This is Lettercnt and userstrlength: ")
            #print(lettercnt)
            #print(" userstrlength: ")
            #print(userstrlength)
            #print("\n")
            print(line)
    wordfile.close()
loopend = "EXIT APP"
print               ("                      Word Unscrambler by Nolan Spencer")
print               ("Enter the letters you would like to be unscrambled. (Enter all in lowercase) ")
userinputstr = input("\nTo exit the program please enter 'EXIT APP': ")
if(userinputstr != loopend):
    print("Your words are: ")
    findword(userinputstr)
    print("\n")

    while(userinputstr != loopend):
        print               ("                      Word Unscrambler by Nolan Spencer")
        print               ("Enter the letters you would like to be unscrambled. (Enter all in lowercase) ")
        userinputstr = input("\nTo exit the program please enter 'EXIT APP': ")
        if(userinputstr != loopend):
            print("Your words are: ")
            findword(userinputstr)
            print("\n")