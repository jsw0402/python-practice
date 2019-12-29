user_input=input("저장할 내용을 입력하시오:")
f=open('./test.txt','a')
f.write("\n")
f.write(user_input)
f.write("\n")
f.close()

