def bisection(fonksiyon, alt, ust, iterasyon_sayisi):
    
    if fonksiyon(alt)*fonksiyon(ust) > 0:
         print("Girdiğiniz aralıkta bir kök yok ya da bu yöntemle kökü bulamıyoruz")
    for iterasyon in range(iterasyon_sayisi):
        
        orta = (ust+alt)/2
        print(orta)
        if fonksiyon(orta)*fonksiyon(ust) < 0:
            alt = orta
        elif fonksiyon(orta)*fonksiyon(alt) < 0:
            ust = orta
    return orta

def fonksiyon(x):
    return x**3 - 2*x**2 - 5

alt_sinir = 2
ust_sinir = 4
iterasyon_sayisi = 4

kok = bisection(fonksiyon, alt_sinir, ust_sinir,iterasyon_sayisi)
print(f"Kök: {kok:.6f}")