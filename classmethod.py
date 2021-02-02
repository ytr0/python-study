#インスタンス化しなくてもクラスから直接呼び出せる
#クラスをインポートすれば、外部から、インスタンス化しなくても使える。
#classmethodの第一引数ではクラスが取得できる

class Item:
    info = "info"
    def __init__(self, id, name):
        self.id = id
        self._name = name

    @classmethod
    def retrieve_from_api(cls, id):
        #res = requests.get(f"https://api.example.com/items/{id}")
        #data = res.json()
        print(cls.info)
        name = "Yamada"
        return cls(id, name) #data["name"]
    
    @property
    def name(self):
        print(self._name)
        return self._name

#https://qiita.com/msrks/items/fdc9afd12effc2cba1bc
#継承クラスで動作が変わるべきとき

i = Item.retrieve_from_api(20)
i.name


class Item2:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def retrieve_item(id):
    res = requests.get(f"https://api.example.com/items/{id}")
    data = res.json()
    return Item(id, data["name"])