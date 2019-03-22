

class Player(object):
    '''
    Usage: player = Player(name, level, health, maxHealth, XP, Quests, Inventory)
    '''
    def __init__(self, _name, _level, _HP, _maxHP, _xp, _quests, _inv):
        self.name = _name
        self.level = _level
        self.health = _HP
        self.maxHealth = _maxHP
        self.xp = _xp
        self.quests = _quests
        self.inventory = _inv

    def damage(self, _amount):
        pass

    def attack(self, _target, _loot):
        pass

    def pickUp():
        pass
