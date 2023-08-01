class Pen:
    def __init__(self, color):
        # private protected
        self.color = color
        self._cover_color = None

    @property
    def color(self):
        print('I AM IN THE GETTER')
        return self._color

    @color.setter
    def color(self, value):
        print('I AM IN THE SETTER')
        self._color = value

    @property
    def cover_color(self):
        return self._cover_color

    @cover_color.setter
    def cover_color(self, value):
        self._cover_color = value


pen = Pen('Blue')
pen.color = 'Pink'
pen.cover_color = 'Blue'
print(pen.color)
print(pen.cover_color)