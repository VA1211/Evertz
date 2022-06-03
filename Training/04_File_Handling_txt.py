#f = open("C:\\Users\\vidhi.shah\\Desktop\\Evertz\\Sample files\\sample2.txt","r")
# data = f.read()               #to read full content of file
# print(data)
#print(f.readline())             #to read a line from a file
#print(f.read(10))                #reads 10 characters of file
# for i in f:                    #another way to print data of file
#     print(i)
#f.close()

# f = open("C:\\Users\\vidhi.shah\\Desktop\\Evertz\\Sample files\\sample2.txt","w") #overrides existing data
# f.write('''My name is Vidhi
#  I am working in Yash Technologies
#  I am practicing for Evertz project''')
#f.close()

# f = open("C:\\Users\\vidhi.shah\\Desktop\\Evertz\\Sample files\\sample2.txt","a") #adds in existing data
# f.write("\nI like to work here")
# f.close()

#file operations using with, it closes file automatically
# with open("myfile.txt","r") as file:
#     data = file.read()
#     print(data)

# with open("myfile.txt","w") as file:
#     file.write("This is other text I am writing in this file")

# with open("myfile.txt","a") as file:
#     file.write("\nI am adding this line")

#finding specific word from file
with open("myfile.txt","r") as file:
    data = file.read()
    print(type(data))
    print(data)
    words = data.split()
    print(words)
    for i in words:
        if "Yash" in i:
            print(i)
