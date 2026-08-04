# Pythonic

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Non-Pythonic approach
i = 0
new_list = []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Half-Pythonic approach
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Pythonic approach
# This would be read as:
# first name -> what is being saved.
# after for -> element being iterated.
# after if -> condition that must be met for the element to be saved.
best_list = [name for name in names if len(name) >= 6]
print(best_list)

# Range()

# range(start, stop, step)
nums = range(0, 11)
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
# * unpacks the object into a list, this means it is like doing list(range(1,12,2))
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

# Enumerate()

# enumerate(start, stop, step)
letters = ['a', 'b', 'c', 'd', 'e']
indexed_letters = enumerate(letters)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)

# Enumerate non-Pythonic approach
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Enumerate Pythonic approach
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Enumerate Pythonic approach with unpacking
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

# Map()

nums = [1.5, 2.5, 3.5, 4.5, 5.5]
rnd_nums = map(round, nums)
print(list(rnd_nums))

nums = [1, 2, 3, 4, 5]
sqrd_nums = map(lambda x: x**2, nums)
print(list(sqrd_nums))

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Unpack names_map into a list
names_uppercase = [*names_map]

print(type(names_map))
print(names_uppercase)

# NumPy

import numpy as np

nums = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]
nums = np.array(nums)

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

# All Together.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

welcome_guest = lambda guest_time: f"Welcome {guest_time[0]}! Your table will be ready at {guest_time[1]} minutes."
# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')