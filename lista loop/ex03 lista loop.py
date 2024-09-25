a = 80000
b = 200000
anos = 0
while b >= a:
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)