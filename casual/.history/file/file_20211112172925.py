f_name = 'test.txt'
f = None
try:    
f = open('test.txt')
content = f.read()
print(content)
f.close()
