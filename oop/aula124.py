class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f'{self.name} it is already filming...')
            return

        print(f'{self.name} is filming...')
        self.filming = True

    def stop_film(self):
        if not self.filming:
            print(f'{self.name} is not filming...')
            return

        print(f'{self.name} is stopping to film...')
        self.filming = False

    def shoot(self):
        if self.filming:
            print(f'{self.name} you can not shoot while you are filming')
            return

        print(f'{self.name} is shooting...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.film()
c1.film()
c1.shoot()
c1.stop_film()
c1.shoot()

print()

c2.stop_film()
c2.film()
c2.film()
c2.shoot()
c2.stop_film()
c2.shoot()