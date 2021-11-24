f_name = 'test.txt'
f = None
try:    
    f = open(f_name)
    print
content = f.read()
print(content)
f.close()
