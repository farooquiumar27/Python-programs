class Bulb:
    def setWattage(j,e):
        j.wattage=e
    def getWattage(m):
        return m.wattage
k=Bulb()
k.setWattage(60)
print("Wattage is : ",k.getWattage())

r=Bulb()
r.setWattage(100)
print("Wattage is : ",r.getWattage())
