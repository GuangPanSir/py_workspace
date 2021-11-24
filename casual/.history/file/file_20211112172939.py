f_name = 'test.txt'
f = None
try:    
    f = open(f_name)
    
content = f.read()
print(content)
f.close()
