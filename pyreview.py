# Variables ex

length = 10
width = 5

area = length * width

print(f'Variables ex:\nthe length is {length} and the width is {width} so area = {area}')


# lists ex
fav_animals = ['dog', 'monkey', 'cat', 'rabbit']

fav_animals[3] = 'horse'

fav_animals.remove("cat")

fav_animals.append('Pepe')

print(f"lists ex:\n{fav_animals}")



#Functions ex
def cube(number):
    return number ** 3

def by_three(number):
    return cube(number) if number % 3 == 0 else False

print(f'Functions ex:\ncube output= {cube(3)} by_three output= {by_three(2)}')



#Functions extra:
def padel_court_cost(hours, court_type):
    cost_per_hour = 30 if court_type == "indoors" else 20

    return (cost_per_hour * hours) * 20/100  if hours >= 3 else cost_per_hour * hours

print(f"Functions extra:\n{padel_court_cost(3,'indoors')}")



#Functions & loops

# 1:
def printer(elements):
    for element in elements:
        print(f'{element}C')

        
# 2:
def to_celsius(temperatures):
    
    celsius_array = []
    for temperature in temperatures:
        celsius_array.append(round((temperature - 32) * (5/9)))

    return celsius_array

# outputs
array_of_temperatures = to_celsius([100,200,330,400])
print(f'Functions & loops:\n\n1:\n {array_of_temperatures}\n2:')
printer(array_of_temperatures)


# Functions advanced
print("Functions advanced:\n\n")



# secs to mins
def secounds_to_mins(secounds):
    return secounds / 60

print("secs to mins: ",secounds_to_mins(60))



# is odd ?
def is_odd(number):
    return True if number % 2 == 0 else False

print("is odd ?: ",is_odd(3))



# sum last and first from a list
def sum_last_first(elements):
    return elements[0] + elements[-1]

print("sum last and first from a list: ",sum_last_first([1,2,3,4,5,6,7,8,9,10]))




# is array length even?
def is_array_length_even(elements):
    
    return True if is_odd(len(elements)) is True else False

print('is array length even?:\n',is_array_length_even([1,2,4]))




# greatest score cooded assessment:
def return_greatest_score(elements):
    first_number = elements[0]
    greatest_number = first_number
    for element in elements:
        greatest_number = greatest_number if greatest_number >= element else element

    return(greatest_number)
            
print("greatest score cooded assessment:\n",return_greatest_score([1,3,5,6,1,2]))




# Sorts the list and finds the missing number
def check_if_there_is_missing_number(elements):
    sorted_list = sorted(elements)
    secound_number_index = 1

    for element in sorted_list:
        if secound_number_index == len(sorted_list) - 1:
            msg_to_user = 'The list is well sorted there is no missing number'
            break

        if element == sorted_list[secound_number_index] - 1:
            secound_number_index +=1

        else:
            msg_to_user = f'There is a missing number which is {element + 1}'
            break
    
    return msg_to_user


print("Sorts the list and finds the missing number:\n",check_if_there_is_missing_number([1,2,3,4,5,6,8,9,10]))