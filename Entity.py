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
        b = "\nname: " + str(self.name) + '\n'
        c = "\nimg(gallery): " + str(self.img) + '\n'
        d = "\nprice: " + str(self.price) + '\n'
        e = "\nbrief: \n" + str(self.brief) + '\n'
        f = "\ndescription: \n" + str(self.description) + '\n'
        g = "\ncountry: " + str(self.country) + '\n'
        h = "\nID of product: " + str(self.IDE) + '\n'
        i = "\nratings: " + str(self.ratings) + '\n'
        j = "\ndetails: \n"
        dic = ""
        for key in self.product_information:
            tmp = "      " + str(key) + "  " + str(self.product_information[key])
            dic = dic + '\n' + tmp
        j = j + dic
        res = a + b + c + d + e + f + g + h + i + j
        res = res + "\n--------------------------------------------------------------------------------------------------" + '\n\n\n\n'
        return res

    def getCountry(self) -> str:
        return str(self.country)
