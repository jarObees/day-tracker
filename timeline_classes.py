import matplotlib.pyplot as plt

# Horizontal bar plot with gaps
#activities = {
#    'rotting' : [1, 2]
#    'working' : [3,4]
#    'shitting' : [5]
#}

fig, ax = plt.subplots()

#counter = 0
#for unique_activity in activities:
    #ax.broken_barh(
        #[LIST OF TUPLES CONTAINING START AND END TIMES OF ALL UNIQUE ACTIVTIES]
        #COULD LOOK SOMETHING LIKE THIS
            # function takes in list of activity_id.
            # function returns a list of tuples, each tuple containing the start_time, duration (end_time - start_time)
        #,
        # BAR_HEIGHT = 2
        # Y_INCREMENT = 4
        # (TUPLE THAT CONTAINS THE Y START OF THE ACTIVITY BAR AND THE bar_height)
            # y_start = Y_INCREMENT(1 + counter) - BAR_HEIGHT / 2
            # (y_start, BAR_HEIGHT)
        #,
        # make it black or sumn idk
    #)
ax.broken_barh([(110, 30), (150, 10)], (7, 2), facecolors='tab:brown')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (3, 2),facecolors='tab:orange')
# ax.set_ylim(0, (number_of_unique_activities + 1) * Y_INCREMENT)
ax.set_ylim(0, 12 )
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
# ax.set_yticks(
    #list of all y heights of rendered bars.
        # function takes in y increment and number of unique activities.
        # function returns a list of y heights.
            # list = []
            # for unique_acitvities in activities:
                # counter = 0
                # list.append(y_increment * (1 + counter))
            # return list
    # labels= [another function]
        # labels should be a list of names of the unique activities (all the keys in the unique activity list.
ax.set_yticks([4, 8], labels=['Bill', 'Jim'])     # Modify y-axis tick labels
ax.set_xticks([])
ax.grid(True)      # Make grid lines visible

plt.show()