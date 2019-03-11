from enum import Enum


class ArticleType(Enum):
    pants = "pants"
    jeans = "jeans"
    leggings = "leggings"
    skirt = "skirt"
    dress = "dress"
    blouse = "blouse"
    tshirt = "tshirt"
    sweater = "sweater"
    cardigan = "cardigan"
    jacket = "jacket"


class OccassionType(Enum):
    daytime = "daytime"
    evening = "evening"
    casual = "casual"
    fancy = "fancy"


