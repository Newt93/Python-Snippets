# .format method for string interpolation
from tokenize import Name


print('My name is {}. I am {} years old. I am from {}'.format('Tyler', 'twenty-nine', 'Texas'))

# interpolation with indexing
print('The {2} {1} {0}'.format('fox','brown','quick'))

# interpolation with indexing and keywords
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# Width float formatting
result = 100/ 222
print("The result was {r:3.3f}".format(r=result))

# f-String
name = 'Tyler'
print(f'My name is {name}')

# .format benefits because it is more precise
# f-string is neater formatting