numuneler = ["H_001","H_002","H_003","H_004"]
gc_degerleri = [58.3,40.0,66.7,20,0]

print("H_003" in numuneler)
print("H_009" in numuneler)

for i in range(3):
    print("Tekrar",i)

for kuyu,numune in enumerate(numuneler,start= 1):
    print(f"Kuyucuk {kuyu}: {numune}")

print(sorted(gc_degerleri))
print(sorted(gc_degerleri,reverse=True))

dna = "CCATGGGCTTTAAG"
print("ATG"in dna)
print("GAATTC" in dna)    
          

