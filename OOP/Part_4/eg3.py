class Movie:
    def start(self):
        print("Welcome")
    def interval(self):
        print("Interval , have coffee for Rs.50/-")
    def end(self):
        print("Thank you - Come again")
class JungleBook(Movie):
    def reelOne(self):
        print("Mowgli enters the jungle")
    def reelTwo(self):
        print("Bagheera saves mowgli")
j=JungleBook()
j.start()
j.reelOne()
j.interval()
j.reelTwo()
j.end()
print(JungleBook.mro())