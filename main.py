import matplotlib.pyplot as plt
from datetime import datetime

# Sample data
elements = [
    {"time": "2024-04-30T08:00:00", "value": 10},
    {"time": "2024-04-30T08:30:00", "value": 15},
    {"time": "2024-04-30T09:00:00", "value": 20},
    # Add more elements as needed
]

# Step 1: Convert string time values to datetime objects
times = [datetime.fromisoformat(element["time"]) for element in elements]

# Step 2: Extract other values
values = [element["value"] for element in elements]

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(times, values, marker='o', linestyle='-')

# Beautify the plot
plt.title('Plot of Elements Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()