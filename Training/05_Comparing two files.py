#comparing complete files at once
# import filecmp

# f1= 'text1.txt'
# f2 = 'text2.txt'
#
# result = filecmp.cmp(f1,f2)      #shallow comparison, checks metadata like size,date modified etc
# print(result)
#
# result = filecmp.cmp(f1,f2,shallow=False)    #deep comparison
# print(result)

#comparing files line by line
#
f1 = open('text1.txt')

f2 = open('text2.txt')
i=0
for linef1 in f1:
    i=i+1

    for linef2 in f2:
        if linef1==linef2:
            print (f"line {i} : similar")

        else:
            print(f'line {i} : different')
            print("line of f1 : ",linef1,end='')
            print('line of f2 :',linef2,end='')
        break

f1.close()
f2.close()

