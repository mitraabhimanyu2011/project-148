from tkinter import *
import random

root = Tk()
root.title("Picnic Time!")
root.geometry("400x400")

items = Label(root, text = "Listed items: Bottle, Tiffin, ID Card, Chocolates, Chips, Tickets, Hanky")
bag = Label(root)

def put():
    item = random.randint(0, 7)
    #get = item.get()
    if (item == 1):
        bag["text"] = "Put the bottle in the bag."
    elif (item == 2):
        bag["text"] = "Put the tiffin in the bag."
    elif (item == 3):
        bag["text"] = "Put the ID card in the bag."
    elif (item == 4):
        bag["text"] = "Put the chocolates in the bag."
    elif (item == 5):
        bag["text"] = "Put the chips in the bag."
    elif (item == 6):
        bag["text"] = "Put the tickets in the bag."
    elif (item == 7):
        bag["text"] = "Put the hanky in the bag."
    

btn = Button(root, text = "Which item should go in the bag?", command = put)

btn.pack()
items.pack()
bag.pack()

root.mainloop()