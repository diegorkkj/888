x = "n"

while x !="y":
    
    x = 4

    if 8 > x:
        print ("8 é maior")
    else:
        print ("8 é menor")

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"


