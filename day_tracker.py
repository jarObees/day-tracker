from tkinter import *
from datetime import date, datetime
import sqlite3
from matplotlib import pyplot as plt

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

c.execute("""CREATE TABLE activities (
            activity_id INTEGER PRIMARY KEY,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            notes TEXT
            );
            """)
c.execute("""CREATE TABLE types (
            type_id INTEGER PRIMARY KEY,
            name TEXT
            );
            """)

c.execute("""CREATE TABLE activities_types (
            activity_id INTEGER,
            type_id INTEGER,
            PRIMARY KEY (activity_id, type_id)
            FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
            FOREIGN KEY (type_id) REFERENCES types(type_id)
            );
            """)

for value in types_of_activities:
    c.execute("""
    INSERT INTO types (name)
    VALUES (?)
    """, (value,))

c.execute("""SELECT * FROM types""")
types_table = c.fetchall()

# SAMPLE DATA
sample_data = [
    ('2024-04-30 09:30', '2024-04-30 10:30', 'playing games'),
    ('2024-04-30 12:15', '2024-04-30 14:16', 'more games'),
    ('2024-04-30 15:30', '2024-04-30 16:30', 'eating linner'),
    ('2024-05-30 01:30', '2024-05-30 02:30', 'jacking off')
]
c.executemany("""
    INSERT INTO activities (start_date, end_date, notes) 
    VALUES (?, ?, ?)
    """, sample_data)

sample_data_activities_types = [
    (1, 1),
    (2, 1),
    (3, 3)
]
c.executemany("""
    INSERT INTO activities_types (activity_id, type_id)
    VALUES (?, ?)
    """, sample_data_activities_types)

c.execute(""" SELECT * FROM activities""")
sample_activities = c.fetchall()
c.execute(""" SELECT * FROM activities_types""")
sample_activities_types = c.fetchall()


def throw_error():
    pass


def leading_zero(input_str):
    if len(input_str) < 2:
        clean_input_str = "0" + input_str
        return clean_input_str
    else:
        return input_str

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
    startHourEntry = Entry(start_frame, width=10)
    Label(start_frame, text="Hour [24]").grid(row=0, column=0)
    startHourEntry.grid(row=0, column=1)
    startMinuteEntry = Entry(start_frame, width=10)
    Label(start_frame, text="Minute").grid(row=1, column=0)
    startMinuteEntry.grid(row=1, column=1)

    # End Time Frame Content
    endHourEntry = Entry(end_frame, width=10)
    Label(end_frame, text="Hour [24]").grid(row=0, column=0)
    endHourEntry.grid(row=0, column=1)
    endMinuteEntry = Entry(end_frame, width=10)
    Label(end_frame, text="Minute").grid(row=1, column=0)
    endMinuteEntry.grid(row=1, column=1)

    # Type of Activity
    type_frame = LabelFrame(add_frame, text="Type of Activity")
    type_frame.grid(row=5, column=2)
    activity_type1= StringVar()
    activity_type2 = StringVar()
    type_drop = OptionMenu(type_frame, activity_type1, *types_of_activities)
    type_drop2 = OptionMenu(type_frame, activity_type2, *types_of_activities)
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
            if int(startHourEntry.get()) not in range(1, 25) or int(endHourEntry.get()) not in range(1,25):
                throw_error()
            if int(startMinuteEntry.get()) not in range(1,61) or int(endMinuteEntry.get()) not in range(1,61):
                throw_error()
        except:
            Label(root, text="Please insert Start Time/ End Time numbers in appropriate range.", foreground="red").grid(row=9, column=0)
        try:
            if int(monthEntry.get()) not in range(1, 13) or int(dayEntry.get()) not in range(1,32):
                throw_error()
            int(yearEntry.get())
        except:
            Label(root, text="Please insert appropriate Year/Month/Date", foreground="red").grid(row=9,column=0)
        # TO:DO CLEAN THIS SHIT UP MAKE SURE THE INPUTS WORK
        act_month = leading_zero(monthEntry.get())
        act_day = leading_zero(dayEntry.get())
        start_hour = leading_zero(startHourEntry.get())
        start_minute = leading_zero(startMinuteEntry.get())
        end_hour = leading_zero(endHourEntry.get())
        end_minute = leading_zero((endMinuteEntry.get()))

        start_date = yearEntry.get() + "-" + act_month + "-" + act_day + " " + start_hour + ":" + start_minute
        end_date = yearEntry.get() + "-" + act_month + "-" + act_day + " " + end_hour + ":" + end_minute

        notes = notes_entry.get()

        # Begin SQLite Insertions
        def check_conflicts(start, end):
            c.execute("""
            SELECT * 
            FROM activities
            WHERE 
            (? BETWEEN activities.start_date AND activities.end_date)
            OR
            (? BETWEEN activities.start_date AND activities.end_date)
            """, (start, end))
            conflicting_events = c.fetchall()
            if conflicting_events:
                print("CONFLICT FOUND!")
                return True
            else:
                print("NO CONFLICTS!")
                return False

        if check_conflicts(start_date, end_date):
            throw_error()
        else:
            c.execute("""
            INSERT INTO activities (start_date, end_date, notes)
            VALUES (?, ?, ?)
            """, (start_date, end_date, notes))

            c.execute("""SELECT last_insert_rowid()""")
            last_activity_id = c.fetchone()[0]
            c.execute("""
            INSERT INTO activities_types (activity_id, type_id)
            VALUES (?, 
                (SELECT type_id FROM types WHERE name = ?)
            )
            """, (last_activity_id, activity_type1.get()))

            c.execute("""
            INSERT INTO activities_types(activity_id, type_id)
            VALUES (?, 
                (SELECT type_id FROM types WHERE name = ?)
            )
            """, (last_activity_id, activity_type2.get()))


    insert_data_button = Button(add_frame, text="ADD ACTIVITY!", command=insertData, borderwidth=5)
    insert_data_button.grid(row=6, column=1, columnspan=2)


    # Confirmation message
    #confirmation = Label(add_frame, text="Activity Added!")
    #confirmation.grid(row=6, column=0)

def rem_activity():
    pass


def edit_activity():
    pass


def visualize_activity():
    # Visualize all the activities from one day on a plot.
    def oneDay():
        oneDay_frame = LabelFrame(vis_frame, text="One Day")
        oneDay_frame.grid(row=1, column=0)

        # Add Date Information
        titleDay = Label(oneDay_frame, text="Day")
        dayEntry = Entry(oneDay_frame)

        titleMonth = Label(oneDay_frame, text="Month")
        monthEntry = Entry(oneDay_frame)

        titleYear = Label(oneDay_frame, text="Year")
        yearEntry = Entry(oneDay_frame)

        titleDay.grid(row=1, column=0)
        dayEntry.insert(0, date_dict["day"])
        dayEntry.grid(row=2, column=0)

        titleMonth.grid(row=1, column=1)
        monthEntry.insert(0, date_dict["month"])
        monthEntry.grid(row=2, column=1)

        titleYear.grid(row=1, column=2)
        yearEntry.insert(0, date_dict["year"])
        yearEntry.grid(row=2, column=2)

        act_month = leading_zero(monthEntry.get())
        act_day = leading_zero(dayEntry.get())
        sel_day = yearEntry.get() + "-" + act_month + "-" + act_day

        # Grab all data from particular day for matplotlib use in the future.
        c.execute("""SELECT * FROM activities WHERE Date(start_date) = ? """, (sel_day,))
        one_day_activities = c.fetchall()
        # Make a set that contains the unique activities of the day.
        distinct_activities = set()
        for activity in one_day_activities:
            activity_id = activity[0]
            c.execute("""SELECT DISTINCT name 
                        FROM types 
                        JOIN activities_types ON types.type_id=activities_types.type_id
                        WHERE activities_types.activity_id = ? """, (activity_id,))
            names = c.fetchone()
            name = names[0]
            distinct_activities.add(name)
        # Setup a dictionary with each unique activity as a key. Will be pulled from in order to create timeline.
        activities = {}
        for activity in distinct_activities:
            print("DICT: current activity: ", activity)
            activities[activity] = []
        # Add an activity_id to the appropriate activities[key].
        for activity in one_day_activities:

            activity_id, start_date, end_date, notes = activity
            # Get the activity type of activity by joining appropriate table.
            c.execute("""SELECT name 
                            FROM types 
                            JOIN activities_types ON types.type_id=activities_types.type_id
                            WHERE activities_types.activity_id = ?""", (activity_id,))
            activity_type = (c.fetchone())[0]
            activities[activity_type].append(activity_id)
        print("ALL UNIQUE ACTIVITITES :", activities)
        def make_timeline():
            BAR_HEIGHT = 2
            Y_INCREMENT = 4
            fig, ax = plt.subplots()
            bar_count = 0
            for unique_activity_type in activities:
                print("unique activity type: ", unique_activity_type)
                barh_activities = []
                for activity_id_data in activities[unique_activity_type]:
                    print("ACTIVITY ID: ", activity_id)
                    start_time = c.execute("""SELECT start_date FROM activities 
                    WHERE activity_id = ? """, (activity_id_data,)).fetchone()[0]
                    start_time = datetime.fromisoformat(start_time)

                    end_time = c.execute("""SELECT end_date FROM activities 
                    WHERE activity_id = ? """, (activity_id_data,)).fetchone()[0]
                    end_time = datetime.fromisoformat(end_time)

                    duration = (end_time - start_time)

                    barh_activity = (start_time, duration)
                    barh_activities.append(barh_activity)
                # Where on the Y graph this unique activity should be rendered in , and centers it on this value.
                y_start = Y_INCREMENT*(1 + bar_count) - BAR_HEIGHT / 2

                ax.broken_barh(barh_activities, (y_start, BAR_HEIGHT))
                bar_count += 1
            ax.set_yticks([4 + 4 * i for i in range(bar_count)])
            plt.xlabel('Time')
            plt.xticks(rotation=45)
            plt.ylabel('Activities')
            plt.title('One Day Analysis')
            plt.grid(True)
            plt.show()
        make_timeline()
    vis_frame = LabelFrame(root, text="Visualize Activity")
    vis_frame.grid(row=1, column=0)
    oneDayButton = Button(vis_frame, text="One Day", command=oneDay)
    oneDayButton.grid(row=0, column=0, padx=20)


activityAddButton = Button(main_frame, text="Add Activity", command=add_activity)
activityRemButton = Button(main_frame, text="Remove Activity", command=rem_activity)
activityEditButton = Button(main_frame, text="Edit Activity", command=edit_activity)
activityVisualizeButton = Button(main_frame, text="Visualize Activity", command=visualize_activity)
activityAddButton.grid(row=0, column=0, padx=10)
activityRemButton.grid(row=0, column=1, padx=10)
activityEditButton.grid(row=0, column=2, padx=10)
activityVisualizeButton.grid(row=0, column=3, padx=10)

root.mainloop()