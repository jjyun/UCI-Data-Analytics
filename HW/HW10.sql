#1A
SELECT first_name, last_name FROM actor;
#1B
SELECT CONCAT(first_name, ', ', last_name) AS Actor_Name FROM actor;
#2A
SHOW FIELDS IN actor;
SELECT actor_id, first_name, last_name FROM actor WHERE first_name="Joe";
#2B
SELECT first_name, last_name FROM actor WHERE last_name LIKE "%gen%";
#2C
SELECT last_name, first_name FROM actor WHERE last_name LIKE "%LI%" ORDER BY last_name asc, first_name asc;
#2D
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');
#3A
ALTER TABLE actor ADD COLUMN description BLOB AFTER last_update;
#3B
ALTER TABLE actor DROP Description;
#4A
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name;
#4B
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name HAVING count(*) > 2;
#4C
UPDATE actor SET first_name='Harpo' WHERE first_name='GROUCHO' AND last_name='WILLIAMS';
SELECT * FROM actor WHERE first_name='GROUCHO' OR first_name='HARPO';
#4D
UPDATE actor SET first_name='GROUCHO' WHERE first_name='Harpo' AND last_name='Williams';
SELECT * FROM actor WHERE first_name='GROUCHO';
#5a
DESCRIBE Sakila.address;
#6A
SELECT first_name, last_name, address FROM staff JOIN address ON staff.address_id = address.address_id;
#6B
SELECT first_name, last_name, SUM(payment.amount) FROM staff JOIN payment ON staff.staff_id = payment.staff_id GROUP BY first_name;
#6C
SELECT title, COUNT(actor_id) FROM film JOIN film_actor ON film.film_id = film_actor.film_id GROUP BY title;
#6D
SELECT title, COUNT(title) FROM film JOIN inventory on film.film_id = inventory.film_id WHERE film.title='Hunchback Impossible';
#6E
SELECT last_name, first_name, SUM(payment.amount) FROM customer JOIN payment ON customer.customer_id = payment.customer_id GROUP BY first_name, last_name ORDER BY last_name;
#7A
SELECT title FROM film WHERE title LIKE 'K%' OR title LIKE 'Q%' AND language_id=(SELECT language_id FROM language WHERE name='English');
#7B
SELECT first_name, last_name FROM actor WHERE actor_id 	IN (SELECT actor_id FROM film_actor WHERE film_id IN (SELECT film_id FROM film WHERE title='ALONE TRIP'));
#7C
SELECT first_name, last_name, email FROM customer JOIN address ON customer.address_id = address.address_id JOIN city ON address.city_id=city.city_id JOIN country ON city.country_id=country.country_id;
#7D
SELECT title FROM film JOIN film_category ON film.film_id=film_category.film_id JOIN category ON film_category.category_id=category.category_id;
#7E
SELECT title, COUNT(film.film_id) FROM film JOIN inventory ON film.film_id=inventory.film_id JOIN rental ON inventory.inventory_id=rental.inventory_id GROUP BY title ORDER BY COUNT(film.film_id); 
#7F
SELECT store_id, SUM(payment.amount) FROM payment JOIN staff ON payment.staff_id=staff.staff_id GROUP BY store_id;
#7G
SELECT store_id, city, country FROM store JOIN address ON store.address_id=address.address_id JOIN city ON store.address_id=address.address_id JOIN country ON city.country_id=country.country_id;
#7H
SELECT name, SUM(payment.amount) FROM category JOIN film_category ON category.category_id=film_category.category_id JOIN inventory ON film_category.film_id=inventory.film_id JOIN rental ON inventory.inventory_id=rental.inventory_id JOIN payment ON rental.rental_id=payment.rental_id GROUP BY category.name ORDER BY SUM(payment.amount) LIMIT 5;
#8A
SELECT name AS "top_five_genres", SUM(payment.amount) FROM category JOIN film_category ON category.category_id=film_category.category_id JOIN inventory ON film_category.film_id=inventory.film_id JOIN rental ON inventory.inventory_id=rental.inventory_id JOIN payment ON rental.rental_id=payment.rental_id GROUP BY category.name ORDER BY SUM(payment.amount) LIMIT 5;
SELECT * FROM top_five_genres;
#8B
SELECT * FROM top_five_genres;
#8C
DROP VIEW top_five_genres;