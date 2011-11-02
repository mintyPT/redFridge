import json


def load():
    try:
        f = open("fridge.json","r")
        fridge = json.load(f)
        f.close()
    except :
        fridge = {}
    return fridge



def open_fridge(product, action, amout):
    if(not(fridge.has_key(product)) and action != "sub"):
        fridge.update({product : 0})
        add_product(product)
    else:
        if action == "add":
            for i in range(amount):
                add_product(product)
            save(fridge)
        elif action == "sub":
            for i in range(amount):
                sub_product(product)
            save(fridge)
        else:
            return "Command not recognised!"

def add_product(product):
    if fridge.has_key(product):
        fridge[product] += 1
    else:
        fridge.update({product : 0})
        add_product(product)
    message = product + " added!"
    return  message

def sub_product(product):
    if(fridge[product]>=1):
        fridge[product] -= 1
        message = product + " subtracted!"
    else:
        message = "No more product to subtract!"
    return message

def save(fridge):
    from StringIO import StringIO
    jfridge = StringIO()

    json.dump(fridge, jfridge)
    f = open("fridge.json", "w")

    #f.write(jfridge)
    f.write(jfridge.getvalue())
    f.close()
    return "saved!"

def clear(fridge):
    fridge.clear()
    save(fridge)


def get_amount(product):
    message = product, "-->", fridge[product]
    return message


fridge = load()
print "Fridge opened!"



