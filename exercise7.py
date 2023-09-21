# Exercise 7.1
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    ln = line.rstrip()
    print(ln.upper())
fhand.close()
    
# Exercise 7.2
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
total = 0
average = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        colon_pos = line.find(':')
        extracted_num = float(line[colon_pos+1:])
        total += extracted_num
        count += 1
fhand.close()
average = total/count
print('Average spam confidence:',average)

# Exercise 7.3
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        print('File cannot be opened:',fname)
finally:
    # Ensure the file is closed, whether an exception occurred or not
    if 'fhand' in locals():
        fhand.close()

