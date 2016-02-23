class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class weapon(item):
    def __init__(self,name, description, damage):
        super(weapon, self).__init__(name, description)
        self.damage = damage
        
class throwing_weapon(weapon):
    def __init__(self, name, description, damage):
        super(throwing_weapon, self).__init__(name, description, damage)
        
    def throw(self):
        print 'You throw %s' % (self.name)

class sword(weapon):
    def __init__(self, name = 'A Sword', description = 'It is a basic sword', damage = 10):
        super(sword,self).__init__(name, description, damage)
        
    def swing(self):
        print 'You swing %s' % (self.name)

class consumable(item):
    def __init__(self, name, description, healing_value = 10, restore_value = 0):
        super(consumable, self).__init__(name, description)
        self.healing_value = healing_value
        self.restore_value = restore_value
        
    def consume(self):
        print 'You consume %s' % (self.name)
        print 'You get healed for %s' % (self.healing_value)

class clothing(item):
    def __init__(self, name, description, clothing):
        super(clothing, self).__init__(name, description)
        
class jutsu(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ninjutsu(jutsu):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class taijutsu(jutsu):
    def __init__(self, name, description):
        super(taijutsu, self).__init__(name, description)
    
class genjutsu(jutsu):
    def __init__(self, name, description):
        super(genjutsu, self).__init__(name, description)
        
class sagejutsu(jutsu):
    def __init__(self, name , description):
        super(sagejutsu, self).__init__(name, description)