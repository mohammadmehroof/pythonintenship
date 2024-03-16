# class animal:
#     def __init__(self,name):
#         self.name=name
# class dog(animal):
#     def make_sound(self):
#         return "woof"
# d1=dog("jack")
# print(d1.name)
# print(d1.make_sound())

class brands:
    brand_name_1 = "amazon"
    brand_name_2 = "OLX"

class products:
    prod_1 = "online ecommerce store"
    prod_2 = "online store"

class popularity(brands,products):
    prod_1_popularity = 100
    prod_2_popularity = 70

obj_1 =popularity()
print(obj_1.brand_name_1+ " is an " +obj_1.prod_1)
print(obj_1.brand_name_2+ " is an " +obj_1.prod_2)
