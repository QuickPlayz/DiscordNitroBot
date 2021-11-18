import random
import webbrowser

url = 'https://discord.gift/'

rnd = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(24)))

print('Made by @QuickPlayz_ on Github')
print('-------------------------')
print('Would you like to show or open the link')
print('1=Print/2=Open')
print('-------------------------')
I = input()

if I == '1' :
    print("".join([url , rnd ]))
    quit()
    
if I == '2' :
    webbrowser.open("".join([url , rnd ]))
    quit()


quit()
