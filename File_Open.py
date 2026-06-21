with open("tasks.txt", "w") as f:
    f.write("1.Review Python Notes\n 2.Complete Coding Exercise\n 3. Backup Important Files\n")
with open("tasks.txt", "a") as a:
    a.write("Tasks file created successfully.")


with open("tasks.txt", "r") as r:
    content = r.read()
    print(content)
    print("Tasks file read successfully.")


with open ("tasks.txt", "r") as r:
    content = r.read()
    if "Prepare Presentation" in content:
        print("Task already exists.")
    else:
        with open("tasks.txt", "a") as a:
            a.write("4. Prepare Presentation\n")
            print("Task added successfully.")

