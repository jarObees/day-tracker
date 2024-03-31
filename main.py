# Get user input through Activity()
# Write data into some database

# DISPLAY
# Read data
# Display on individual timeline
# compare two separate days.
# See the total amount of time spent on a particular activity.

# Store type of activity, the date of the event, and the start/end time (24hr format),
class Activity:
    def __init__(self, type, date, start, end):
        self.type = type
        self.start = start
        self.end = end
        self.date = date
