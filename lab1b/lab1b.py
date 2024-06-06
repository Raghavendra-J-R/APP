"""
1b.Write a program to enter the following records in a binary file:
    
Item No integer       
Item_Name string        
Qty integer        
Price float
Number of records to be entered should be accepted from the user. Read the file to display the records in the following format:
Item No:
Item Name :
Quantity:
Price per item:
Amount: ( to be calculated as Price * Qty)

"""

import struct

filename = "test.bin"
record_format = "i20sif"


def read_from_user():
    Item_no = int(input("Enter item no."))
    Item_name = input("Enter item name")
    Qty = int(input("Enter quantity"))
    Price = float(input("Enter price"))

    data = struct.pack(record_format, Item_no, Item_name.encode(), Qty, Price)
    with open(filename, "wb") as f:
        f.write(data)


def read_from_file():
    with open(filename, "rb") as f:
        text = f.read()
        item_no, item_name, qty, price = struct.unpack(record_format, text)

        item_name = item_name.decode().strip()

        # Calculate amount
        amount = qty * price

        print(f"Item No: {item_no}")
        print(f"Item Name: {item_name}")
        print(f"Quantity: {qty}")
        print(f"Price per item: {price:.2f}")
        print(f"Amount: {amount:.2f}")
        print("-" * 20)


if __name__ == "__main__":
    read_from_user()
    read_from_file()
