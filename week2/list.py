# testing list
list1 = [1,2,3,4,5,6]

## list comprehension
#list1 = [x*2 for x in list1 if x <3 ]
#print(list1)

def print_first_and_last_name(full_name) :
    full_name = full_name.split()
    first_name = full_name[0]
    last_name = full_name[1]
    return (first_name, last_name)
#first_name_and_last_name("eugene idan")
