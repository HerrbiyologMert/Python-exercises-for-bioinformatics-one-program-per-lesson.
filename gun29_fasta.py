diziler = {}
ad = ""
with open("ornek.fasta") as dosya :
    for satir in dosya:
        satir = satir.strip()
        if satir.startswith(">"):
            ad = satir[1:]
            diziler[ad] = ""
        else:
            diziler[ad] = diziler[ad] + satir
for ad in diziler :
    print(ad,len(diziler[ad]),diziler[ad])
