# Exercise 5.1: print the total, count and average of input numbers
# Exercise 5.2: print the largest&smallest of the input numbers
inp = None
count = 0
total = 0
largest_num = None
smallest_num = None
while True:
    inp = input('Enter a number (enter done if you want to end): ')
    if inp == 'done':
        break;

    try:
        inp = int(inp)
    except Exception:
        print('Invalid input')
        continue
        
    count += 1
    total += inp
        
    if largest_num is None or largest_num < inp:
        largest_num = inp-1
        
    if smallest_num is None or smallest_num > inp:
        smallest_num = inp
    
            
print('total of the numbers:',total,'\n'
      'count of the numbers:',count,'\n'
      'average of the numbers:', total/count)

print('The largest number is:', largest_num)
print('The smallest number is:', smallest_num)

        
    
    


