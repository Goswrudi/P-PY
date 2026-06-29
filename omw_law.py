# Simulating oms law in python 

# The three formulas are :
# Find Voltage: V = I × R
# Find Current: I = V/R
# Find Resistance: R = V/I


# find voltage

name = input('Enter your name : ')
print(f'Welcome Dear {name}')

current = float(input('enter the exact current flow '))
resistance = float(input('enter the exact resistance flow '))

def formula():
    print(f'Your current is {current}:amps , and resistance is {resistance}:omw')
    voltage = current * resistance
    print(f'Your Voltage is {voltage}volt')
    
formula()
