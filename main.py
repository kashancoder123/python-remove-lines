# Program to remove lines starting with any prefix

file1 = open('codingal.txt','r')
file2 = open('codingalUpdated.txt','w')

#reading each line form original
# text file
for line in file1.readline():

   # reading all lines that do not 
   # begin with "coding"
   if not (line.startswith("Hello")):
      

    # printing those lines
    print("line")

    # storing only those lines that
    # do not begin with "coding"
    file2.write(line)