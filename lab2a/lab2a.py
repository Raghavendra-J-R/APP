"""
2a. Write the file mode that will be used for opening the following files. Also, write the Python statements to open the following files: a text file “example.txt” in both read and write  mode      
a binary file “bfile.dat” in write mode             
a text file “try.txt” in append and read mode               
a binary file “btry.dat” in read only mode.

"""

# Open example.txt in read mode
with open("example.txt", "r") as file_read:
    print("Reading example.txt:")
    print(file_read.read())

# Open example.txt in write mode
with open("example.txt", "w") as file_write:
    file_write.write("This is a new content.")

# Open bfile.dat in write mode
with open("bfile.dat", "wb") as binary_file_write:
    binary_file_write.write(b"\x00\x01\x02\x03\x04")

# Open try.txt in append and read mode
with open("try.txt", "a+") as append_read_file:
    append_read_file.write("This is appended content.\n")
    append_read_file.seek(0)
    print("\nReading try.txt after appending:")
    print(append_read_file.read())

# Open btry.dat in read only mode
with open("btry.dat", "rb") as binary_read_file:
    print("\nReading btry.dat:")
    print(binary_read_file.read())
