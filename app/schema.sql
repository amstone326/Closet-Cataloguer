DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS outfits;
DROP TABLE IF EXISTS outfit_items;

CREATE TABLE brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_type TEXT NOT NULL,
    brand_id INTEGER NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brands (id)
);

CREATE TABLE outfits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occasion TEXT NOT NULL
);

CREATE TABLE outfit_items (
    outfit_id INTEGER NOT NULL,
    article_id INTEGER NOT NULL,
    PRIMARY KEY (outfit_id, article_id)
);


/*
Article types:
- pant
- blouse
- tshirt
- sweater
- cardigan
- skirt
- dress

Occasion types:
- casual day
- nice day
- casual evening
- fancy evening
*/
