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
sum = (n + 1) * n * 2
print(sum)

# 8. Widgets and Gizmos
widget = int(input('Enter widget count'))
gizmo = int(input('Enter gizmo count'))
print(widget*75+gizmo*112, 'grams')

# 9. Compound Interest
money = float(input('Enter cash'))
for n in [1, 2, 3]:
    money += 0.04*money
    print(n, 'year:', '{:.2f}'.format(money))

# 10. Arithmetic
import math

a = int(input('a:'))
b = int(input('b:'))
print('sum:', a + b, '\n', 'dif:', a - b, '\n', 'product:', a * b, '\n', 'quotient:', a / b)
print('remainder:', a % b, '\n', 'log:', math.log10(a), '\n', a * b)

# 11. Fuel Efﬁciency
mpg = float(input('MPG:'))
print(235.214583/mpg)

# 12. Distance Between Two Points on Earth
import math

t1 = math.radians(float(input('latitude 1:')))
g1 = math.radians(float(input('longitude 1:')))
t2 = math.radians(float(input('latitude 2:')))
g2 = math.radians(float(input('longitude 2:')))
distance = 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(distance, 'km')

