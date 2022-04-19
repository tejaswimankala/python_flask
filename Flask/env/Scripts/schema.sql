DROP TABLE IF EXISTS Users ;
DROP TABLE IF EXISTS store_groceries  ;

CREATE TABLE Users (
    

    name  TEXT NOT NULL,
    email TEXT NOT NULL
    
);

CREATE TABLE store_groceries(

    store_name TEXT NOT NULL,
    grocery_item  TEXT NOT NULL,
    price  INTEGER NOT NULL
    
)
    



