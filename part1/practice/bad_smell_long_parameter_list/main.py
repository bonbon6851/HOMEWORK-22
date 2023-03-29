# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, speed, state, field, x_coord, y_coord):
        self.speed = speed
        self.state = state
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, direction):

        speed = self.get_speed()

        if direction == 'UP':
            self.set_unit(self.x_coord, self.y_coord + speed)
        elif direction == 'DOWN':
            self.set_unit(self.x_coord, self.y_coord - speed)
        elif direction == 'LEFT':
            self.set_unit(self.x_coord - speed, self.y_coord)
        elif direction == 'RIGHT':
            self.set_unit(self.x_coord + speed, self.y_coord)

    def get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')

    def set_unit(self, x, y):
        pass
