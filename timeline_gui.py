from tkinter import *
from datetime import date

# Get and store local day information into a dict
local_date = date.today()
date_dict = {
    "year": local_date.year,
    "month": local_date.month,
    "day": local_date.day,
}

# GUI
root = Tk()
root.title("Day Management")

main_frame = LabelFrame(root, text="Main Menu", padx=50, pady=5)
main_frame.grid(row=0, column=0)


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

    

    # Confirmation message
    confirmation = Label(add_frame, text="Activity Added!")
    confirmation.grid(row=6, column=0)


def rem_activity():
    pass


def edit_activity():
    pass


activityAddButton = Button(main_frame, text="Add Activity!", command=add_activity)
activityRemButton = Button(main_frame, text="Remove Activity!", command=rem_activity)
activityEditButton = Button(main_frame, text="Edit Activity!", command=edit_activity)

activityAddButton.grid(row=0, column=0, padx=10)
activityRemButton.grid(row=0, column=1, padx=10)
activityEditButton.grid(row=0, column=2, padx=10)

root.mainloop()