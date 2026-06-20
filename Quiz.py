with open("Test_File.txt", "w") as f:
  f.write("Hello, World!")

with open("Test_File.txt", "r") as f:
   i = f.read()
   print(i)

with open("Test_File.txt", "a") as f:
    f.write("\nThis is a second line!")

f = open("myfile.py", "x")