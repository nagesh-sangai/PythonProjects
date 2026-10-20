import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
hours = [1, 2, 3, 5, 6]

plt.plot(days, hours, marker="o")

plt.title("My Coding Progress")
plt.xlabel("Day")
plt.ylabel("Hours Practiced")
plt.grid(True)

plt.show()