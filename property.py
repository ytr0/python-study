import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        print(self._x) #この書き方は便利
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @property
    def distance(self):
        return math.sqrt(self._x * self._x + self._y * self._y)

    
point = Point(10, 20)
print(point.distance) 
#関数として定義されているが、@propertyデコレータがついていると変数のようにアクセスできる。

point.x = 30
point.x

point.y = 30 #setterを定義しないとアクセスできない。

"""
プロパティの利点は get_x() のような関数を定義しなくても、まるで変数を直接参照しているようなコードが書ける点にあります。
これはクラスを利用する人からするとシンプルなコードが書けるので便利です。
"""