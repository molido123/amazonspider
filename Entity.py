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
    name: str
    img: str
    price: str
    brief: str
    description: str
    country: str
    product_information: dict
    IDE: str
    ratings: str

    def __init__(self, name: str, img: str, price: str, brief: str, description: str, country: str,
                 product_information: dict, IDE: str, ratings: str):
        self.img = img
        self.price = price
        self.name = name
        self.brief = brief
        self.description = description
        self.country = country
        self.product_information = product_information
        self.IDE = IDE
        self.ratings = ratings

    def toString(self) -> str:
        a = "----------" + self.name + '--------------' + '\n'
        b = "name: " + str(self.name) + '\n'
        c = "img(gallery): " + str(self.img) + '\n'
        d = "price: " + str(self.price) + '\n'
        e = "brief: \n" + str(self.brief) + '\n'
        f = "description: " + str(self.description) + '\n'
        g = "country: " + str(self.country) + '\n'
        h = "ID of product: " + str(self.IDE) + '\n'
        i = "ratings: " + str(self.ratings) + '\n'
        j = "details: " + '\n' + str(self.product_information) + '\n'
        res = a + b + c + d + e + f + g + h + i + j
        res = res + "----------------------------------------------" + '\n'
        return res
