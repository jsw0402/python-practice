f1=open('./test1.txt','w')
f1.write("Life is too short")
f1.close()

f2=open('./test1.txt','r')
print(f2.read())
f2.close()