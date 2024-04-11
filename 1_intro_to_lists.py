#List in python are collections of items and are; mutable, ordered, and have dynamic sizing
#lists are another datatype in python

#-- ordered: each item has a position, which allows me to know where each item is
#-- mutable: the ability to mutate lists, add, remove, manipulate
#-- dynamic size: add and remove froms list allowing them to grow and shrink

#Lists are created with square brackets '[]' and each item is separated by ','

#empty list

empty_list = []

#populated list
person = 'Jill'

people = ['Bob', 'Barry', 'Bernie', 'Bill', person]

#python list can hold a variety of different

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis', ['tacos']]]

print(stuff[4][-1][0])

#another thing, we can have duplicate items in list

toppings = ['pepperoni', 'pepperoni', 'pepperoni']


#--- LIST INDEX

#each item has a position marked by an index
#indices are in numeric order starting from 0, we use indices to access, modify,
# and remove items from our list


#indices    0       1       2       3
alist = ['item1','item2','item3','item4']
print(alist)

#grabbing item 3 at idx 2
print('third item', alist[2])
#grabbing item 1 at idx 0
print('first item', alist[0])

#grabbing the last item
print('last item', alist[3])

#grabbing the last item with idx -1
print('last item', alist[-1])


#potentila pitfalls

#IndexError
#-- index out of range, trying to access an index that doesnt exist

# print(alist[4])