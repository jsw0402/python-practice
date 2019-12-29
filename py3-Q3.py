i=0
size=10
while True:
    i+=1
    if i>size:
        break
    print("★"*i,end="")
    print("☆"*(size-i+1))