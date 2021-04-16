#recursion
#n! =1*2*3*4*5...n
#n! =#n! =[1*2*3*4*5...n-1]*n
#n! =(n-1)! *n
'''n = 4
product =1
for i in range(n):
    product = product * (i + 1)

print(product)    
    '''
#wrapping in function

'''def fac_iteration(n):
    product =1
    for i in range(n):
        product = product * (i + 1)
    return product

a = fac_iteration(4)
print(a)
'''
def fac_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * fac_recursive(n - 1)

b = fac_recursive(1)
print(b)