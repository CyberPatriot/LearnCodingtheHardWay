#from subprocess import call #ADDED for system call # Try 1
import os #Added for System Call #Try2

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,

		#>>> clear = lambda: os.system('cls')
		#>>> clear()

        #print ("%s\r"); #this line DOESN'T PRINT ANYTHING
		
		
		#call(["ls", "-l"]) #TRY1
