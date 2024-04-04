class superhero:
    def __init__(self,name,nickname,superpower,health_point,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    def printt(self,*args,**kwargs):
        print (f'имя: {self.name}')

    def __len__(self):
        return len(self.catchphrase)

    def health(self, *args,**kwargs):
        return (self.health_point*2)

    def __str__(self):
        return (f'прозвише: {self.nickname}\n'
                f'супер способность: {self.superpower}\n'
                f'здоровье: {self.health(hero) }')



hero = superhero('Грут',
                 'Деревянный',
                 'быстрая регенерация, '
                 'очень большая физическая сила, '
                 'умеет управлять деревьями',
                  700,
                 'я есть грут')
hero.printt()
print(hero)
print(len(hero))
class alliens(superhero):
    damage = 300

    def printt(self,*args,**kwargs):
        print (f'имя: {self.name}')
    def __init__(self,name,nickname,superpower,health_point,
                 catchphrase,damage,view,fly=False):
        super().__init__(name,nickname,superpower,health_point,catchphrase)
        self.damage = damage
        self.fly = fly
        self.view = view

    def try_catch(self):
        print(f'true in the true_phrase')

    def health1(self):
        self.health_point **= 2
        self.fly = True

    def __str__ (self):
        return (f'{super().__str__()} \n'
                f'{self.damage}\n'
                f'{self.fly}\n'
                f'{self.view}')


hero2 = alliens('грут',
                'деревянный',
                'управляет деревьями',
                7000,' ',
                240,'инопланетянен',
                True

                )
hero2.printt()
print(hero2)
hero2.try_catch()
hero2.health1()

class flora_colosus(superhero):

    def printt(self,*args,**kwargs):
        print (f'имя: {self.name}')
    def __init__(self, name, nickname, superpower, health_point,
                 catchphrase, damage,live ,fly=False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)
        self.damage = damage
        self.fly = fly
        self.live = live

    def try_catch1(self):
        print('true in the true_phrase')

    def health2(self):
        self.health_point **= 2
        self.fly = True

    def __str__(self):
        return (f'{super().__str__()} \n'
                f'{self.damage}\n'
                f'{self.fly}\n'
                f'{self.live}')


hero3 = flora_colosus(f'грут',
                'деревянный',
                'управляет деревьями',
                7000, ' '
                , 240, 'земля-199999',True
                )
hero3.printt()
print(hero3)
hero3.try_catch1()

class villain(alliens):
    people ='people'

    def printt(self,*args,**kwargs):
        print(f'имя: {self.name}')

    def __init__(self, name, nickname, superpower, health_point,
                 catchphrase,view,crit, fly=False):
        super().__init__(name, nickname, superpower, health_point, catchphrase,view,crit)
        self.fly = fly
        self.view = view
        self.crit = crit

    def gen_x(self):
        pass

    def super_crit(self):
        print (f'{super().damage + self.crit **2}')
villains = villain
villains.people = 'monsters'

# crits.super_crit = super(alliens.)
super_villains = villain('танос',
                         'танка',
                         'перчатка бесконечности',
                         50000,
                         'пока есть те кто помнит как было до,'
                         ' будут и те что не способны не какое после',
                         'инопланетянен',
                         2,
                         True,)
super_villains.printt()
print(super_villains)
super_villains.super_crit()
