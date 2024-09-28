# The Fridge

"""

Get the user to enter a temperature in celsius.

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"

"""


# Version 1
"""
temp = float(input("temperatrure in celcius: "))

if temp < 0:
    print("Fridge too cold")
elif temp >= 0 and temp < 4:
    print("Fridge OK")
elif temp >= 4 and temp < 6:
    print("Fridge too warm")
elif temp > 6:
    print("Fridge broken")
"""

# Version 2
STATUS_BROKEN = "Fridge is broken."
STATUS_OK = "Fridge OK."
STATUS_WARM = "Fridge is too warm."
STATUS_COLD = "Fridge is too cold."
status = STATUS_BROKEN

temp = float(input("Enter the fridge temperature: "))

if temp < 0:
    status = STATUS_COLD
elif temp <= 4:
    status = STATUS_OK
elif temp <= 6:
    status = STATUS_WARM

print(status)