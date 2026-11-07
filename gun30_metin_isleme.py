baslik = ">gen1|hasta_A|BRCA1"
parcalar = baslik[1:].split("|")
print(parcalar)

dna = "atgggctttaag"
dna = dna.upper()
print(dna)

mrna = dna.replace("T","U")
print(mrna)

protein = ["Met","Gly","Phe","Lys"]
print("-".join(protein))

gc = 41.666
print(f"{dna} için GC oranı:%{round(gc,1)}")
print(f"Uzunluk:{len(dna)}baz")

