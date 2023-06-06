from random import shuffle

suites = 'H D S C'.split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
points = {i:j for j,i in enumerate(ranks)}

class Deck():
    def __init__(self):
        self.deck = []
        for s in suites:
            for r in ranks:
                self.deck.append(s+r)
    
    def distribute_and_shuffle(self):
        # print(self.deck)
        shuffle(self.deck)
        # print(self.deck)
        half = int(len(self.deck)/2)
        a,b = self.deck[:half],self.deck[half:]
        return a,b
        
class Clash():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self,c,d):
        for i in c:
            d.append(i)
        
    def war(self,d1,d2,c= []):
        c.append(d1.pop(0))
        c.append(d2.pop(0))
        p1,p2 = points[c[-2][1:]],points[c[-1][1:]]
        print(f"Matchup between p1 : {c[-2]} and p2: {c[-1]}" )
        if p1 != p2:
            if p1>p2:
                self.add(c,d1)
                print(f"p1 won the cards {c}")
                c = []
            else:
                self.add(c,d2)
                print(f"p2 won the cards {c}")
                c = []
        else:
            if(len(d1) < 4 or len(d2) < 4):
                if(len(d1) < len(d2)):
                    for el in d1:
                        d2.append(el)
                    for el in c:
                        d2.append(el)
                    d1 = []
                elif(len(d1) > len(d2)):
                    for el in d2:
                        d1.append(el)
                    for el in c:
                        d1.append(el) 
                    d2 = []
            else:
                for e in range(3):
                    c.append(d1.pop(0))
                    c.append(d2.pop(0))
                d1,d2 = self.war(d1,d2,c)
        return d1,d2
                
    def play(self):
        j = 300
        while (len(self.a) > 0 and len(self.b) > 0 and j >0 ):
            self.a,self.b = self.war(self.a,self.b,c=[])
            j -= 1
            print(len(self.a),len(self.b))

        if (len(self.a) == 0 or len(self.b) == 0):
          if(len(self.a) > len(self.b)):
            return("p1 won the game!!")

          else:
            return("p2 won the game!!")

        else:
          shuffle(self.a)
          shuffle(self.b)
          return self.play()
            
d = Deck()
p1,p2 = d.distribute_and_shuffle()
c = Clash(p1,p2)
print(c.play())