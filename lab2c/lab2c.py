"""
 2c.    Suppose we have created a file with 500 lines of data and the file object reference is   “f”. Illustrate what each of these following operations does:
a.	F.seek(0,)
b.	F.seek(10,1)
c.	F.seek(-10,2).
d.	F.seek(0,2)
e.	F.tell()
"""

# Open the file in read mode
with open("file.txt", "r") as f:
    # a. Move to the beginning of the file
    f.seek(0, 0)
    print("Current position after seeking to the beginning:", f.tell())

    # b. Move 10 bytes forward from the current position
    f.seek(10, 0)
    print("Current position after seeking 10 bytes forward:", f.tell())

    # # c. Move 10 bytes backward from the end of the file
    # f.seek(-10, 2)
    # print("Current position after seeking 10 bytes backward from the end:", f.tell())

    # d. Move to the end of the file
    f.seek(0, 2)
    print("Current position after seeking to the end:", f.tell())

    # e. Get the current position
    current_position = f.tell()
    print("Current position without seeking:", current_position)
