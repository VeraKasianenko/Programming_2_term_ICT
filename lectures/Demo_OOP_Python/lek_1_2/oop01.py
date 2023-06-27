
class Person:
    name = "Иван"   # атрибут класса
    
    """        
    методы класса должны принимать в качестве первого параметра ссылку на текущий объект
    Через эту ссылку внутри класса следует обращаться к методам или атрибутам этого же класса
    """
    def display_info(self):
        print("Имя: ", self.name)
        
# получить строковое представление объекта - наследуется от класса object 
    def __str__(self):
        return "Имя: {}".format(self.name)



# создание объектов класса:
"""
Объект создается путем вызова класса по его имени.
После имени класса обязательно ставятся скобки:
      ИмяКласса()
Для создания объекта, связанного с переменной:
      имя_объекта = ИмяКласса([параметры])
Класс вызывается подобно функции, однако при этом происходит не выполнение его тела, а создается объект
"""
print(Person().display_info())  # объект вызвает свой метод

person1 = Person()      # объект связан с именем переменной
person1.display_info()         
 
person2 = Person()
person2.name = "Петр"   # атрибут объекта
person2.display_info()

print(person2)

person2.age = 101   # добавление нового атрибута для объекта
print(person2.age)


# Атрибуты хранятся в специальном словаре
"""  к словарю атрибутов можно обратиться по имени __dict__"""
print('AttrPerson:"', Person.__dict__)
print('AttrOb:', person2.__dict__)

print(hasattr(person2, 'age'))      # проверить наличие атрибута
print(getattr(person2, 'age'))      # получить наличие атрибута
setattr(person2, 'age', 202)        # изменить наличие атрибута
print(person2.age)