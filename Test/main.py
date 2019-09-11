import tkinter as tk
import test
import GUI
import dbHelper

#root = tk.Tk()

#app = GUI.bookwedding(root)
#root.mainloop()

# print(Test.dbHelper.read_from_db())

dbHelper.connect()
GUI.mainMenu()


weddingList = []

for i in weddingList:
    print(i.contactNo)

