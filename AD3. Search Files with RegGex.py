import re

text = "myfile.txt"

    # Searching for the character "m" in the text. 
found = re.search("m", text)

# complex object
print(found) 

if found:
  print("Found it!")
else:
  print("Nope")
