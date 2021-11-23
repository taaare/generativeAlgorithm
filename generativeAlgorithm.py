import random

base = []
dimension = []
dimension2 = []
frequency = []
frequency2 = []
mechanics = []
efficiency = []
finish = []
for x in range(0, 10000):
    baseRandom = random.randint(0,100)
    dimensionRandom = random.randint(0,1)
    dimensionRandom2 = random.randint(0,100)
    frequencyRandom = random.randint(0,100)
    frequencyRandom2 = random.randint(0,100)
    mechanicsRandom = random.randint(0,100)
    efficiencyRandom = random.randint(0,100)
    finishRandom = random.randint(0,100)
    if baseRandom <= 40:
        base.append("BG1")
    elif baseRandom <= 70:
        base.append("BG2")
    elif baseRandom <= 85: 
        base.append("BG3")
    elif baseRandom <= 95: 
        base.append("BG4")
    elif baseRandom <= 98: 
        base.append("BG5")
    elif baseRandom > 98:
        base.append("BG6")
    if dimensionRandom == 0:
        dimension.append("C")
    elif dimensionRandom == 1:
        dimension.append("P")
    if dimensionRandom2 <= 35:
        dimension2.append("B")
    elif dimensionRandom2 <= 60:
        dimension2.append("T")
    elif dimensionRandom2 <= 80: 
        dimension2.append("O")
    elif dimensionRandom2 <= 95: 
        anotherRandom = random.randint(0,2)
        if anotherRandom == 0:
            dimension2.append("BT")
        elif anotherRandom == 1: 
            dimension2.append("BO")
        elif anotherRandom == 2:
            dimension2.append("TO")
    elif dimensionRandom2 > 95: 
        dimension2.append("BTO")
    if frequencyRandom <= 50:
        frequency.append("CON")
    elif frequencyRandom <= 80: 
        frequency.append("CUR")
    elif frequencyRandom > 80:
        frequency.append("ORG")
    if frequencyRandom2 <= 50:
        frequency2.append("D1")
    elif frequencyRandom2 <= 80: 
        frequency2.append("D2")
    elif frequencyRandom2 > 80:
        frequency2.append("D3")
    if mechanicsRandom <= 40:
        mechanics.append("S")
    elif mechanicsRandom <= 65:
        mechanics.append("P")
    elif mechanicsRandom <= 85:
        mechanics.append("F")
    elif mechanicsRandom <= 95:
        mechanics.append("T")
    elif mechanicsRandom > 95:
        mechanics.append("G")
    if efficiencyRandom > 10:
        efficiency.append("ED")
    else:
        efficiency.append("SS")
    if finishRandom <= 40: 
        finish.append("S")
    elif finishRandom <= 50:
        minedRandom = random.randint(0,100)
        if minedRandom <= 50:
            finish.append("MS")
        elif minedRandom <= 80:
            finish.append("MG")
        elif minedRandom <= 81:
            finish.append("MD")
        elif minedRandom > 81:
            finish.append("MP")
    elif finishRandom <= 70:
        excavatedRandom = random.randint(0,100)
        if excavatedRandom <= 50:
            finish.append("ES")
        elif excavatedRandom <= 80:
            finish.append("EF")
        elif excavatedRandom > 80:
            finish.append("EM")
    elif finishRandom > 70:
        manufacturedRandom = random.randint(0,100)
        if manufacturedRandom <= 50:
            finish.append("MI")
        elif manufacturedRandom <= 80:
            finish.append("MC")
        elif manufacturedRandom > 80:
            finish.append("MA")
def listAttributes(x):
    print(base[x] + "-" + dimension[x] + "-" + dimension2[x] + "-" + frequency[x] + "-" + frequency2[x] + "-" + mechanics[x] + "-" + efficiency[x] + "-" + finish[x])
for x in range(10000):
    listAttributes(x)