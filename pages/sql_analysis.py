import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("📊 SQL Analysis")

conn = get_connection()

selected_query = st.selectbox(
    "Select Query",
    [
        "1. Providers and Receivers by City",
        "2. Provider Type Contributing Most Food",
        "3. Provider Contacts by City",
        "4. Receivers Who Claimed Most Food",
        "5. Total Quantity Available",
        "6. City with Highest Food Listings",
        "7. Most Common Food Types",
        "8. Claims for Each Food Item",
        "9. Provider with Highest Successful Claims",
        "10. Claim Status Percentage",
        "11. Average Quantity Claimed Per Receiver",
        "12. Most Claimed Meal Type",
        "13. Total Quantity Donated by Provider",
        "14. Cities with More Providers than Receivers",
        "15. Cities with Most Unclaimed Food",
        "16. Providers with High Claim Success",
        "17. Food Type with Highest Cancellation Rate"
    ]
)

# Query 1
if selected_query == "1. Providers and Receivers by City":

    query = """
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
    """

    df = pd.read_sql(query, conn)

    st.subheader("Providers and Receivers in Each City")
    st.dataframe(df)


# Query 2
elif selected_query == "2. Provider Type Contributing Most Food":

    query = """
    select type, count(*) as provider_count
from providers_data
group by type
order by provider_count desc
limit 1;
    """

    df = pd.read_sql(query, conn)

    st.subheader("Provider Type Contributing Most Food")
    st.dataframe(df)


# Query 3
elif selected_query == "3. Provider Contacts by City":

    city = st.text_input("Enter City Name")

    if city:

        query = f"""
        select city,
       row_number() over(partition by city) as provider_number_asPer_city,
       contact
from providers_data;
        """

        df = pd.read_sql(query, conn)

        st.dataframe(df)


# Query 4
elif selected_query == "4. Receivers Who Claimed Most Food":

    query = """
    select receiver_id, total_claims 
from (select receiver_id , count(*) as total_claims 
      from claims_data
      group by receiver_id)
where total_claims = (select max(total_claims) from (select receiver_id , count(*) as total_claims 
      from claims_data
      group by receiver_id))
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 5
elif selected_query == "5. Total Quantity Available":

    query = """
    select provider_id, sum(quantity) as total_food_quantity
from food_listing_data
group by provider_id ;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 6
elif selected_query == "6. City with Highest Food Listings":

    query = """
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
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 7
elif selected_query == "7. Most Common Food Types":

    query = """
    select distinct food_type  
from food_listing_data;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 8
elif selected_query == "8. Claims for Each Food Item":

    query = """
    select f.food_name, count(*) as total_claims
from claims_data c
join food_listing_data f
on c.food_id = f.food_id 
group by food_name;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 9
elif selected_query == "9. Provider with Highest Successful Claims":

    query = """
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
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 10
elif selected_query == "10. Claim Status Percentage":

    query = """
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
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 11
elif selected_query == "11. Average Quantity Claimed Per Receiver":

    query = """
    select c.receiver_id , round(avg(f.quantity),1) as avg_quantity_claimed
from claims_data c
join food_listing_data f
on c.food_id = f.food_id
group by c.receiver_id ;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 12
elif selected_query == "12. Most Claimed Meal Type":

    query = """
    select f.meal_type, count(*) as Total_claims
from food_listing_data f
join claims_data c
on f.food_id = c.food_id 
group by f.meal_type
order by total_claims desc
limit 1;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 13
elif selected_query == "13. Total Quantity Donated by Provider":

    query = """
    select f.provider_id,sum(f.quantity) as total_quantity_donated
from providers_data p
join food_listing_data f
on p.provider_id = f.provider_id 
group by f.provider_id;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 14
elif selected_query == "14. Cities with More Providers than Receivers":

    query = """
    select city
from (select coalesce(p.city, r.city)as city,
     count(p.provider_id) as total_providers, 
     count(r.receiver_id) as total_receivers
from providers_data p
full join receivers_data r
on p.city = r.city 
group by p.city, r.city)
where total_receivers > total_providers ;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 15
elif selected_query == "15. Cities with Most Unclaimed Food":

    query = """
    select location as city, count(*) as total_unclaimed_food
from food_listing_data
where food_id not in (select distinct food_id 
	from claims_data)
group by location
having count(*) > 1
order by total_unclaimed_food  desc;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 16
elif selected_query == "16. Providers with High Claim Success":

    query = """
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
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


# Query 17
elif selected_query == "17. Food Type with Highest Cancellation Rate":

    query = """
    select food_type, count(*) as total_cancelled_claims
from (select f.food_type 
from claims_data c
join food_listing_data f
on c.food_id = f.food_id 
where c.status = 'Cancelled')
group by food_type 
order by total_cancelled_claims desc
limit 1;
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)


conn.close()



