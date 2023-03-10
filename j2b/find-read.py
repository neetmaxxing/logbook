import os, sys

#change the cloned repo path in the variable below
global PATH
PATH = "/home/nathan/Documents/logbook/j2b/"


def find_read():
    print("""1:Sort
2:Search
3:Quit""")

    ans = int(input("\n: "))
    ans_dic = {1 :sort, 2:keysearch, 3:leave}
    act = ans_dic.get(ans, error)
    act()


def sort():
    print("""Sorting files by:
    1: oldest
    2: latest
    3: volume (greatest to least)""")
    choice = int(input("\n: "))
    choice_dic = {1: oldest, 2:latest, 3: vol}
    action = choice_dic.get(choice, error)
    action()

def oldest():
    search("-time=ctime --inode")
        
def latest():
    search("t -h --inode")
def vol():
    print("Sorting size by largest first. \n")
    search("S --inode")


def keysearch():
    keyword = str(input("(enter keywords): "))
    if not keyword == "":
        search_file = os.popen(f"ls | grep {keyword}").read()
    else:
        print(os.listdir(PATH))

def search(command):
    query = os.system(f"ls -l -{command}")
    if query == 256:
        sys.exit("No file matched your query. Exiting...")
    elif query == 32512:
        error()

    print(query)

def leave():
    sys.exit("Quitting.")

def error():
    sys.exit("Error encountered. Exiting...")


find_read()
