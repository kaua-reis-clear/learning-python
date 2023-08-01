class Pen:
    def __init__(self, cor):
        self.tint_color = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.tint_color

    @property
    def cover_color(self):
        return 123456

###########################


pen = Pen('Blue')
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cor)
print(pen.cover_color)

#####################################

# class Pen:
#     def __init__(self, cor):
#         self.tint_color = cor

#     def get_color(self):
#         print('GET COLOR')
#         return self.tint_color

# ###########################


# pen = Pen('Blue')
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())