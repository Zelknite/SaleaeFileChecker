import sys
import re

def main():
    file1 = open(sys.argv[1],"r")
    #Gathering all the data in the file and making it into a string
    content = file1.read()
    #use the split function to make an array of strings to iterate through
    string = re.split(' |\n|/',content)
    #close file1
    file1.close()
    #Open the second file
    file2 = open(sys.argv[2],"r")
    #read the data from the second file
    content2 = file2.read()
    string2 = re.split(' |\n|/',content2)
    print(string2)
    file2.close()
    loop(string, string2)

#let me know which files are bigger
def comparison(string, string2):
    if len(string2) > len(string):
        print("They are not the same size. The second file is larger.")
        print(len(string2))
        return 2
    elif len(string2)<len(string):
        print("They are not the same size. The first file is larger.")
        print(len(string))
        return 1
    elif len(string2)==len(string):
        print("They are the same size. The length of the two are as follows:")
        print("S1:",len(string),"S2:",len(string2))
        return 0
#start the for loop to compare
def loop(string, string2):
    x = comparison(string, string2)
    if x==2:
        print("Will not do, Second file larger")
    if x==1:
        print("Will not do, First file larger")
    if x==0:
        print("Starting For Loop...")
        print("S1", "S2")
        for y in range(0,len(string),1):
            if string[y] != string2[y]:
                print("These are the strings that are different:")
                print(string[y], string2[y])
                print("\n")
        print("There was nothing different about the two strings.")

if __name__ == "__main__":
    main()
