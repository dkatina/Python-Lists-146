#Other cool things you can do with lists

#Membership checks using 'in' to check if an item is in a list, returns a boolean value

guest_list = ['Adam', 'Bob', 'Charlie', 'Dylan','Ethan']

print('Albert' in guest_list)
print('Dylan' in guest_list)

name = input('What is your name? ')

guest_list.append('Travis')

#if statements with membership checks
if name in guest_list:
    print('Welcome to the party', name)
else:
    print('Scrammmm! Punk')

#Merging two list with '+'

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = list_1 + list_2
print(list_3)

#Copying a list using .copy()
#making changes to the copy does not effect the original list
fruit = ['Apple', 'Orange', 'Banana']
copy_fruit = fruit.copy()
print(copy_fruit)
copy_fruit.pop()
print(copy_fruit)
print(fruit)

#Copying a list with a full slice [:]

fruit = ['Apple', 'Orange', 'Banana']
copy_fruit = fruit[:]
print(copy_fruit)
copy_fruit.pop()
print(copy_fruit)
print(fruit)

#Common mistakes when trying to make copies, setting one list = to another

nums = [1,2,3,4]
dnums = nums
print(dnums)
dnums.pop()
print(dnums)
print(nums)

#All this does is make two variable that point to the same value/ location in memory
#1 piece of data with 2 names



#Identiy operators 'is' and 'is not', returns a boolean value
#checking if to vars are pointing to the same location in memory


fruit = ['Apple', 'Orange', 'Banana']
copy_fruit = fruit[:]

print(fruit is copy_fruit)
print(fruit == copy_fruit)

nums = [1,2,3,4]
dnums = nums
print(dnums is nums)


#List slicing list[start:stop] : returns a sublist from the start index to the stop index
#default for start and stop are the beginning and end of the list
#the stop index is non-inclusive, meaning the item at the stop index wont be included in the slice

key_lime_pie = ['slice1','slice2','slice3','slice4']

my_slice = key_lime_pie[0:1]
print(my_slice)
big_slice = key_lime_pie[1:3] #item at stop index is not included
print(big_slice)
last_slice = key_lime_pie[3:] #sliceing to the end, can use -1
print(last_slice)


#Joing a list of strings ''.join(list)

words = ['Hello','Im','getting','joined!']

scentence = ' '.join(words)
print(scentence)