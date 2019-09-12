from sqlite3.dbapi2 import Date
from tkinter import *
from tkinter import simpledialog
import test
import dbHelper
import CalendarWidget
import viewbooking
import datetime


# Main menu of applaction used to access all other forms


class mainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        main_menu = Tk()
        main_menu.resizable(0, 0)
        main_menu.title("Main Menu")
        main_menu.config(background="powder blue")

        # adding UI elements to the form
        Label(main_menu, text="Please select what you would like to do...", font=("arial", 15, "bold"),
              bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10))

        btnbookWedding = Button(main_menu, text="Add wedding Booking", width=23, bg="medium aquamarine",
                                command=bookwedding)

        btnbookParty = Button(main_menu, text="Add Party Booking", width=23, bg="medium aquamarine", command=bookParty)
        btnbookConference = Button(main_menu, text="Add Conference Booking", width=23, bg="medium aquamarine",command=bookConference)
        btnviewbookings = Button(main_menu, text="View, edit and delete Bookings", width=23, bg="medium aquamarine",
                                 command=viewbooking.frmViewBooking)

        btnbookWedding.grid(row=1, column=0, pady=(25, 5))
        btnbookParty.grid(row=2, column=0, pady=(25, 5))
        btnbookConference.grid(row=3, column=0, pady=(25, 5))
        btnviewbookings.grid(row=4, column=0, pady=(25, 25))

        main_menu.mainloop()


########################################################################################################################


class bookwedding:
    eventRoomNo = ''
    bandName = ''

    def __init__(self):
        # FrmWeddingBooking = Tk()
        FrmWeddingBooking = Toplevel()
        FrmWeddingBooking.grab_set

        FrmWeddingBooking.title("Wedding bookings")
        FrmWeddingBooking.resizable(0, 0)
        FrmWeddingBooking.config(background="powder blue")

        RoomOption = ['H', 'I']
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultRoomNo = StringVar(FrmWeddingBooking)
        DefaultRoomNo.set(RoomOption[0])  # default value
        DefaultBandName = StringVar(FrmWeddingBooking)
        DefaultBandName.set(BandNames[0])  # default value

        Label(FrmWeddingBooking, text="Please fill in the details for the wedding event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        Label(FrmWeddingBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,
                                                                                                            columnspan=2,
                                                                                                            pady=(
                                                                                                                25, 0),
                                                                                                            padx=(
                                                                                                                10, 10))
        Label(FrmWeddingBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,
                                                                                                            columnspan=2,
                                                                                                            pady=(
                                                                                                                25, 0),
                                                                                                            padx=(
                                                                                                                10, 10))
        Label(FrmWeddingBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, columnspan=2,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))
        Label(FrmWeddingBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,
                                                                                                           columnspan=2,
                                                                                                           pady=(25, 0),
                                                                                                           padx=(
                                                                                                               10, 10))
        Label(FrmWeddingBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,
                                                                                                              columnspan=2,
                                                                                                              pady=(
                                                                                                                  25,
                                                                                                                  0),
                                                                                                              padx=(
                                                                                                                  10,
                                                                                                                  10))
        Label(FrmWeddingBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,
                                                                                                          columnspan=2,
                                                                                                          pady=(25, 0),
                                                                                                          padx=(10, 10))
        Label(FrmWeddingBooking, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=8,
                                                                                                      columnspan=2,
                                                                                                      pady=(25, 0),
                                                                                                      padx=(10, 10))
        Label(FrmWeddingBooking, text="Number of bedrooms reserved", font=("arial", 10, "bold"), bg="powder blue").grid(
            row=9, columnspan=2, pady=(25, 0), padx=(10, 10))

        self.EntnumberOfguest = Entry(FrmWeddingBooking, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(FrmWeddingBooking, font=("arial", 10), width=50)
        self.EntAddress = Entry(FrmWeddingBooking, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(FrmWeddingBooking, font=("arial", 10), width=50)
        self.OpmEventRoomNumber = OptionMenu(FrmWeddingBooking, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.CalDateOfEvent = Entry(FrmWeddingBooking, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", self.popup)
        self.data = {}
        self.OpmBandName = OptionMenu(FrmWeddingBooking, DefaultBandName, *BandNames, command=self.getBandName)
        self.EntBedroomReserved = Entry(FrmWeddingBooking, font=("arial", 10), width=50)

        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.CalDateOfEvent.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmBandName.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntBedroomReserved.grid(row=9, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))

        btnCloseForm = Button(FrmWeddingBooking, text="Cancel", command=FrmWeddingBooking.quit)

        btnAddBooking = Button(FrmWeddingBooking, text="Add Booking",
                               command=lambda: [test.createwedding(self.EntnumberOfguest.get(),
                                                                   self.EntnameOfContact.get(),
                                                                   self.EntAddress.get(),
                                                                   self.EntContactNumber.get(),
                                                                   self.eventRoomNo,
                                                                   self.CalDateOfEvent.get(),
                                                                   self.bandName,
                                                                   self.EntBedroomReserved.get()), exit])

        btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(25, 50), padx=(0, 25), sticky="ew")
        btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(25, 50), padx=(0, 50), sticky="ew")

        FrmWeddingBooking.wait_window()
        FrmWeddingBooking.mainloop()

    def getRoomnumber(self, value):
        self.eventRoomNo = value

    def getBandName(self, value):
        self.bandName = value

    def popup(self, event):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        child.wait_window()
        self.Get_selected_date()

    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)


########################################################################################################################
class bookParty:
    def __init__(self):
        FrmPartyBooking = Tk()
        # FrmPartyBooking = Toplevel()
        # FrmPartyBooking.grab_set
        # mainMenu.wait_window()
        FrmPartyBooking.title("Party bookings")
        FrmPartyBooking.resizable(0, 0)
        FrmPartyBooking.config(background="powder blue")

        RoomOption = ['D', 'E','F','G']
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        DefaultRoomNo = StringVar(FrmPartyBooking)
        DefaultRoomNo.set(RoomOption[0])  # default value
        DefaultBandName = StringVar(FrmPartyBooking)
        DefaultBandName.set(BandNames[0])  # default value

        Label(FrmPartyBooking, text="Please fill in the details for the Party event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        Label(FrmPartyBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1, columnspan=2,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmPartyBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,columnspan=2,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmPartyBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3,columnspan=2, pady=(25, 0),
                                                                                                  padx=(10, 10))
        Label(FrmPartyBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,columnspan=2,
                                                                                                         pady=(25, 0),
                                                                                                         padx=(
                                                                                                             10, 10))
        Label(FrmPartyBooking, text="Date of Event", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,columnspan=2,
                                                                                                            pady=(
                                                                                                                25, 0),
                                                                                                            padx=(
                                                                                                                10, 10))
        Label(FrmPartyBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,columnspan=2,
                                                                                                        pady=(25, 0),
                                                                                                        padx=(10, 10))
        Label(FrmPartyBooking, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=7,columnspan=2,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))

        self.EntnumberOfguest = Entry(FrmPartyBooking, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(FrmPartyBooking, font=("arial", 10), width=50)
        self.EntAddress = Entry(FrmPartyBooking, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(FrmPartyBooking, font=("arial", 10), width=50)
        self.CalDateOfEvent = Entry(FrmPartyBooking, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", self.popup)
        self.data = {}
        self.OpmEventRoomNumber = OptionMenu(FrmPartyBooking, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.OpmBandName = OptionMenu(FrmPartyBooking, DefaultBandName, *BandNames, command=self.getBandName)

        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2,columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2,columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2,columnspan=2, pady=(25, 0), padx=(0, 25))
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.OpmBandName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")

        btnCloseForm = Button(FrmPartyBooking, text="Cancel", command=FrmPartyBooking.quit)

        btnAddBooking = Button(FrmPartyBooking, text="Add Booking",
                               command=lambda: [test.createParty(self.EntnumberOfguest.get(),
                                                                 self.EntnameOfContact.get(),
                                                                 self.EntAddress.get(),
                                                                 self.EntContactNumber.get(),
                                                                 self.eventRoomNo,
                                                                 self.CalDateOfEvent.get(),
                                                                 self.bandName), exit])

        btnAddBooking.grid(row=10, column=1, columnspan=1, sticky="ew", pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=3, columnspan=2, sticky="ew", pady=(25, 50), padx=(0, 25))
        FrmPartyBooking.mainloop()

    def getRoomnumber(self, value):
        self.eventRoomNo = value

    def getBandName(self, value):
        self.bandName = value

    def popup(self, event):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        child.wait_window()
        self.Get_selected_date()

    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)

########################################################################################################################

class bookConference:
    def __init__(self):
        def getBool(self):
            print(self.v.get())
        FrmConferenceBooking = Tk()
        FrmConferenceBooking.title("Conference bookings")
        FrmConferenceBooking.resizable(0, 0)
        FrmConferenceBooking.config(background="powder blue")

        RoomOption = ['A', 'B', 'C']

        DefaultRoomNo = StringVar(FrmConferenceBooking)
        DefaultRoomNo.set(RoomOption[0])  # default value

        Label(FrmConferenceBooking, text="Please fill in the details for the Conference event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=4)

        Label(FrmConferenceBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,
                                                                                                          columnspan=2,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmConferenceBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,
                                                                                                          columnspan=2,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmConferenceBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, columnspan=2,
                                                                                                  pady=(25, 0),
                                                                                                  padx=(10, 10))
        Label(FrmConferenceBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,
                                                                                                         columnspan=2,
                                                                                                         pady=(25, 0),
                                                                                                         padx=(
                                                                                                             10, 10))
        Label(FrmConferenceBooking, text="Date of Event", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,
                                                                                                        columnspan=2,
                                                                                                        pady=(
                                                                                                            25, 0),
                                                                                                        padx=(
                                                                                                            10, 10))
        Label(FrmConferenceBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,
                                                                                                            columnspan=2,
                                                                                                            pady=(
                                                                                                            25, 0),
                                                                                                            padx=(
                                                                                                            10, 10))
        Label(FrmConferenceBooking, text="Company Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=7, columnspan=2,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))
        Label(FrmConferenceBooking, text="Number of Days", font=("arial", 10, "bold"), bg="powder blue").grid(row=8, columnspan=2,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))
        Label(FrmConferenceBooking, text="Projector Required", font=("arial", 10, "bold"), bg="powder blue").grid(row=9, columnspan=2,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))
        self.EntnumberOfguest = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.EntnameOfContact = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.EntAddress = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.EntContactNumber = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.CalDateOfEvent = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.CalDateOfEvent.bind("<Button-1>", self.popup)
        self.data = {}
        self.OpmEventRoomNumber = OptionMenu(FrmConferenceBooking, DefaultRoomNo, *RoomOption, command=self.getRoomnumber)
        self.EntCompanyName = Entry(FrmConferenceBooking, font=("arial", 10), width=50)
        self.EntNoOfDays = Entry(FrmConferenceBooking,font=("arial", 10), width=50)
        self.v = BooleanVar()
        self.chxProjectorRequired = Checkbutton(FrmConferenceBooking, text='', variable=self.v,command=getBool(self))

        self.EntnumberOfguest.grid(row=1, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.CalDateOfEvent.grid(row=5, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.OpmEventRoomNumber.grid(row=6, column=2, columnspan=2, pady=(25, 0), padx=(0, 25), sticky="ew")
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        btnCloseForm = Button(FrmConferenceBooking, text="Cancel", command=FrmConferenceBooking.quit)

        btnAddBooking = Button(FrmConferenceBooking, text="Add Booking",
                               command=lambda: [test.createConference(self.EntnumberOfguest.get(),
                                                                 self.EntnameOfContact.get(),
                                                                 self.EntAddress.get(),
                                                                 self.EntContactNumber.get(),
                                                                 self.CalDateOfEvent.get(),
                                                                 self.eventRoomNo,
                                                                 self.EntCompanyName.get(),
                                                                 self.EntNoOfDays.get(),
                                                                 self.v1), exit])

        btnAddBooking.grid(row=10, column=1, columnspan=1, sticky="ew", pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=3, columnspan=2, sticky="ew", pady=(25, 50), padx=(0, 25))
        # FrmConferenceBooking.mainloop()

    def getRoomnumber(self, value):
        self.eventRoomNo = value



    def popup(self, event):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        child.wait_window()
        self.Get_selected_date()

    def Get_selected_date(self):
        Day = self.data.get("day_selected", "date error")
        Month = self.data.get("month_selected", "date error")
        year = self.data.get("year_selected", "date error")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)


