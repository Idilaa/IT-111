# create a new file:
f = open("filedemo.txt", "x")
f.close()

# Overwrite in the file:
f = open("filedemo.txt", "w")
f.write("Be persistent and never give up hope.")
f.close()

# Append from a text file:
f = open("filedemo.txt", "a")
f.write("Success is falling nine times and getting up 10")
f.close()

# Delete a file
import os
os.remove("filedemo.txt")
f.close()





