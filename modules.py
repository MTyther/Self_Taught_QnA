# Question 1
import statistics

print("\nQuestion 1")
data = ["red", "blue", "blue", "red", "green", "red", "red"]
data1 = []
try:
    print(data)
    print("The mode in data list above is '{}' ".format(statistics.mode(data)))
except statistics.StatisticsError:
    print("Data list is empty!")

# Question 2
# In cubed.py
# def ncube(n):
#    return n*n*n
import cubed

value = cubed.ncube(3)
print(value)

