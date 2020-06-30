import sys

pprint = 'Teste local.'
print(pprint)
with open('..\\templates\\file.txt', 'w') as out:
    out.write(pprint)