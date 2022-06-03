# creating a file
#f = open("myfile.txt","x")

#writing in file
f = open("myfile.txt","w")
f.write("My name is Vidhi\n 12/2/2023 ytgshw2sih")

#reading from file
f = open("myfile.txt","r")
data = f.read()
print(data)
words = data.split()
print(words)
for i in words:
   if "/" in i:
       print(i)
