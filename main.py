"======================= 1 ==================="
from datetime import date

class CreateMixin:
    def create(self,todo,key):
        if key in self.todos.keys():
            return  "Задача под таким ключём уже существует"
        self.todos[key] = todo

class DeleteMixin:
    def delete(self,key):
        p = self.todos.pop(key)
        return f'удалили {p} задачу'  

class UpdateMixin:
    def update(self,key,new_value):
        self.todos[key] = new_value
    
class ReadMixin:
    def read(self):
        list_ = sorted(self.todos)
        return list_

class ToDo(CreateMixin,DeleteMixin,UpdateMixin,ReadMixin):
    def __init__(self,todos):
        self.todos = todos

    def set_deadline(self,data):
        today = str(date.today())
        y = int(data[6:]) - int(today[:4])
        m = int(data[3:5]) - int(today[5:7])
        d = int(data[:2]) - int(today[8:])
        result = y*365 + m * 30 + d
        return result
 
todo = ToDo({})
print(todo.set_deadline('15/12/2023'))
todo.create('dsfa',6)
print(todo.read())
"======================= 2 ====================="
class Person:
    __name = None
    __last_name = None
    __age = None
    __email = None

    @property  
    def name(self):
        return self.__name

    @property  
    def last_name(self):
        return self.__last_name

    @property  
    def age(self):
        return self.__age

    @property  
    def email(self):
        return self.__email

    @name.setter 
    def name(self,n):
        self.__name = n
    
    @last_name.setter 
    def last_name(self,n):
        self.__last_name = n
    
    @age.setter 
    def age(self,n):
        self.__age = n
    
    @email.setter 
    def email(self,n):
        self.__email = n
    
john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com
    

"===================== 3 ======================="
class Dog:
    def voice(self):
        print('Гав')

class Cat:
    def voice(self):
        print('Мяу')

def to_pet(obj):
    obj.voice()
barsik = Cat()
rex = Dog()
to_pet(barsik)
to_pet(rex)
