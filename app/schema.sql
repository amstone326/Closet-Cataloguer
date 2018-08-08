DROP TABLE IF EXISTS brand;
DROP TABLE IF EXISTS article;

CREATE TABLE brand (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE article (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_type TEXT NOT NULL,
    brand_id INTEGER NOT NULL,
    FOREIGN_KEY (brand_id) REFERENCES brand (id)
);

# Article types:
# - pant
# - blouse
# - tshirt
# - sweater
# - cardigan
# - skirt
# - dress