# Author: JAp (amdg) 12/9/20


# hw 3-3#1

def thermostat():
    f_temp = input("Tempature in fahrenheit")
    c_temp = (float(f_temp) - 32) * 5 / 932
    print(c_temp)


print(thermostat())

# Plug in 50, you get .0965; Plug in 90 ypi get 0.25751; Plug in 60 = 0.15
