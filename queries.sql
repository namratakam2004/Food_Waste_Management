--1. How many food providers and receivers are there in each city?
select coalesce(p.city,r.city) as city ,
       p.providers_count ,
       r.receivers_count  
from (select city, count(*) as providers_count
       from providers_data
       group by city) p
full outer join (select city, count(*) as receivers_count
        from receivers_data
        group by city) r
on p.city = r.city;

--2.Which type of food provider (restaurant, grocery store, etc.) contributes the most food?
select type, count(*) as provider_count
from providers_data
group by type
order by provider_count desc
limit 1;

--3.What is the contact information of food providers in a specific city?
select city,
       row_number() over(partition by city) as provider_number_asPer_city,
       contact
from providers_data;

--4.Which receivers have claimed the most food?
select receiver_id, total_claims 
from (select receiver_id , count(*) as total_claims 
      from claims_data
      group by receiver_id)
where total_claims = (select max(total_claims) from (select receiver_id , count(*) as total_claims 
      from claims_data
      group by receiver_id))
      
--5. What is the total quantity of food available from all providers?
select provider_id, sum(quantity) as total_food_quantity
from food_listing_data
group by provider_id ;

--6.Which city has the highest number of food listings?
select city, row_number() over(partition by food_listing_count) as rank
from (select p.city, count(f.provider_id ) food_listing_count
       from food_listing_data f
       left join providers_data p
       on f.provider_id = p.provider_id
       group by p.city
       order by food_listing_count desc)
where food_listing_count = (select max(food_listing_count) from(select p.city, count(f.provider_id ) food_listing_count
       from food_listing_data f
       left join providers_data p
       on f.provider_id = p.provider_id
       group by p.city
       order by food_listing_count desc));

--7.What are the most commonly available food types?
select distinct food_type  
from food_listing_data;

--8. How many food claims have been made for each food item?
select f.food_name, count(*) as total_claims
from claims_data c
join food_listing_data f
on c.food_id = f.food_id 
group by food_name;

--9. Which provider has had the highest number of successful food claims?
select f.provider_id , count(*) as total_claims
from providers_data p
join food_listing_data f
on p.provider_id = f.provider_id 
join claims_data c
on f.food_id = c.food_id 
where c.status = 'Completed'
group by f.provider_id
order by total_claims desc
limit 1;

--10. What percentage of food claims are completed vs. pending vs. canceled?
select 'Complete' as food_claim_status,((total_claims*100)/1000) as status_percentage
from (select status, count(*) as total_claims
	from claims_data
group by status)
where status = 'Completed'
UNION
select 'Cancelled', ((total_claims*100)/1000) 
from (select status, count(*) as total_claims
	from claims_data
group by status)
where status = 'Cancelled' 
UNION
select 'Pending', ((total_claims*100)/1000) 
from (select status, count(*) as total_claims
	from claims_data
group by status)
where status = 'Pending' ;

--11. What is the average quantity of food claimed per receiver?
select c.receiver_id , round(avg(f.quantity),1) as avg_quantity_claimed
from claims_data c
join food_listing_data f
on c.food_id = f.food_id
group by c.receiver_id ;

--12. Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?
select f.meal_type, count(*) as Total_claims
from food_listing_data f
join claims_data c
on f.food_id = c.food_id 
group by f.meal_type
order by total_claims desc
limit 1;

--13.What is the total quantity of food donated by each provider?
select f.provider_id,sum(f.quantity) as total_quantity_donated
from providers_data p
join food_listing_data f
on p.provider_id = f.provider_id 
group by f.provider_id;

--14. Cities with more receivers than providers
select city
from (select coalesce(p.city, r.city)as city,
     count(p.provider_id) as total_providers, 
     count(r.receiver_id) as total_receivers
from providers_data p
full join receivers_data r
on p.city = r.city 
group by p.city, r.city)
where total_receivers > total_providers ;

--15. Cities with most unclaimed food
select location as city, count(*) as total_unclaimed_food
from food_listing_data
where food_id not in (select distinct food_id 
	from claims_data)
group by location
having count(*) > 1
order by total_unclaimed_food  desc;

--16. Providers with high claim success 
select provider_id , name 
from providers_data 
where provider_id in(select provider_id 
	from (select f.provider_id, count(*) as total_Successed_claims  
		from food_listing_data f
		join claims_data c
		on f.food_id = c.food_id 
		where c.status = 'Completed'
		group by f.provider_id 
		having count(*) > 1
		order by total_successed_claims desc));

--17. Food type with highest cancellation claim status
select food_type, count(*) as total_cancelled_claims
from (select f.food_type 
from claims_data c
join food_listing_data f
on c.food_id = f.food_id 
where c.status = 'Cancelled')
group by food_type 
order by total_cancelled_claims desc
limit 1;


