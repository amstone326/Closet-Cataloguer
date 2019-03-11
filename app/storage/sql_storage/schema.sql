DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS outfits;
DROP TABLE IF EXISTS outfits_pivot;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brandname TEXT UNIQUE NOT NULL
);

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_type TEXT NOT NULL,
    short_desc TEXT NOT NULL,
    brand_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_wear TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE outfits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    occasion TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_wear TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (rowid)
);

CREATE TABLE outfits_pivot (
    outfit_id INTEGER NOT NULL,
    article_id INTEGER NOT NULL,
    FOREIGN KEY (outfit_id) REFERENCES outfits (id),
    FOREIGN KEY (article_id) REFERENCES articles (id),
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
