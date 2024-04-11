#Some of the cool things we can do with list methods

food = ["Tacos", 'Pizza', 'Tiramisu']

print(food)

#-- list.append() : adds item to the end of a list

print('Adding Ice Cream')
food.append('Ice Cream')
print(food)

#-- list.insert(idx, item) : adds an item to a specific index
#If you try to add to an index out of range, it will just put it at the end
print('Inserting Potato into the 3rd position')
food.insert(2, 'Potato')
print(food)

#-- list.remove(item) : removes the first occurance of an item
#-- will give ValueError if item doesn't exist in list (case sensitive)
print('Eating all the Pizza (removing)')
food.remove('Pizza')
print(food)

#-- list.pop() : removes and returns the last item in the list
# just because it returns a value doesn't mean I have to collect the value in a variable
print('Popping ice cream into the freezer')
freezer = food.pop()
print('Freezer:', freezer)
print(food)

#-- list.pop(idx) : removes the item at a certain index
#can run into IndexError if you grab an index out of range
print('Popping potato into oven')
oven = food.pop(1)
print('Oven:', oven)
print(food)


#Hitting the grocery store
food.append('Burger')
food.append('Cheese')
food.append('Salad')
food.append('Sushi')
food.append('Burger')
food.append('Key Lime Pie')

print('Hit the store!')
print(food)


#-- list.index(item) : will return the index of a particular item

print('Finding the position of Salad using .index().')
salad_idx = food.index('Salad')
print('Salad position:', salad_idx)


#-- Modify the values at a particular postion/index MUTABILITY list[index] = new_item
print('Spicing up our Salad.')
food[4] = 'Caesar Salad'
print(food)

#-- list.count(item) : will count the occurances of an item in a list, returns an int

print('Counting Burgers!')
burg_count = food.count('Burger')
print('Burger Count:', burg_count)

#-- list.reverse() : will revers the order of your list

print('Flipping my list with .reverse()')
food.reverse()
print(food)

#-- list.sort() : will sort your list in ascending / alphabetical order
#When sorting a list, all list items need to be of the same type
print('Sorting in abc order')
food.sort()
print(food)

#-- list.sort(reverse=True) : reverse sort, descending / zyx order

print('Sorting in zyx order.')
food.sort(reverse=True)
print(food)

#-----List Functions

#-- len() : returns the length of the list aka how many items in the list

print('Length of Food List:',len(food))


#-- sum() : give the sum total of all the numbers in a list
#list must be entirely made of ints and/or floats

nums = [1,2,3,4,5,6.4]
total = sum(nums)
print('Sum of nums list:', total)


#--- SORTING OUT A MESS

mess = [ False, True, False]
mess.sort()
print(mess)