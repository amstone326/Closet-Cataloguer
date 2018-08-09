DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS outfits;
DROP TABLE IF EXISTS outfit_items;

CREATE TABLE users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE brands (
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE articles (
    article_type TEXT NOT NULL,
    brand_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES brands (rowid),
    FOREIGN KEY (user_id) REFERENCES users (rowid)
);

CREATE TABLE outfits (
    occasion TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (rowid)
);

CREATE TABLE outfit_items (
    outfit_id INTEGER NOT NULL,
    article_id INTEGER NOT NULL,
    FOREIGN KEY (outfit_id) REFERENCES outfits (rowid),
    FOREIGN KEY (article_id) REFERENCES articles (rowid),
    PRIMARY KEY (outfit_id, article_id)
);


/*
The brands table is shared amongst all users

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
