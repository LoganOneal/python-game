

class Inventory(object):
    '''
    Usage: inventory = Inventory()
           inventoryu.addItem(Item('Sword', 5, 1, 15, 2))
           print(inventory)
    '''
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        self.items[item.name] = item

    def __str__():
        out = '\t'.join(['Name','Atk', 'Arm', 'Lb', 'Val'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]])
        return out


