from tkinter import *
from datetime import date
import sqlite3

# Get and store local day information into a dict
local_date = date.today()
date_dict = {
    "year": local_date.year,
    "month": local_date.month,
    "day": local_date.day,
}

types_of_activities = [
    "Rot",
    "Productive",
    "Self-Care",
    "Commute",
    "School",
    "Leisure",
    None
]

class Activity:
    def __init__(self, type, start_hour, start_minute, end_hour, end_minute, date):
        self.type = type
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.date = date

# GUI Setup
root = Tk()
root.title("Day Management")
main_frame = LabelFrame(root, text="Main Menu", padx=50, pady=5)
main_frame.grid(row=0, column=0)

# Setup SQLite3 and necessary tables.
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE act_type (
            
            """)
c.execute("""CREATE TABLE activities (
            type text,
            start_hour int,
            start_minute int,
            end_hour int,
            end_minute int,
            date text
            )""")

def throw_error():
    pass

def add_activity():
    # Display the Add Activity Menu
    add_frame = LabelFrame(root, text="Add Activity")
    add_frame.grid(row=1, column=0)

    # Add Date Information
    titleDay = Label(add_frame, text="Day")
    dayEntry = Entry(add_frame)

    titleMonth = Label(add_frame, text="Month")
    monthEntry = Entry(add_frame)

    titleYear = Label(add_frame, text="Year")
    yearEntry = Entry(add_frame)

    # Start/End Time Frame Initilizations
    start_frame = LabelFrame(add_frame, text="Start Time")
    start_frame.grid(row=5, column=0)
    end_frame = LabelFrame(add_frame, text="End Time")
    end_frame.grid(row=5, column=1)

    # Start Time Frame Content
    start_hour = Entry(start_frame, width=10)
    Label(start_frame, text="Hour [24]").grid(row=0, column=0)
    start_hour.grid(row=0, column=1)
    start_minute = Entry(start_frame, width=10)
    Label(start_frame, text="Minute").grid(row=1, column=0)
    start_minute.grid(row=1, column=1)

    # End Time Frame Content
    end_hour = Entry(end_frame, width=10)
    Label(end_frame, text="Hour [24]").grid(row=0, column=0)
    end_hour.grid(row=0, column=1)
    end_minute = Entry(end_frame, width=10)
    Label(end_frame, text="Minute").grid(row=1, column=0)
    end_minute.grid(row=1, column=1)

    # Type of Activity
    type_frame = LabelFrame(add_frame, text="Type of Activity")
    type_frame.grid(row=5, column=2)
    activity_input = StringVar()
    activity_input2 = StringVar()
    type_drop = OptionMenu(type_frame, activity_input, *types_of_activities)
    type_drop2 = OptionMenu(type_frame, activity_input2, *types_of_activities)
    type_drop.grid(row=0, column=0)
    type_drop2.grid(row=1, column=0)

    # Additional Notes
    notes_frame = LabelFrame(add_frame, text="Additional Notes")
    notes_frame.grid(row=6, column=0)
    notes_entry = Entry(notes_frame, text="Notes (optional)")
    notes_entry.pack()


    # Display
    titleDay.grid(row=1, column=0)
    dayEntry.insert(0, date_dict["day"])
    dayEntry.grid(row=2, column=0)

    titleMonth.grid(row=1, column=1)
    monthEntry.insert(0, date_dict["month"])
    monthEntry.grid(row=2, column=1)

    titleYear.grid(row=1, column=2)
    yearEntry.insert(0, date_dict["year"])
    yearEntry.grid(row=2, column=2)

    Label(add_frame, text="        ").grid(row=4, column=0)

    # INSERT DATA
    def insertData():
        # Sanitize Data
        try:
            if int(start_hour.get()) not in range(1, 25) or int(end_hour.get()) not in range(1,25):
                throw_error()
            if int(start_minute.get()) not in range(1,61) or int(end_minute.get()) not in range(1,61):
                throw_error()
        except:
            Label(root, text="Please insert Start Time/ End Time numbers in appropriate range.", foreground="red").grid(row=9, column=0)
        # Insert Data into SQlite database
        current_activity = Activity()
        with conn:
            # Check to make sure that data in given time frame doesn't exist.
            c.execute("SELECT * FROM activities WHERE date = ")
            # If it exists, ask if you want to override and if not, do not insert data.
            # Else insert data.
            #




    insert_data_button = Button(add_frame, text="ADD ACTIVITY!", command=insertData, borderwidth=5)
    insert_data_button.grid(row=6, column=1, columnspan=2)


    # Confirmation message
    #confirmation = Label(add_frame, text="Activity Added!")
    #confirmation.grid(row=6, column=0)

def rem_activity():
    pass


def edit_activity():
    pass


activityAddButton = Button(main_frame, text="Add Activity", command=add_activity)
activityRemButton = Button(main_frame, text="Remove Activity", command=rem_activity)
activityEditButton = Button(main_frame, text="Edit Activity", command=edit_activity)

activityAddButton.grid(row=0, column=0, padx=10)
activityRemButton.grid(row=0, column=1, padx=10)
activityEditButton.grid(row=0, column=2, padx=10)

root.mainloop()