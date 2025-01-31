import math

# decalre list
points_per_game = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]

#original list of averages
print("Original list of points per game:")
print(points_per_game)

#sorted lsit
points_per_game_sorted = sorted(points_per_game, reverse=True)

print(" \nList sorted in descending order:")
print(points_per_game_sorted)

points_per_game = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]
#count of nums
count = len(points_per_game)
print(f"\nCount of numbers: {count}")

#mean
mean = sum(points_per_game) / count
print (f"\nMean (average) of set: {mean:.2f}") #round

#smallest and largest
smallest = min(points_per_game)
largest = max(points_per_game)
print(f"\nsmallest number is: {smallest}")
print(f"largest number is: {largest}")

#median
SortedList = sorted(points_per_game)
middle = len(SortedList) // 2 #find middle index

if len(SortedList) % 2 == 0:
    median = (SortedList[middle - 1] + SortedList[middle]) / 2 #finds avg of two middle elements if list is even
else:
    median = SortedList[middle] #if list is odd
print(f"\nMedian is: {median}")



points_per_game = [12.8, 2.3, 2.5, 10.6, 0.0, 11.8, 11.3, 5.8, 4.7, 10.8, 17.3, 0.0, 5.9]
start = float(input("Enter the starting value: "))
end = float(input("Enter the ending value: "))


for i in range(len(points_per_game)):#replace all values in range with 0 and iterate
    if start <= points_per_game[i] <= end:
        points_per_game[i] = 0

#the modified list
print("\nModified list:")
print(points_per_game)
