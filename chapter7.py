import sys
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Close the file before attempting to read it again
fhand.close()

# When you read the contents of the file using fhand.read(), the file cursor moves to the end of the file, 
# so if you try to read from fhand again in the loop or after fhand.read(), you won't get any content 
# because the cursor is already at the end of the file.

# Reopen the file to read its contents
fhand = open('mbox.txt')
inp = fhand.read()
print('Character Count:', len(inp))
print('First 20 characters:', inp[:20])

# Close the file when you're done with it
fhand.close()


fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
fhand.close()

# Same result
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
fhand.close()

count = 0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.find('@uct.ac.za')==-1:
        count += 1
        continue
print(count)
fhand.close()

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    sys.exit()
count = 0 
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count,'subject lines in',fname)
fhand.close()


fout = open('output.txt', 'w')
print(fout)
line1 = "This here's the wattle, \n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)
fout.close()

s = '1 2\t 3\n 4'
print(s)
print(repr(s))



