import os, sys

#change the cloned repo path in the variable below
global PATH
PATH = "/home/nathan/Documents/j2b/"


def find_read():
    print("""1:Sort
    2:Search
    3:Quit""")

    ans = int(input("\n: "))
    ans_dic = {1 :sort, 2:search, 3:leave}
    act = ans_doc.get(ans, error)
    act()


def sort():
    try:
        print("""Sorting files by:
        1: by oldest
        2: by latest
        3: by volume (greatest to least)""")
        choice = int(input("\n: "))
        choice_dic = {1: oldest, 2:latest, 3: vol}
        action = choice_dic.get(choice, error)
        def oldest():
            pass
        def latest():
            pass
        def vol():
            pass
    except KeyboardInterrupt:
        leave()

def search(keyword):
    query = os.system(f"find | grep {keyword}")
    if query == 256:
        sys.exit("No file matched your query. Exiting...")
    elif query == 32512:
        sys.exit("Bash command (find) missing... Exiting...")



def leave():
    sys.exit("Quitting.")

def error():
    sys.exit("Error encountered. Exiting...")


