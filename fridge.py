import json

class redFridge(object):

    json = {}

    def __init__(self, filename="fridge.json"):
        self.filename = filename
        try:
            f = open(self.filename, "r")
            self.json = json.load(f)
            f.close()
        except:
            self.json = {}
    
    def add(self, product, amount):
        if self.json.has_key(product) == False:
            self.json.update({product : 0})
        self.json[product] += amount

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

    def sub(self, product, amount):
        if(self.json[product]>=amount):
            self.json[product] -= amount
        else:
            self.json[product] = 0
