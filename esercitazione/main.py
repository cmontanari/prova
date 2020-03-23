n = int(input("Inserisci un numero? "))
if n%2 == 0:
    print("numero pari")
    if n < 10:
        n+=1
        print(n)
    else:
        n-=1
        print(n)
else:
    print("numero dispari")
