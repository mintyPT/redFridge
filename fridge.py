import json

class fridge(object):

    def __init__(self):
        self.json = {}

    def open(self):
        try:
            f = open("fridge.json","r")
            self.json = json.load(f)
            f.close()
        except:
            self.json = {}
    
    def add(self, product, amount):
        if self.json.has_key(product):
            self.json[product] += amount
        else:
            self.json.update({product : 0})
            self.add(product, amount)

    def show(self):
        print 'In the fridge, you have:'
        if(len(self.json)) != 0:
            for product in self.json:
                print '\t+', product+':', self.json[product]
        else:
            print '\tNothing!'

    def close(self):
        from StringIO import StringIO
        jfridge = StringIO()

        json.dump(self.json, jfridge)
        f = open("fridge.json", "w")

        #f.write(jfridge)
        f.write(jfridge.getvalue())
        f.close()

        self.clear()

    def clear(self):
        self.json.clear()
    
    def amountOf(self, product):
        print product, "-->", self.json[product]

    def sub(self, product):
        if(self.json[product]>=1):
            self.json[product] -= 1


def shop(fridge):
    fridge.add('Beer',6)
    fridge.add('Coca Cola 1.5l',1)
    fridge.add('Cheese',1)



    



# For testing purposes
a = fridge()
a.open()
a.show()
