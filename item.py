# Item sınıfı: Oyunda kullanılacak eşyaları temsilen bir temel sınıf oluşturalım
class Item:
    def __init__(self, name, weight):
        self.name = name  # Eşyanın adı
        self.weight = weight  # Eşyanın ağırlığı

    def use(self):
        pass  # Eşyanın kullanılmasını simgeler
