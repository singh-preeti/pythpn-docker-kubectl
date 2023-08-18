# f=open("abc.txt", 'w')
# print("File Name: ", f.name)
# print("File Mode: ", f.mode)
# print("Is File Readable: ", f.readable())
# print("Is File Writable: ", f.writable())
# print("Is File Closed : ", f.closed)
# f.close()
# print("Is File Closed : ", f.closed)


#Writing the file
# f=open("wish.txt", 'w')
# f.write("Welcome\n")
# f.write("to\n")
# f.write("python world\n")
# print("Data written to the file successfully")
# f.close()

# f=open("wish.txt", 'a')
# f.write("Welcome\n")
# f.write("to\n")
# f.write("automation\n")
# print("Data written to the file successfully")
# f.close()

f=open("wish.txt", 'r')
data=f.read()
print(data)
f.close()