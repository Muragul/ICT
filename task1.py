# 1. Mailing Address
print('Muragul Muratbekova \n Almaty, Kazakhstan')

# 2. Hello
name = input('What is your name?')
print('Hello, ', name)

# 3. Area of a Room
c = input('Enter units:')
a = input('Enter the width:')
b = input('Enter the length:')
s = float(a) * float(b)
print('Area of a room is', s, c)

# 4. Area of a Field
a = input('Enter length:')
b = input('Enter width:')
s = (float(a) * float(b)) / 43.560
print(s, 'acres')

# 5. Bottle Deposits
small = input('How much small containers?')
big = input('How much big containers?')
refund = float(small) * 0.1 + float(big) * 0.25
print("${:.2f}".format(refund))

# 6. Tax and Tip
cost = input('Enter cost:')
tax = 0.1 * float(cost)
tip = 0.18 * float(cost)
total = float(cost) + tax + tip
print('Tax: {:.2f}, Tip: {:.2f}, Total: {:.2f}'.format(tax, tip, total))

# 7. Sum of the First n Positive Integers
n = int(input())
sum = ((n + 1) * n) / 2
print(sum)

# 8. Widgets and Gizmos
widget = int(input('Enter widget count'))
gizmo = int(input('Enter gizmo count'))
print(widget * 75 + gizmo * 112, 'grams')

# 9. Compound Interest
money = float(input('Enter cash'))
for n in [1, 2, 3]:
    money += 0.04 * money
    print(n, 'year:', '{:.2f}'.format(money))

# 10. Arithmetic
import math

a = int(input('a:'))
b = int(input('b:'))
print('sum:', a + b, '\n', 'dif:', a - b, '\n', 'product:', a * b, '\n', 'quotient:', a / b)
print('remainder:', a % b, '\n', 'log:', math.log10(a), '\n', math.pow(a, b))

# 11. Fuel Efﬁciency
mpg = float(input('MPG:'))
print(235.214583 / mpg)

# 12. Distance Between Two Points on Earth
import math

t1 = math.radians(float(input('latitude 1:')))
g1 = math.radians(float(input('longitude 1:')))
t2 = math.radians(float(input('latitude 2:')))
g2 = math.radians(float(input('longitude 2:')))
distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(distance, 'km')

# 14. Height Units
feet = float(input('enter feet:'))
inch = float(input('enter inch:'))
print((feet * 12 + inch) * 2.54, 'cm')

# 15. Distance Units
feet = float(input('enter feets:'))
print('inches:', feet * 12)
print('yards:', feet * 0.333333)
print('miles:', feet * 0.000189394)

# 16. Area and Volume
import math

r = float(input('enter radius:'))
print('Area:', math.pi * r * r, '\n Volume:', math.pi * r * r * r * 4 / 3)

# 17. Heat Capacity
m = float(input('enter water amount:'))
dt = float(input('enter temperature change:'))
q = m * dt * 4.186
print(q, 'Joules')
cost = q / 3600000 * 8.9
print(cost, 'cents')

# 18. Volume of a Cylinder
import math

r = float(input('enter radius:'))
h = float(input('enter height:'))
V = math.pi * r * r * h
print('{:.1f}'.format(V))

# 19. Free Fall
h = float(input('enter height: '))
print(2 * 9.8 * h, 'm/s')

# 20. Ideal Gas Law
P = float(input('Pressure: '))
V = float(input('Volume: '))
T = float(input('Temperature: '))
n = (P * V) / (T * 8.314)
print(n)

# 21. Area of a Triangle
b = float(input('Enter base: '))
h = float(input('Enter height: '))
print('Area:', b * h / 2)

# 22. Area of a Triangle (Again)
import math

a = float(input('Side 1: '))
b = float(input('Side 2: '))
c = float(input('Side 3: '))
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)

# 23. Area of a Regular Polygon
import math

s = float(input('Enter side: '))
n = float(input('Enter number of sides: '))
area = (n * s * s) / (4 * math.tan(math.pi / n))
print(area)

# 24. Units of Time
d = int(input('Days: '))
h = int(input('Hours: '))
m = int(input('Minutes: '))
s = int(input('Seconds: '))
total = ((d * 24 + h) * 60 + m) * 60 + s
print(total, 'seconds')

# 25. Units of Time (Again)
total = int(input('Enter seconds: '))
d = total // 86400
total %= 86400
h = total // 3600
total %= 3600
m = total // 60
total %= 60
if h // 10 < 1:
    hh = '0' + str(h)
if m // 10 < 1:
    mm = '0' + str(m)
if total // 10 < 1:
    ss = '0' + str(total)
print('{0}:{1}:{2}:{3}'.format(d, hh, mm, ss))

# 26. Current Time
import time

print(time.asctime())

# 27. Body Mass Index
print('Choose units: \n (1) inches, pounds \n (2) meters, kilograms')
n = int(input())
h = float(input('Enter height: '))
w = float(input('Enter weight: '))
if n == 1:
    BMI = (w * 703) / (h * h)
else:
    BMI = w / h / h
print(BMI)

# 28. Wind Chill
import math

Ta = float(input('Temperature: '))
V = float(input('Speed: '))
WCI = 13.12 + 0.6215 * Ta - 11.37 * math.pow(V, 0.16) + 0.3965 * Ta * math.pow(V, 0.16)
print(round(WCI))

# 29. Celsius to Fahrenheit and Kelvin
t = float(input('Temperature in C: '))
print('Fahrenheit: ', t * 9 / 5 + 32)
print('Kelvin: ', t + 273.15)

# 30. Units of Pressure
p = float(input('Pressure in kilopascals: '))
print(p / 6.895, 'pounds per square inch')
print(p * 7.501, 'milimeters of mercury')
print(p / 101, 'atm')

# 31. Sum of the Digits in an Integer
number = int(input())
sum = 0
for i in range(4):
    sum += number % 10
    number //= 10
print(sum)

# 32. Sort 3 Integers
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
mini = min(a, min(b, c))
maxi = max(a, max(b, c))
print(mini, a + b + c - mini - maxi, maxi)

# 33. Day Old Bread
n = float(input('Number of loaves: '))
sum = n * 3.49
discount = sum * 0.6
total = sum * 0.4
print('Regular {:.2f} \n Discount {:.2f} \n Total {:.2f}'.format(sum, discount, total))