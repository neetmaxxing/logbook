import os, sys

#change the cloned repo path in the variable below
global PATH
PATH = "/home/nathan/Documents/logbook/j2b/"


def mkjournal():
	curr_date = os.popen("date | cut -c 6-18").read()
	curr_date = curr_date[:-1]
	try:
		text = str(input("(write your journal down) > "))
		format = f"{curr_date} / {text}"
		with open(f"{PATH}{curr_date}", "x") as r:
			r.write(format)
			r.close()
			sys.exit("Journal saved.")
	except FileExistsError:
		print("File already exists. Delete [0/1] ?")
		ans = int(input("\n: "))
		if ans == 0:
			sys.exit("Quitting.")
		elif ans == 1:
			del_file = os.system (f"rm -rf {PATH}{curr_date}")
			sys.exit("\nThe file was deleted. Run the script again to rewrite one.")
		else:
			sys.exit("Incorrect input detected.")

mkjournal()
