import matplotlib.pyplot as plt
from paths import resolve_path as path


days = [1, 2, 3, 4, 5]
sales = [100, 120, 90, 130, 150]

# Line Graph

# plt.plot(days, sales)
# plt.title("Sales Over Time")
# plt.xlabel("Day")
# plt.ylabel("Sales")

# Bar chart

# products = ['Apples', 'Bananas', 'Cherries']
# quantity = [30, 15, 25]

# plt.bar(products, quantity)
# plt.title("Fruit Inventory")
# plt.xlabel("Fruit")
# plt.ylabel("Quantity")
# plt.show()


# # Scatter Plot

# height = [150, 160, 170, 180]
# weight = [50, 60, 70, 80]

# plt.scatter(height, weight)
# plt.title("Height vs Weight")
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.show()

# Histogram

# ages = [18, 19, 22, 25, 25, 26, 28, 30, 33, 35]

# plt.hist(ages, bins=5)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.show()

# Pie Chart

labels = ['Math', 'Science', 'English']
scores = [40, 35, 25]

plt.pie(scores, labels=labels, autopct='%1.2f%%')
plt.title("Subject Score Percentages")
plt.show()

plt.savefig(path("plt_graph/start/Pie_Chart.png"))

