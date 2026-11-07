kodon_tablosu = {"ATG": "Met", "GGC": "Gly", "TTT": "Phe", "AAG": "Lys",
                 "TGA": "Dur", "TAA": "Dur", "TAG": "Dur"}
def gc_hesapla(dna):
    g = dna.count("G")
    c = dna.count("C")
    return (g+c) / len (dna) * 100
def cevir(dna):
    protein = []
    i = 0
    while i + 3 <= len(dna):
        kodon = dna [i:i+3]
        aminoasit = kodon_tablosu[kodon]
        if aminoasit == "Dur":
            return protein
        protein.append(aminoasit)
        i = i + 3
    return protein
try:
    numune_listesi = []
    sonuclar = {}
    yüksek_sayisi = 0
    with open("hasta_numuneleri.txt")as dosya :
        for satir in dosya:
            numune = satir.strip()
            if numune !="":
                numune_listesi.append(numune)
    print("Numune sayısı:",len(numune_listesi))
    print("İlk numune küçük harf:", numune_listesi[0].lower())
    print("Son numune:",numune_listesi[-1])
    with open("analiz_raporu.txt", "w", encoding="utf-8") as rapor:
        for numune in numune_listesi:
            gc=round(gc_hesapla(numune),1)
            sonuclar[numune] = gc 
            baslangic = numune [0:3]
            bitis = numune[-3:]
            if baslangic == "ATG" and gc >= 40:
               durum = "güçlü aday"
            elif baslangic == "ATG":
               durum = "aday ama GC düşük"
            else:
               durum = "aday değil"
            if bitis == "TAA" or bitis == "TAG" or bitis == "TGA":
                bitis_notu = "stop ile biter"
            else:
                bitis_notu = "stop yok"
            if  baslangic == "ATG":
               protein_yazi = str(cevir(numune))
            else:
               protein_yazi ="protein yok"
            if gc > 50:
               yüksek_sayisi = yüksek_sayisi + 1
            rapor.write(numune + " | GC: "+ str(gc) + " | "+ durum + " | " + bitis_notu + " | "+ protein_yazi + "\n") 
    for numune in sonuclar:
        print(numune,sonuclar[numune])
    print("GC oranı %50 üstü numune sayısı:", yüksek_sayisi)
    print("Rapor hazır:analiz_raporu.txt")
except FileNotFoundError:
    print("hasta_numuneleri.txt bulunumadı,dosya adını kontrol et")
          