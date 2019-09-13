import tkinter as tk

import a as a

import test
import GUI
import dbHelper

# list  = [[],[],[]]
#
# w1 = test.Wedding('Bill','Bob','Tom','Hooly',1,1,1,1,1,1)
# w2 = test.Wedding(2,'Bob',2,2,2,2,2,2,2,2)
#
# p1 = test.Party(1,'Bob',1,1,1,1,1,1,1)
# p2 = test.Party(2,'Bob',2,2,2,2,2,2,2)
#
# c1 = test.Conference(1,'Bob',1,1,1,1,1,1,1,1)
# c2 = test.Conference(2,'Bob',2,2,2,2,2,2,2,2)
#
# list[0].append(w1)
# list[0].append(w2)
#
# list[1].append(p1)
# list[1].append(p2)
#
# list[2].append(c1)
# list[2].append(c2)
#
# for list1 in list:
#     for object in list1:
#         if type(object) == test.Wedding:
#             print(object.noGuests)
#             print(object.contactNo)
#             'weddign'



print('')

dbHelper.connect()
GUI.mainMenu()

