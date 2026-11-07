# ===== GEN ANALİZ HATTI (Günler 14-26) =====

kodon_tablosu = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "Dur", "TAG": "Dur",
    "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys", "TGA": "Dur", "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}
def gc_hesapla(dna):
    g= dna.count("G")
    c = dna.count("C")
    return (g + c) / len(dna) * 100
def ters_tumleyen(dna):
    tamamlayici = {"A":"T","T":"A","G":"C","C":"G"}
    sonuc = ""
    for baz in dna:
        sonuc = sonuc + tamamlayici[baz]
    return sonuc[::-1]
def gen_bul(dna):
    konum = dna.find("ATG")
    if konum == -1:
        return ""
    return dna[konum:]
def cevir(gen):
    protein = []
    i = 0
    while i + 3 <= len(gen):
        kodon = gen [i:i+3]
        aminoasit = kodon_tablosu[kodon]
        if aminoasit == "Dur":
            return protein
        protein.append(aminoasit)
        i = i + 3
    return protein
try :
    diziler = []
    with open("mrna_dizileri.txt") as dosya:
      for satir in dosya:
        dizi = satir.strip()
        if dizi !="":
            diziler.append(dizi)
    gen_sayisi = 0
    with open("gen_raporu.txt","w",encoding="utf-8")as rapor:
        for dizi in diziler:
            gc = round(gc_hesapla(dizi),1)
            gen = gen_bul(dizi)
            if gen == "":
                protein_yazi = " gen yok"
            else:
                protein_yazi = str(cevir(gen))
                gen_sayisi = gen_sayisi + 1
            karsi_zincir = ters_tumleyen(dizi)
            rapor.write(dizi + " | GC: " + str(gc) + " | " + protein_yazi + " | karşı zincir: " + karsi_zincir + "\n")
            print(dizi,"-",protein_yazi)
    print("Gen bulunan dizi sayısı:",gen_sayisi)
    print("Rapor hazır:gen_raporu.txt")
except FileNotFoundError:
    print("mrna_dizileri.txt bulunumadı,dosya adını kontrol et")                                      