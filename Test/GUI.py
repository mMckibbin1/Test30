from tkinter import *
from tkinter import simpledialog
import test
import dbHelper
import CalendarWidget


# Main menu of applaction used to access all other forms


class mainMenu:
    def __init__(self):
        # creates form, removes maximise button on form, adds form title and adds background colour
        main_menu = Tk()
        main_menu.resizable(0, 0)
        main_menu.title("Main Menu")
        main_menu.config(background="powder blue")

        # adding UI elements to the form
        Label(main_menu, text="Please select what you would like1 to do...", font=("arial", 15, "bold"),
              bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10))

        btnbookWedding = Button(main_menu, text="Add wedding Booking", width=23, bg="medium aquamarine",
                                command=bookwedding)

        btnbookParty = Button(main_menu, text="Add Party Booking", width=23, bg="medium aquamarine", command=bookParty)
        btnbookConference = Button(main_menu, text="Add Conference Booking", width=23, bg="medium aquamarine")
        btnviewbookings = Button(main_menu, text="View, edit and delete Bookings", width=23, bg="medium aquamarine")

        btnbookWedding.grid(row=1, column=0, pady=(25, 5))
        btnbookParty.grid(row=2, column=0, pady=(25, 5))
        btnbookConference.grid(row=3, column=0, pady=(25, 5))
        btnviewbookings.grid(row=4, column=0, pady=(25, 25))

        main_menu.mainloop()


################################################################################################################


class bookwedding:
    def __init__(self):
        # FrmWeddingBooking = Tk()
        FrmWeddingBooking = Toplevel()
        FrmWeddingBooking.grab_set

        FrmWeddingBooking.title("Wedding bookings")
        FrmWeddingBooking.resizable(0, 0)
        FrmWeddingBooking.config(background="powder blue")

        RoomOption = ['H', 'I']
        BandNames = ["Lil' Febrezey", "Prawn Mendes", "AB/CD"]

        noGuests = IntVar()
        nameOfContact = StringVar()
        address = StringVar()
        contactNo = StringVar()
        eventRoomNo = StringVar()
        dateOfEvent = StringVar()
        dateOfBooking = StringVar()
        bandName = StringVar()
        noBedroomsReserved = IntVar()

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

        self.EntnumberOfguest = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=noGuests)
        self.EntnameOfContact = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=nameOfContact)
        self.EntAddress = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=address)
        self.EntContactNumber = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=contactNo)
        self.OpmEventRoomNumber = OptionMenu(FrmWeddingBooking, DefaultRoomNo, *RoomOption)
        self.CalDateOfEvent = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=dateOfEvent)
        self.CalDateOfEvent.bind("<Button-1>", self.popup)
        self.data = {}
        # self.EntDateOfEvent = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=dateOfEvent)
        self.OpmBandName = OptionMenu(FrmWeddingBooking, DefaultBandName, *BandNames)
        self.EntBedroomReserved = Entry(FrmWeddingBooking, font=("arial", 10), width=50, textvar=noBedroomsReserved)

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
                                                                   self.OpmEventRoomNumber.get(),
                                                                   self.CalDateOfEvent.get(),
                                                                   self.EntDateOfBooking.get(),
                                                                   self.OpmBandName.get(),
                                                                   self.EntBedroomReserved.get()), exit])

        btnAddBooking.grid(row=10, column=1, columnspan=1, pady=(25, 50), padx=(0, 25), sticky="ew")
        btnCloseForm.grid(row=10, column=3, columnspan=2, pady=(25, 50), padx=(0, 50), sticky="ew")

        FrmWeddingBooking.wait_window()
        FrmWeddingBooking.mainloop()

    def popup(self, event):
        child = Toplevel()
        cal = CalendarWidget.Calendar(child, self.data)
        child.wait_window()
        self.Get_selected_date()

    def Get_selected_date(self):
        Day = self.data.get("day_selected", "Test")
        Month = self.data.get("month_selected", "Test")
        year = self.data.get("year_selected", "Test")
        Date = str(Day) + "/" + str(Month) + "/" + str(year)
        self.CalDateOfEvent.delete(0, 'end')
        self.CalDateOfEvent.insert([0], Date)


#####################################################################################################################

class bookParty:
    def __init__(self):
        FrmPartyBooking = Tk()
        # FrmPartyBooking = Toplevel()
        # FrmPartyBooking.grab_set
        # mainMenu.wait_window()
        FrmPartyBooking.title("Wedding bookings")
        FrmPartyBooking.resizable(0, 0)
        FrmPartyBooking.config(background="powder blue")

        noGuests = IntVar()
        nameOfContact = StringVar()
        address = StringVar()
        contactNo = StringVar()
        eventRoomNo = StringVar()
        dateOfEvent = StringVar()
        dateOfBooking = StringVar()
        bandName = StringVar()
        bandPrice = IntVar()

        Label(FrmPartyBooking, text="Please fill in the details for the Party event you are booking",
              font=("arial", 15, "bold"), bg="powder blue") \
            .grid(row=0, pady=(25, 0), padx=(10, 10), columnspan=3)

        Label(FrmPartyBooking, text="Number of guest", font=("arial", 10, "bold"), bg="powder blue").grid(row=1,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmPartyBooking, text="Name of contact", font=("arial", 10, "bold"), bg="powder blue").grid(row=2,
                                                                                                          pady=(
                                                                                                              25, 0),
                                                                                                          padx=(
                                                                                                              10, 10))
        Label(FrmPartyBooking, text="Address", font=("arial", 10, "bold"), bg="powder blue").grid(row=3, pady=(25, 0),
                                                                                                  padx=(10, 10))
        Label(FrmPartyBooking, text="Contact number", font=("arial", 10, "bold"), bg="powder blue").grid(row=4,
                                                                                                         pady=(25, 0),
                                                                                                         padx=(
                                                                                                             10, 10))
        Label(FrmPartyBooking, text="Event Room Number", font=("arial", 10, "bold"), bg="powder blue").grid(row=5,
                                                                                                            pady=(
                                                                                                                25, 0),
                                                                                                            padx=(
                                                                                                                10, 10))
        Label(FrmPartyBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=6,
                                                                                                        pady=(25, 0),
                                                                                                        padx=(10, 10))
        Label(FrmPartyBooking, text="Date of event", font=("arial", 10, "bold"), bg="powder blue").grid(row=7,
                                                                                                        pady=(25, 0),
                                                                                                        padx=(10, 10))
        Label(FrmPartyBooking, text="Band Name", font=("arial", 10, "bold"), bg="powder blue").grid(row=8,
                                                                                                    pady=(25, 0),
                                                                                                    padx=(10, 10))

        self.EntnumberOfguest = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=noGuests)
        self.EntnameOfContact = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=nameOfContact)
        self.EntAddress = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=address)
        self.EntContactNumber = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=contactNo)
        self.EntEventRoomNumber = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=eventRoomNo)
        self.EntDateOfEvent = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=dateOfEvent)
        self.EntDateOfBooking = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=dateOfBooking)
        self.EntBandName = Entry(FrmPartyBooking, font=("arial", 10), width=50, textvar=bandName)

        self.EntnumberOfguest.grid(row=1, column=1, sticky=W, pady=(25, 0), padx=(0, 25))
        self.EntnameOfContact.grid(row=2, column=1, pady=(25, 0), padx=(0, 25))
        self.EntAddress.grid(row=3, column=1, pady=(25, 0), padx=(0, 25))
        self.EntContactNumber.grid(row=4, column=1, pady=(25, 0), padx=(0, 25))
        self.EntEventRoomNumber.grid(row=5, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfEvent.grid(row=6, column=1, pady=(25, 0), padx=(0, 25))
        self.EntDateOfBooking.grid(row=7, column=1, pady=(25, 0), padx=(0, 25))
        self.EntBandName.grid(row=8, column=1, pady=(25, 0), padx=(0, 25))

        btnCloseForm = Button(FrmPartyBooking, text="Cancel", command=FrmPartyBooking.quit)

        btnAddBooking = Button(FrmPartyBooking, text="Add Booking",
                               command=lambda: [test.createParty(self.EntnumberOfguest.get(),
                                                                 self.EntnameOfContact.get(),
                                                                 self.EntAddress.get(),
                                                                 self.EntContactNumber.get(),
                                                                 self.EntEventRoomNumber.get(),
                                                                 self.EntDateOfEvent.get(),
                                                                 self.EntDateOfBooking.get(),
                                                                 self.EntBandName.get()), exit])

        btnAddBooking.grid(row=10, column=1, pady=(25, 50), padx=(0, 25))
        btnCloseForm.grid(row=10, column=2, pady=(25, 50), padx=(0, 25))
        FrmPartyBooking.mainloop()
