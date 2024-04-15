import matplotlib.pyplot as plt

# Horizontal bar plot with gaps
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (7, 2), facecolors='tab:brown')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (3, 2),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(0, 16)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([4, 8], labels=['Bill', 'Jim'])     # Modify y-axis tick labels
ax.grid(True)      # Make grid lines visible

plt.show()