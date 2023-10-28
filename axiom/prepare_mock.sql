-- CREATE DATABASE city;

-- USE city;

-- CREATE TABLE city(id SERIAL PRIMARY KEY, name VARCHAR(255), country_code VARCHAR(255), population INT);

-- INSERT INTO city (name, country_code, population) 
-- VALUES('Ankara', 'TUR', 8600000), -- Bu Turkiyaning poytaxti va eng katta shahri
-- ('Tashkent', 'UZB', 1978028), -- Bu O'zbekistonning poytaxti va eng katta shahri
-- ('Samarkand', 'UZB', 1000000), -- Bu O'zbekistonning ikkinchi eng katta shahri va tarixiy turizm markazi
-- ('Namangan', 'UZB', 641700), -- Bu O'zbekistonning Farg'ona vodiysidagi eng katta shahri
-- ('Moscow', 'RUS', 12655050), -- Bu Rossiyaning poytaxti va eng katta shahri
-- ('Beijing', 'CHN', 21707000), -- Bu Xitoyning poytaxti va eng katta shahri
-- ('New York', 'USA', 8622698), -- Bu AQShning eng katta shahri va dunyoning iqtisodiy markazi
-- ('London', 'GBR', 8908081), -- Bu Buyuk Britaniyaning poytaxti va eng katta shahri
-- ('Tokyo', 'JPN', 13929286), -- Bu Yaponiyaning poytaxti va eng katta shahri
-- ('Paris', 'FRA', 2148327); -- Bu Frantsiyaning poytaxti va eng katta shahri



-- SELECT * FROM city where population < 1000000;
-- SELECT * FROM city WHERE country_code = 'UZB';



-- SELECT name AS first_column, NULL AS second_column FROM city WHERE population > 1000000
-- UNION ALL
-- SELECT NULL AS first_column, name AS second_column FROM city WHERE population < 1000000;


