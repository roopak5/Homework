use sakila;

-- 1a. Display the first and last names of all actors from the table actor.
select first_name, last_name from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select concat(first_name, ' ',  last_name) as 'Actor Name' from actor; -- its already in upper case

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
select first_name, last_name, actor_id from actor
where first_name = "Joe";

-- 2b. Find all actors whose last name contain the letters GEN:
select * from actor where last_name like "%GEN%";

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select last_name, first_name from actor where last_name like "%li%";

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
-- so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, 
-- as the difference between it and VARCHAR are significant).
ALTER TABLE actor
ADD COLUMN  description BLOB;

-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor drop description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name, count(last_name) as 'Last Names of Actors' from actor
group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name, count(last_name) as 'Last Names of Actors' from actor
group by last_name HAVING count(last_name) >=2;

-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
update actor set first_name = 'HARPO'
where first_name = 'GROUCHO' and last_name  = 'WILLIAMS';
-- select * from actor
-- where first_name = 'HARPO';

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
update actor set first_name = 'GROUCHO'
where actor_id = 172;

select * from actor
where first_name = 'GROUCHO';

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
-- Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html
show create table address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select first_name, last_name
from staff as s
join address as a 
on (s.address_id = a.address_id);

select staff.first_name, staff.last_name, address.address
from staff
join address on staff.address_id = address.address_id;


-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select staff.first_name, staff.last_name, concat('$', cast(sum(payment.amount) as char)) as 'Total Amount' from staff 
join payment on staff.staff_id = payment.staff_id where payment.payment_date like "%2005-08%"
group by staff.staff_id;

select * from payment;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select film.title as 'Film Name', count(film_actor.actor_id) as 'Number of Actors'
from film_actor
join film on film_actor.film_id = film.film_id
group by film_actor.film_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select * from inventory 
where film_id in
(
select count(title) 
from film
where title = "Hunchback Impossible"
);

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer.
--  List the customers alphabetically by last name:
SELECT c.first_name, c.last_name, sum(p.amount) AS `Total Paid`
FROM customer c
JOIN payment p 
ON c.customer_id= p.customer_id
GROUP BY c.last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select title as 'Movies with K and Q' from film where title like 'k%' or title like 'q%'
and title in (
select title from film where language_id = 1
);

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
-- select title from film where title = 'alone trip';
select concat(first_name,' ', last_name) as 'Film -Alone Trip -Actors' from actor where actor_id in 
(select actor_id from film_actor where film_id in
(select film_id from film where title = 'alone trip'
));

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers.
--  Use joins to retrieve this information.

select c.first_name, c.last_name, c.email from customer c join address a on (c.address_id = a.address_id)
join city on (city.city_id = a.city_id)
join country on (country.country_id = city.country_id)
where country.country ='Canada';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as family films.
select * from category;
select title, description 
from film 
join film_category on (film_category.film_id = film.film_id)
join category on (category.category_id = film.film_id)
where category.name = 'family';

SELECT title, description FROM film 
WHERE film_id IN
(
SELECT film_id FROM film_category
WHERE category_id IN
(
SELECT category_id FROM category
WHERE name = "Family"
));


-- 7e. Display the most frequently rented movies in descending order.
select film.title, count(rental_id) as 'Times Rented' from rental
join rental on (rental.inventory_id = inventory.inventory_id)
join film on(inventory.film_id = film.film_id)
group by film.title
order by 'Times Rented' DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id as Stores, CONCAT('$ ', CAST(sum(amount) AS CHAR)) AS Revenue
FROM payment p
JOIN rental r
ON (p.rental_id = r.rental_id)
JOIN inventory i
ON (i.inventory_id = r.inventory_id)
JOIN store s
ON (s.store_id = i.store_id)
GROUP BY s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
select store.store_id, city.city, country.country
from store join address on (address.address_id = store.address_id)
join city on (city.city_id = address.city_id)
join country on (country.country_id = city.country_id);

select * from store; select * from address; select * from city; select * from country;

-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category,
-- inventory, payment, and rental.)
SELECT c.name AS Genre, SUM(p.amount) AS Gross 
FROM category c
JOIN film_category fc 
ON (c.category_id=fc.category_id)
JOIN inventory i 
ON (fc.film_id=i.film_id)
JOIN rental r 
ON (i.inventory_id=r.inventory_id)
JOIN payment p 
ON (r.rental_id=p.rental_id)
GROUP BY c.name ORDER BY Gross  LIMIT 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution
-- from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
create view genre_revenue as 
select c.name as Genre, sum(p.amount) as Gross
from category c join film_category fc on (c.category_id = fc.category_id)
join inventory i on (fc.film_id = i.film_id)
join rental r on (i.inventory_id = r.inventory_id)
join payment p on (r.rental_id = p.rental_id)
group by c.name order by Gross limit 5;


-- 8b. How would you display the view that you created in 8a?
select * from genre_revenue;
-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view genre_revenue;



