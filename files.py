coun_files=open("countries.txt","a")
# print(coun_files.readable()) 
# print(coun_files.readline())
# print(coun_files.readlines()[0])
# for lines in coun_files.readlines():
#     print(lines)
coun_files.write("\nthis is new line")
coun_files.close()
