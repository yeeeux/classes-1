from methods import acceleration as acceleration
from methods import stop as stop

class Car():

    def __init__(self, carName, maxSpeed):
        self.carName = carName
        self.maxSpeed = maxSpeed
        self.engine_status = 0
        self.run_status = 0
        self.cnt_of_srart_engine = 0
    
    def desc(self):
        description = "Car name: " + self.carName + '\n' + "max speed: " + str(self.maxSpeed) + ', число запусков двигателя: ' + str(self.cnt_of_srart_engine)
        return description

    def engine_start(self):
        if self.engine_status == 0:
            print('Автомобиль', self.carName, 'завёлся')
            self.engine_status = 1
            self.cnt_of_srart_engine += 1
        else:
            print('Автомобиль', self.carName, 'уже заведён')

    def engine_stop(self):
        if self.engine_status == 1:
            print('Автомобиль', self.carName, 'заглушен')
            self.engine_status = 0
        else:
            print('Автомобиль', self.carName, 'уже был заглушен')

    def acceleration(self):
        if self.engine_status == 1:
            print('Поiхали')
            self.run_status = 1
        else:
            print('Автомобиль', self.carName, 'не заведён')
    
    def stop(self):
        if self.run_status == 1:
            print('Останавливаемся')
        else:
            print('Мы и так стоим')

class Toyota(Car):
    def __init__(self, carName, maxSpeed):
        super().__init__(carName, maxSpeed)

class Ford(Car):
    def __init__(self, carName, maxSpeed):
        super().__init__(carName, maxSpeed)

ford = Ford('Ford', 200)
ford.engine_start()
ford.engine_stop()
ford.acceleration()
ford.stop()
ford.stop()
