def bisection(fonksiyon, alt, ust):
    sayac=0
    yenikok=ust;
    if fonksiyon(alt)*fonksiyon(ust) > 0:
         print("Girdiğiniz aralıkta bir kök yok ya da bu yöntemle kökü bulamıyoruz")
         
    for iterasyon in range(4):
     
        sayac=sayac+1
        orta = (ust+alt)/2
        if fonksiyon(orta)*fonksiyon(ust) < 0:
            alt = orta
            yenikok=alt
        elif fonksiyon(orta)*fonksiyon(alt) < 0:
            ust = orta
            yenikok=ust

        print(sayac)    
    return orta 

def fonksiyon(x):
    return x**3 + 4*x**2 - 10

alt_sinir = 1
ust_sinir = 2

kok = bisection(fonksiyon, alt_sinir, ust_sinir)
print(f"Kök: {kok:.6f}")