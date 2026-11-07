# ===== HASTA DİZİSİ ANALİZ HATTI (Dersler 17-31) =====

# --- BLOK 1: Genetik kod çizelgesi ---
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

# --- BLOK 2: Makineler (tarifler, çağrılmadan çalışmaz) ---
def ters_tumleyen(dna):
    tamamlayici = {"A": "T", "T": "A", "G": "C", "C": "G"}
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
        kodon = gen[i:i+3]
        aminoasit = kodon_tablosu[kodon]
        if aminoasit == "Dur":
            return protein
        protein.append(aminoasit)
        i = i + 3
    return protein

def kodonlara_bol(gen):
    kodonlar = []
    for i in range(0, len(gen) - 2, 3):
        kodonlar.append(gen[i:i+3])
    return kodonlar

try:
    # --- BLOK 3: FASTA dosyasını sözlüğe oku ---
    diziler = {}
    ad = ""
    with open("hasta_fasta.fasta") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir.startswith(">"):
                ad = satir[1:]
                diziler[ad] = ""
            else:
                diziler[ad] = diziler[ad] + satir.upper()

    # --- BLOK 4: Referansı ve hastaları ayır ---
    referans = ""
    hasta_adlari = []
    for ad in diziler:
        parcalar = ad.split("|")
        if parcalar[0] == "referans":
            referans = diziler[ad]
        else:
            hasta_adlari.append(ad)

    # --- BLOK 5: Referansın özeti ---
    print("Referans uzunluğu:", len(referans))
    print("Hasta sayısı:", len(hasta_adlari))
    print("EcoRI kesim yeri (GAATTC) referansta var mı:", "GAATTC" in referans)

    ref_gen = gen_bul(referans)
    ref_yazi = "-".join(cevir(ref_gen))
    print("Referans kodonlar:", "-".join(kodonlara_bol(ref_gen)))
    print("Referans protein:", ref_yazi)
    print("Referans mRNA:", ref_gen.replace("T", "U"))

    ters_primer = ters_tumleyen(referans[-12:])
    print("Geri primer (son 12 bazın ters tümleyeni):", ters_primer)

    # --- BLOK 6: Her hasta, her pozisyon ---
    mutasyon_sayilari = []
    with open("hasta_raporu.txt", "w", encoding="utf-8") as rapor:
        for numara, ad in enumerate(hasta_adlari, start=1):
            hasta = diziler[ad]
            kod = ad.split("|")[1]
            mutasyon_sayisi = 0
            mutasyonlar = ""

            for i in range(len(referans)):
                if referans[i] != hasta[i]:
                    mutasyon_sayisi = mutasyon_sayisi + 1
                    mutasyonlar = mutasyonlar + f"{i + 1}. baz {referans[i]}>{hasta[i]}; "

            # --- BLOK 7: Protein etkisi ---
            gen = gen_bul(hasta)
            if gen == "":
                protein_yazi = "gen yok"
                etki = "protein yok"
            else:
                protein_yazi = "-".join(cevir(gen))
                if protein_yazi == ref_yazi:
                    etki = "protein aynı"
                else:
                    etki = "protein değişti"

            rapor.write(f"{numara}. kuyucuk | {kod} | mutasyon: {mutasyon_sayisi} | {mutasyonlar}| protein: {protein_yazi} | {etki}\n")
            mutasyon_sayilari.append(mutasyon_sayisi)
            print(f"{numara}. kuyucuk {kod}: {mutasyon_sayisi} mutasyon, {etki}")

    # --- BLOK 8: Kapanış ---
    print("Mutasyon sayıları (çoktan aza):", sorted(mutasyon_sayilari, reverse=True))
    print("Rapor hazır: hasta_raporu.txt")

except FileNotFoundError:
    print("hasta_fasta.fasta bulunamadı, dosya adını kontrol et")