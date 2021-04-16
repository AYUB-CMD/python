# greatest of three num
'''def maxum(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
           if (num2 > num3):
            return num2
           else:
            return num3

m = maxum(3, 6, 4)
print(str(m)) '''

#2 covert to celsiuis to fahernite
#formula = (0°C × 9 / 5) + 32 = 32°F
'''def farh(cel):
    return (cel*(9/5)) + 32 
c = 45
f=farh(c)
print(f)
'''

#3
'''print("hey", end = " ")
print("hello", end = " ")
print("hi", end=" ") '''

#4
#formula = sum(n)= sum(n-1)+n❌
#n(n+1)/2

'''def sum(n):
    if n == 0 or n == 1:
        return 1
    s =n*( n + 1) / 2
    return s

num = sum(4)
print(num)
'''
#5
'''
***
**
* '''
'''n = 6
for i in range(n):
    print("*" * (n - i)) #print * n-i times
    '''

#6
#  convert inch into cms   Formula	multiply the length value by 2.54
'''def length(inch):
    convert = inch * 2.54
    return convert

len = 5
cms = length(len)

print(f" length is {len}inchs = {cms}cm")

'''

#7 strip

'''def remove_and_strip(string,word):
    newsttr = string.replace(word, "")
    return newsttr.strip()

this = "     ayub is goood boy     nigga     "
change = remove_and_strip(this, "nigga")
print(change) '''

#8

def mul_table(num):
    for i in range(11):
       b = print(f"{num}x{i}={i*num}")
      
n = int(input("enter the number"))    
a = mul_table(n)   
print(a)



