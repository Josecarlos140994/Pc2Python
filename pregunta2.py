## Escriba un programa en Python para construir el siguiente patrón.
##
## *
## * *
## * * *
## * * * *
## * * * * *
## * * * *
## * * *
## * *
## *
##

h = 5

for i in range(1, h + 1):
    print("* " * i)

for i in range(h - 1, 0, -1):
    print("* " * i)







