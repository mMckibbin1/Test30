from tkinter import *
import Events.Conference
import Gui.BaseCreateForm

class bookConference(Gui.BaseCreateForm.BaseEvent):

    def __init__(self, master):
        RoomOption = ['A', 'B', 'C']

        super().__init__(master,RoomOption)

        # Creation of wedding form set title, size ect..
        master.title("Conference bookings")
        master.resizable(0, 0)
        master.config(background="powder blue")

        def ch_box_sel():
            print(CheckVar1.get())

        # defines options for dropdown boxes


        DefaultRoomNo = StringVar(master)
        DefaultRoomNo.set(RoomOption[0])  # default value

        # Labels for Conference booking form
        self.lblSubheading.config(text="Please fill in the details for the Conference event you are booking")

        self.lblCompanyname = Label(master, text="Company Name", font=("arial", 10, "bold"), bg="powder blue")
        self.lblCompanyname.grid(row=7,columnspan=2,pady=(25, 0),padx=(10, 10))

        self.lblNoofDays = Label(master, text="Number of Days", font=("arial", 10, "bold"), bg="powder blue")
        self.lblNoofDays.grid(row=8,columnspan=2, pady=(25, 0),padx=(10, 10))

        self.lblProjectorReq = Label(master, text="Projector Required", font=("arial", 10, "bold"), bg="powder blue")
        self.lblProjectorReq.grid(row=9, columnspan=2,pady=(25,0),padx=(10,10))


        # Entry boxes, dropdowns and datepicker for conference form
        self.EntCompanyName = Entry(master, font=("arial", 10), width=50)
        self.EntNoOfDays = Entry(master, font=("arial", 10), width=50)

        #checkbox now works :)
        CheckVar1 = IntVar()
        self.chxProjectorRequired = Checkbutton(master, text='', variable=CheckVar1, onvalue=True, offvalue=False, command=ch_box_sel)

        # Entry boxes, dropdowns and datepicker for conference form being placed using a grid layout
        self.EntCompanyName.grid(row=7, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))
        self.EntNoOfDays.grid(row=8, column=2, columnspan=2, pady=(25, 0), padx=(0, 25))


        #checkbox.....
        self.chxProjectorRequired.grid(row=9, column=2, pady=(25, 0), padx=(0, 25))

        # Buttons for Add and Cancel on the conference form
        self.btnAddBooking.config(command=lambda: [Events.Conference.createConference(self.EntnumberOfguest.get(),
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
