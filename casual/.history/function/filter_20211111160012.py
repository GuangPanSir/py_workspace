#
data=[1,2,3,4,5,6,7,8,9]
def f(x):
    return x > 6

filtered = filter(f,data) 
list = list(filtered)
print(list)