# comment
class animal:
    voice = ''
    ration = ''

    def make_voice(self):
        print(self.voice)
        

class bird(animal):
    ration='Зерно'
    fly = None

class mammals(animal):
    ration='Трава'

class cow(mammals):
    voice='Му'
    
    def get_milk(self,r,c):# r-рацион,c-количество травы. Возвращает n - литров молока по формуле n=c/2
        if r==self.ration: 
            return c/2
        else:
            return 'Я не ем '+ r

        

    

class sheep(mammals):
    voice='Бееее'
    max_wool=5
    def get_wool(self,c):
        if c<=self.max_wool:
            return 'Вот '+ str(c) +'килограмм шерсти'
        else:
            return "У меня нет "+ str(c) + ' килограмм шерсти. Вот только '+str(self.max_wool)+' килограмм'  
        

class pig(mammals):
    voice='Хрю'

class goat(mammals):
    voice='Меее'

class duck(bird):
    voice='Кря'
    fly=True

class chicken(bird):
    voice='Кукареку'
    eggs=0
    
    fly=False
    def get_egg(self):
        if self.eggs==0 :
            self.eggs+=1
            return 1
        else: return "Я сегодня уже давала яйца"
        
    

class gees(bird):
    voice='Гага'
    fly=True

d1=duck()
d1.make_voice()
c1=cow()
print('Получено молока,л:',c1.get_milk('Трава',10))
print(c1.get_milk('Покрышки',10))
ch=chicken()
print(ch.get_egg())
print(ch.get_egg())


s1=sheep()
print(s1.get_wool(4))

print(s1.get_wool(20))



