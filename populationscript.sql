INSERT INTO menu_menu (name, price,image) VALUES('Pepperoni Pizza', 1500, 'https://www.pngkit.com/png/detail/52-520229_pepperoni-pizza-png-pizza-pepperoni.png');
INSERT INTO menu_menu (name, price,image) VALUES('Margarita Pizza', 1300, 'https://www.pngmart.com/files/1/Cheese-Pizza-PNG-Clipart.png');
INSERT INTO menu_menu (name, price,image) VALUES('Hawaii Pizza', 1700, 'https://w7.pngwing.com/pngs/2/723/png-transparent-california-style-pizza-sicilian-pizza-hawaiian-pizza-neapolitan-pizza-pizza-food-recipe-cheese.png');
INSERT INTO menu_menu (name, price,image) VALUES('Ham Pizza', 1500, 'https://w7.pngwing.com/pngs/82/51/png-transparent-california-style-pizza-sicilian-pizza-ham-tomato-sauce-pizza-food-cheese-recipe.png');


INSERT INTO menu_Menudetails (description, menuid_id) VALUES('Pizza with sauce, cheese and pepperoni', 1);
INSERT INTO menu_Menudetails (description, menuid_id) VALUES('Pizza with sauce and cheese', 2);
INSERT INTO menu_Menudetails (description, menuid_id) VALUES('Pizza with sauce, cheese, ham and pinapple', 3);
INSERT INTO menu_Menudetails (description, menuid_id) VALUES('Pizza with sauce, cheese and ham', 4);


INSERT INTO offers_offers (description,price) VALUES('2 for 1 offer: pick two pizzas for the price of one', 1500);
INSERT INTO offers_offers (description,price) VALUES('Lunch offer: pick one pizza of the menu for just 1000 kr', 1000);
INSERT INTO offers_offers (description,price) VALUES('Family offer: pick 4 pizzas of the menu for a discount price', 4800);


INSERT INTO personal_profile_user (name,  phone_number ,home_address, user_name, password) VALUES('Gunnar Hjartarson', 8688574, 'Vesturhop 21', 'Gunnar_16', 'Gunnar.1234');
INSERT INTO personal_profile_user (name,  phone_number ,home_address, user_name, password) VALUES('Lína Lára', 5768490, 'Ránargata 13', 'Lina_lara15', 'lara.best');


INSERT INTO personal_profile_ProfileImages (user_name_id, image) VALUES(1, 'https://freepngimg.com/thumb/man/22654-6-man-thumb.png');
INSERT INTO personal_profile_ProfileImages (user_name_id, image) VALUES(2, 'https://freepngimg.com/download/girl/147844-professional-woman-business-free-hd-image.png');

