import sys

if len(sys.argv)< 3:
    print("This program needs 2 arguments separated by spaces")
    print("The first is the price, the second is the tax rate")
    print*"Example: python tax.py 10 0.05"
    sys.exit()

price = float(sys.argv[1])
tax = float(sys.argv[2])

print(f"""Price: {price:10.2f} 
Taxes: {price * tax:10.2f} 
Total: {price + price*tax:10.2f}""")