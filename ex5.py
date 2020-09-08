# 5. Bottle Deposits
small = input('How much small containers?')
big = input('How much big containers?')
refund = float(small) * 0.1 + float(big) * 0.25
print("${:.2f}".format(refund))
