class Chicken:
    def __init__(self, fry, size, quantity, hotpepper, parts):
        self.fry = fry
        self.size = size
        self.quantity = quantity
        self.hotpepper = hotpepper
        self.parts = parts

    def cook(self):
        print(f"準備{self.quantity}個 {self.size}份 {self.fry} 炸雞")

    def add_hot_pepper(self):
        print(f"加辣 辣度為: {self.hotpepper}")

    def get_parts(self):
        print(f"使用部位是 {self.parts}")
        print(f"-----")

# 建立四個 Chicken 物件 分鼻為四個訂單
chicken1 = Chicken("脆皮", "大", 10, 3, "翅膀")
chicken2 = Chicken("韓式", "中", 8, 2, "雞胸")
chicken3 = Chicken("台式", "小", 12, 1, "雞腿")
chicken4 = Chicken("泰式", "中", 6, 4, "雞塊")

# 呼叫三個副函式
chicken1.cook()
chicken1.add_hot_pepper()
chicken1.get_parts()

chicken2.cook()
chicken2.add_hot_pepper()
chicken2.get_parts()

chicken3.cook()
chicken3.add_hot_pepper()
chicken3.get_parts()

chicken4.cook()
chicken4.add_hot_pepper()
chicken4.get_parts()
