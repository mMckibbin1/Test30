from sqlite3.dbapi2 import Date
from tkinter import *
from tkinter import simpledialog
import test
import dbHelper
import CalendarWidget
import viewbooking
import datetime
import treeview


#Functions to call various pop-ups
def call_wedding_popup():
    top = Toplevel()
    ui = bookwedding(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

def call_party_popup():
    top = Toplevel()
    ui = bookParty(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

def call_conference_popup():
    top = Toplevel()
    ui = bookConference(top)
    top.grab_set()
    top.wait_window()
    top.destroy()

# def call_viewBookings_popup():
#     top = Toplevel()
#     ui = bookConference(top)
#     top.grab_set()
#     top.wait_window()
#     top.destroy()



##########################################       MAIN MENU      ###################################################

# Main menu of applIction used to access all other forms
class mainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        main_menu = Tk()
        main_menu.resizable(0, 0)
        main_menu.title("Main Menu")
        main_menu.config(background="powder blue")

        #adding UI elements to the form
        #Main menu Title
        Label(main_menu, text="Please select what you would like to do...",font=("arial",15,"bold"), bg="powder blue")\
            .grid(row=0, pady=(25, 0), padx=(10,10))

        #Main menu buttons with styling that redirect to our other windows
        btnbookWedding = Button(main_menu, text="Add wedding Booking", width=23, bg="medium aquamarine",command=call_wedding_popup)
        btnbookParty = Button(main_menu, text="Add Party Booking", width=23, bg="medium aquamarine", command=call_party_popup)
        btnbookConference = Button(main_menu, text="Add Conference Booking", width=23, bg="medium aquamarine",command=call_conference_popup)
        btnviewbookings = Button(main_menu, text="View, edit and delete Bookings", width=23, bg="medium aquamarine",command=viewbooking.call_viewBookings_popup)

        #Main menu buttons being placed using grid layout
        btnbookWedding.grid(row=1, column=0, pady=(25, 5))
        btnbookParty.grid(row=2, column=0, pady=(25, 5))
        btnbookConference.grid(row=3, column=0, pady=(25, 5))
        btnviewbookings.grid(row=4, column=0, pady=(25, 25))

        #calling the main menu loop
        main_menu.mainloop()




##########################################       BOOK WEDDING      ###################################################



#Class for Book Wedding UI window
class bookwedding:
    #setting default values for eventRoom and BandName as empty strings
    eventRoomNo = ''
    bandName = ''


    def __init__(self, master):
        #Creation of wedding form set title, size ect..
        master.title("Wedding bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        #defines options for dropdown boxes
        RoomOption = ['H', 'I']
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set(RoomOption[0])  # default value
        DefaultBandName = StringVar(master)
        DefaultBandName.set(BandNames[0])  # default value


        #Labels for Wedding booking form
        Label(master, text="Please fill in the details for the wedding event you are booking",font=("arial", 15, "bold"), bg="powder blue").grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1, columnspan=2, pady=(25, 0), padx=(10, 10))
        Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,columnspan=2,pady=( 25, 0), padx=(10, 10))
        Label(master, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4, columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,columnspan=2,pady=(25, 0),padx=(10,10))
        Label(master, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=8, columnspan=2, pady=(25, 0), padx=(10, 10))
        Label(master, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="powder blue").grid(row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        #Entry boxes, dropdowns and datepicker for wedding form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.OpmEventRoomNumber = OptionMenu(master, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)
        self.EntBedroomReserved = Entry(master, font=("arial", 10), width=50)

        # Entry boxes, dropdowns and datepicker for wedding form being placed using grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        #Buttons for Add and Cancel on the wedding form
        btnCloseForm = Button(master, text="Cancel", command=master.destroy)
        btnAddBooking = Button(master, text="Add Booking",
                               command=lambda: [test.createwedding(self.EntnumberOfguest.get(),
                                                                   self.EntnameOfContact.get(),
                                                                   self.EntAddress.get(),
                                                                   self.EntContactNumber.get(),
                                                                   self.eventRoomNo,
                                                                   self.CalDateOfEvent.get(),
                                                                   self.bandName,
                                                                   self.EntBedroomReserved.get()), master.destroy()])
        ##Buttons for Add and Cancel on the wedding form being placed using grid layout
        btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(25, 50), padx=(0, 25), sticky="ew")
        btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(25, 50), padx=(0, 50), sticky="ew")

    #function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value

    # function to display calander widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date()

    #function to get the selected date from calander widget and display it as a formatted string
    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)




############################################   BOOK PARTY  ############################################################




#Class for Book Party UI window
class bookParty:
    def __init__(self, master):
        # Creation of wedding form set title, size ect..
        master.title("Party bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        # defines options for dropdown boxes
        RoomOption = ['D', 'E', 'F', 'G']
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set(RoomOption[0])  # default value
        DefaultBandName = StringVar(master)
        DefaultBandName.set(BandNames[0])  # default value

        # Labels for Party booking form
        Label(master, text="Please fill in the details for the Party event you are booking",font=("arial", 15, "bold"), bg="powder blue").grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)
        Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Date of Event", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=7, columnspan=2,pady=(25, 0), padx=(10, 10))

        # Entry boxes, dropdowns and datepicker for party form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}
        self.OpmEventRoomNumber = OptionMenu(master, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.OpmBandName = OptionMenu(master, DefaultBandName, *BandNames, command=self.getBandName)

        # Entry boxes, dropdowns and datepicker for party form being placed using grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        # Buttons for Add and Cancel on the party form
        btnCloseForm = Button(master, text="Cancel", command=master.destroy)
        btnAddBooking = Button(master, text="Add Booking",
                               command=lambda: [test.createParty(self.EntnumberOfguest.get(),
                                                                 self.EntnameOfContact.get(),
                                                                 self.EntAddress.get(),
                                                                 self.EntContactNumber.get(),
                                                                 self.eventRoomNo,
                                                                 self.CalDateOfEvent.get(),
                                                                 self.bandName), master.destroy()])

        # Buttons for Add and Cancel on the party form being placed using grid layout
        btnAddBooking.grid(row=10, column=1, columnspan=1, sticky="ew", pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=3, columnspan=2, sticky="ew", pady=(25, 50), padx=(0, 25))

    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to get band name from dropdown
    def getBandName(self, value):
        self.bandName = value

    # function to display calander widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date()

    # function to get the selected date from calander widget and display it as a formatted string
    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)




#######################################          BOOK CONFERENCE          ###########################################



#Class for Book Conference UI window
class bookConference:

    def __init__(self, master):


        # Creation of wedding form set title, size ect..
        master.title("Conference bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        def ch_box_sel():
            print(CheckVar1.get())
            # C1Var = CheckVar1.get()
            #
            # if C1Var == 1:
            #     print
            #     "Yes"
            # if C1Var == 0:
            #     print
            #     "No"


        # defines options for dropdown boxes
        RoomOption = ['A', 'B', 'C']

        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set(RoomOption[0])  # default value

        # Labels for Conference booking form
        Label(master, text="Please fill in the details for the Conference event you are booking",font=("arial", 15, "bold"), bg="powder blue").grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        Label(master, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,columnspan=2,pady=(25,0),padx=(10,10))
        Label(master, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,columnspan=2,pady=(25,0),padx=(10,10))
        Label(master, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,columnspan=2, pady=(25, 0), padx=( 10,10))
        Label(master, text="Date of Event", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,columnspan=2,pady=(25, 0),padx=(10,10))
        Label(master, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=6, columnspan=2,pady=(25,0),padx=(10,10))
        Label(master, text="Company Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))
        Label(master, text="Number of Days", font=("arial", 10, "bold"), bg="powder blue").grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))
        Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="powder blue").grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))


        # Entry boxes, dropdowns and datepicker for conference form
        self.EntnumberOfguest = Entry(master, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(master, font=("arial", 10), width=50)
        self.EntAddress = Entry(master, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent = Entry(master, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", lambda event: self.popup(event, master))
        self.data = {}
        self.OpmEventRoomNumber = OptionMenu(master, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50)

        #checkbox now works :)
        CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=CheckVar1, onvalue=True, offvalue=False, command=ch_box_sel)

        # Entry boxes, dropdowns and datepicker for conference form being placed using a grid layout
        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))


        #checkbox.....
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the conference form
        btnCloseForm = Button(master, text="Cancel", command=master.destroy)
        btnAddBooking = Button(master, text="Add Booking",
                               command=lambda: [test.createConference(self.EntnumberOfguest.get(),
                                                                      self.EntnameOfContact.get(),
                                                                      self.EntAddress.get(),
                                                                      self.EntContactNumber.get(),
                                                                      self.CalDateOfEvent.get(),
                                                                      self.eventRoomNo,
                                                                      self.EntCompanyName.get(),
                                                                      self.EntNoOfDays.get(),
                                                                      #checkbox get
                                                                      CheckVar1.get()), master.destroy()])
        # Buttons for Add and Cancel on the conference form being placed using grid layout
        btnAddBooking.grid(row=10, column=1, columnspan=1, sticky="ew", pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=3, columnspan=2, sticky="ew", pady=(25, 50), padx=(0, 25))

    # function to get room number from dropdown
    def getRoomnumber(self, value):
        self.eventRoomNo = value

    # function to display calander widget for date of event
    def popup(self, event, master):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        master.grab_release()
        child.grab_set()
        child.wait_window()
        child.grab_release()
        master.grab_set()
        self.Get_selected_date()

    #function to get the selected date from calander widget and display it as a formatted string
    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)














    # #updated calander that can be used outside class
    # # function to display calander widget for date of event
    # def popup(self, event, master, caldata, entry):
    #     child = Toplevel()
    #     cal = CalendarWidget.Calendar(child, caldata)
    #     master.grab_release()
    #     child.grab_set()
    #     child.wait_window()
    #     child.grab_release()
    #     master.grab_set()
    #     self.Get_selected_date(caldata, entry)
    #
    # # function to get the selected date from calander widget and display it as a formatted string
    # def Get_selected_date(self, data, entry):
    #     Day = data.get("day_selected", "date error")
    #     Month = data.get("month_selected", "date error")
    #     year = data.get("year_selected", "date error")
    #     Date = str(Day) + "/" + str(Month) + "/" + str(year)
    #     entry.delete(0, 'end')
    #     entry.insert([0], Date)

