import matplotlib.pyplot as plt

# Data to plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, label="y = 2x", color='b', marker='o')

# Adding titles and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display legend
plt.legend()

# Show the plot
plt.show()
