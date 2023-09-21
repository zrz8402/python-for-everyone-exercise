# Exercise 6.4 practice using str.count(sub[, start[, end]])
word = 'banana'
letter = 'a'
print(word.count(letter))

# 6.4 practice find and substring
str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
sub = str[pos+1:]
num = float(sub)
print(num)


# Exercise 6.1 print s tring in reverse way
def reverse_string(string):
    index = len(string)
    while index > 0:
        letter = string[index-1]
        print(letter)
        index -=1
        
reverse_string('Hello')


# Exercise 6.3 count letters in a string
def count(string,letter):
    count = 0
    for char in string:
        if char == letter:
            count +=1
    return count

print(count('banana','a'))
print(count('banana','c'))


