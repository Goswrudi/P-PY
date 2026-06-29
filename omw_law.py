# Simulating oms law in python 

# The three formula are :
# Find Voltage: V = I × R
# Find Current: I = V/R
# Find Resistance: R = V/I


# find voltage

name = input('Enter your name : ')
print(f'Welcome Dear {name}')


def volt():
    current = float(input('enter the exact current flow '))
    resistance = float(input('enter the exact resistance flow '))
    print(f'Your current is {current}:amps , and resistance is {resistance}:omw')
    voltage = current * resistance
    print(f'Your Voltage is {voltage}volt')
    
volt()



def Current():
    voltage = float(input('enter the exact voltage '))
    resistance = float(input('enter the exact current '))
    print(f'your Current voltage is {voltage}volt , and current is {resistance}omw ') 
    current = voltage / resistance
    print(f'your Current is {current}amps') 

Current()
