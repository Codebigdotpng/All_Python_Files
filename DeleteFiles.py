import os
if os.path.exists("TestAgain"):
  os.rmdir("TestAgain")
else:
  print("That folder does not exist. (Yet)")