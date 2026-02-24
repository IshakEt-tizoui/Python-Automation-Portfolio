import tkinter as tk
import csv
import os
from tkinter import messagebox

root = tk.Tk()

Label = tk.Label(root, text="📦 Inventory Manager")

new_item_name = tk.Entry(root)
new_item_Quantity = tk.Entry(root)


def new_entry():
    file_exist = os.path.exists("inventory.csv")
    new_item = new_item_name.get()
    new_quantity = new_item_Quantity.get()
    if not new_item or not new_quantity:
         messagebox.showwarning("Missing!", "Please fill all fields!!")
    else:
        try:
            int(new_quantity)
            #Change "inventory" with another name if you wish to create another file or simply dont like the name
            with open("Inventory.csv", "a", newline='') as inv:
                writer = csv.writer(inv)
                if not file_exist:
                    writer.writerow(["Item", "Quantity"])
                writer.writerow([new_item, new_quantity])
                messagebox.showinfo("SUCCESS", f"Item added : {new_item} \nQuantity added : {new_quantity}")
                new_item_name.delete(0, tk.END)
                new_item_Quantity.delete(0, tk.END)
                
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

button = tk.Button(root, text="Add to inventory!", command=new_entry)

Label.pack()
new_item_name.pack()
new_item_Quantity.pack()
button.pack()

root.mainloop()