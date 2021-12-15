# read file with number list
f = open('num_list.txt', 'r')

increase_count = 0
content = f.readlines()
length_of_f = len(content)

# get first number
num_1 = int(content[0])
# print(num_1)

# loop through file
for x in range(1, length_of_f):
# get second number
  num_2 = int(content[x])
  # print(num_2)
  
  difference = num_1 - num_2
  # print(difference)

# compare first number to second number, if there is a negative difference, add to increase count, compare to next number
  if difference <= -1:
    increase_count += 1
    num_1 = num_2
    # print(num_1)

# if there is a positive difference, compare to next number
# print the increase count
  else:
    num_1 = num_2
    # print(num_1)

print(str(increase_count))