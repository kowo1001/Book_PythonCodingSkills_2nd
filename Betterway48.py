class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* 실행: {name}의 메타 {meta}.__new__')
        print('기반 클래스들:', bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)
    
class MyClass(metaclass=Meta):
    stuff = 123

    def foo(self):
        pass
    
class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass

class ValidatePolygon(type):
	def __new__(meta, name, bases, class_dict):
        # Polygon 클래스의 하위 클래스만 검증한다
            if bases:
                if class_dict['sides'] < 3:
                    raise ValueError('다각형 변은 3개 이상이어야함')
            return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    sides = None # 하위 클래스는 이 애트리뷰트에 값을 지정해야 한다
    
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180
    
class Triangle(Polygon):
    sides = 3

class Rectangle(Polygon):
    sides = 4

class Nonagon(Polygon):
    sides = 9

assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260


print('class 이전')

class Line(Polygon):
    print('sides 이전')
    sides = 2
    print('sides 이후')

print('class 이후')
