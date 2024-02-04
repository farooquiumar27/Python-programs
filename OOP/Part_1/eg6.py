class Bulb:
    def setWattage(j,e):
        j.wattage=e
    def getWattage(m):
        return m.wattage
k=Bulb()
print(k.wattage)
print("Wattage is : ",k.getWattage())
