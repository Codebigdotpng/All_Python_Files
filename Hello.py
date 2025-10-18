attempts=0
i="hello"
greeting=input("Say hello(all lowercase):")
while greeting!=i:
    print("Please, just say hello.")
    greeting=input("Say hello(all lowercase):")
    attempts+=1
print("It took you",attempts,"tries just to say hello.")