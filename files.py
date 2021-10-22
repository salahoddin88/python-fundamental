"""
    r = read
    w = write (overwrite)
    a = append (append on existing)
    r+ = read and write(append)

"""

# fileObject = open('workfile.txt', 'r')
# # readData = fileObject.read()
# readData = fileObject.readline()

# fileObject.close()
# print(fileObject.closed)

# #This operation will read your existing file
# with open('workfile.txt', 'r') as fileObject:
#     readData = fileObject.read()
#     print(readData)

# #This operation will overwrite your existing file
# with open('workfile.txt', 'w') as fileObject:
#     readData = fileObject.write('My name is Akash)
#     print(readData)


# #This operation will append data to your existing file
# with open('workfile.txt', 'a') as fileObject:
#     readData = fileObject.write('My name is Akash)
#     print(readData)


# with open('workfile.txt', 'w') as fileObject:
#     readData = fileObject.write('abcdefg')

with open('workfile.txt', 'r+') as fileObject:
    readData = fileObject.read()
    print(readData)
    fileObject.truncate(0) # this will truncate your data from 0 offsets
    fileObject.write('Hello My name is salahuddin')
    # readData = fileObject.truncate(0)


with open('workfile.txt', 'r+') as fileObject:
    readData = fileObject.read()
    print(readData)




