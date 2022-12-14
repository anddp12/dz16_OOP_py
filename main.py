# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. 
# У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. 

celcii = 10
farengeit = 50

class Temperature:
    @staticmethod
    def Celcii(Farengeit):
        return ((farengeit - 32) * 5) / 9

    @staticmethod
    def Farengeit(Celcii):
        return (celcii * 1.8) + 32

temp = Temperature()
t1 = temp.Celcii(50)
t2 = temp.Farengeit(10)

print(t1)
print(t2)