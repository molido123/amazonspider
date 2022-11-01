
class Review:
    name = ""
    star = ""
    content = ""

    def toString(self):
        return self.name + "\n" + self.star + "\n" + self.content + "\n"

    def __init__(self, name, star, content):
        self.name = name
        self.star = star
        self.content = content


class Entity:
    comments = []
    price = []
    name = ""

    def __init__(self, comments, price, name):
        self.comments = comments
        self.price = price
        self.name = name
