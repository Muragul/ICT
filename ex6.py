# 6. Tax and Tip
cost = input('Enter cost:')
tax = 0.1 * float(cost)
tip = 0.18 * float(cost)
total = float(cost) + tax + tip
print('Tax: {:.2f}, Tip: {:.2f}, Total: {:.2f}'.format(tax, tip, total))
