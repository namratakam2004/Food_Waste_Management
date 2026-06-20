import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("🔧 CRUD Operations")

conn = get_connection()
cursor = conn.cursor()

st.header("Providers")
operation = st.selectbox(
    "Select Operation",
    [
        "Add Provider",
        "Update Provider",
        "Delete Provider",
        "View Providers"
    ]
)

# -------------------------------
# ADD PROVIDER
# -------------------------------

if operation == "Add Provider":

    st.subheader("Add New Provider")

    name = st.text_input("Provider Name")
    provider_type = st.text_input("Provider Type")
    address = st.text_input("Address")
    city = st.text_input("City")
    contact = st.text_input("Contact")

    if st.button("Add Provider"):

        cursor.execute(
            """
            INSERT INTO providers_data
            (name, type, address, city, contact)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (name, provider_type, address, city, contact)
        )

        conn.commit()

        st.success("Provider Added Successfully")


# -------------------------------
# UPDATE PROVIDER
# -------------------------------

elif operation == "Update Provider":

    st.subheader("Update Provider")

    provider_id = st.number_input(
        "Provider ID",
        min_value=1,
        step=1
    )

    new_city = st.text_input("New City")
    new_contact = st.text_input("New Contact")

    if st.button("Update Provider"):

        cursor.execute(
            """
            UPDATE providers_data
            SET city=%s,
                contact=%s
            WHERE provider_id=%s
            """,
            (
                new_city,
                new_contact,
                provider_id
            )
        )

        conn.commit()

        st.success("Provider Updated Successfully")


# -------------------------------
# DELETE PROVIDER
# -------------------------------

elif operation == "Delete Provider":

    st.subheader("Delete Provider")

    provider_id = st.number_input(
        "Provider ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Provider"):

        cursor.execute(
            """
            DELETE FROM providers_data
            WHERE provider_id=%s
            """,
            (provider_id,)
        )

        conn.commit()

        st.success("Provider Deleted Successfully")


# -------------------------------
# VIEW PROVIDERS
# -------------------------------

elif operation == "View Providers":

    st.subheader("Providers Data")

    query = """
    SELECT *
    FROM providers_data
    ORDER BY provider_id
    """

    df = pd.read_sql(query, conn)

    st.dataframe(
        df,
        use_container_width=True
    )
#-----------------------------------------------------------------------------------
st.header("Receivers")
operation = st.selectbox(
    "Select Operation",
    [
        "Add Receiver",
        "Update Receiver",
        "Delete Receiver",
        "View Receiver"
    ]
)

# -------------------------------
# ADD RECEIVERS
# -------------------------------

if operation == "Add Receiver":

    st.subheader("Add New Receiver")

    name = st.text_input("Receiver Name")
    type = st.text_input("Receiver Type")
    city = st.text_input("Receiver City")
    contact = st.text_input("Receiver Contact")

    if st.button("Add Receiver"):

        cursor.execute(
            """
            INSERT INTO receivers_data
            (name, type, city, contact)
            VALUES (%s,%s,%s,%s)
            """,
            (name, type, city, contact)
        )

        conn.commit()

        st.success("Receiver Added Successfully")


# -------------------------------
# UPDATE RECEIVERS
# -------------------------------

elif operation == "Update Receiver":

    st.subheader("Update Receiver")

    receiver_id = st.number_input(
        "Receiver ID",
        min_value=1,
        step=1
    )

    new_city = st.text_input("New City")
    new_contact = st.text_input("New Contact")

    if st.button("Update Receiver"):

        cursor.execute(
            """
            UPDATE receivers_data
            SET city=%s,
                contact=%s
            WHERE receiver_id=%s
            """,
            (
                new_city,
                new_contact,
                receiver_id
            )
        )

        conn.commit()

        st.success("Receiver Updated Successfully")


# -------------------------------
# DELETE RECEIVERS
# -------------------------------

elif operation == "Delete Receiver":

    st.subheader("Delete Receiver")

    provider_id = st.number_input(
        "Receiver ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Receiver"):

        cursor.execute(
            """
            DELETE FROM receivers_data
            WHERE receiver_id=%s
            """,
            (receiver_id,)
        )

        conn.commit()

        st.success("Receiver Deleted Successfully")


# -------------------------------
# VIEW RECEIVERS
# -------------------------------

elif operation == "View Receiver":

    st.subheader("Receiver Data")

    query = """
    SELECT *
    FROM receivers_data
    ORDER BY receiver_id
    """

    df = pd.read_sql(query, conn)

    st.dataframe(
        df,
        use_container_width=True
    )
	
#----------------------------------------------------------------------------------------------
st.header("Food Listing")
operation = st.selectbox(
    "Select Operation",
    [
        "Add Food Listing",
        "Update Food Listing",
        "Delete Food Listing",
        "View Food listing"
    ]
)

# -------------------------------
# ADD FOOD
# -------------------------------

if operation == "Add Food Listing":

    st.subheader("Add Food Listing")

    food_name = st.text_input("Food Name")
    quantity = st.number_input("Quantity", min_value=1)
    expiry_date = st.date_input("Expiry Date")
    provider_id = st.number_input("Provider_ID", min_value=1)
    provider_type = st.text_input("Provider_Type")
    location = st.text_input("Location")
    food_type = st.text_input("Food Type")
    meal_type = st.text_input("Meal Type")

    if st.button("Add Food"):

        cursor.execute(
            """
            INSERT INTO food_listing_data
            (
                food_name,
                quantity,
                expiry_date,
                provider_id,
                provider_type,
                location,
                food_type,
                meal_type
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                food_name,
                quantity,
                expiry_date,
                provider_id,
                provider_type,
                location,
                food_type,
                meal_type
            )
        )

        conn.commit()

        st.success("Food Listing Added Successfully")

# -------------------------------
# UPDATE FOOD
# -------------------------------

elif operation == "Update Food Listing":

    st.subheader("Update Food Listing")

    food_id = st.number_input(
        "Food ID",
        min_value=1,
        step=1
    )

    new_quantity = st.number_input(
        "New Quantity",
        min_value=1
    )

    new_expiry_date = st.date_input(
        "New Expiry Date"
    )

    if st.button("Update Food"):

        cursor.execute(
            """
            UPDATE food_listing_data
            SET quantity=%s,
                expiry_date=%s
            WHERE food_id=%s
            """,
            (
                new_quantity,
                new_expiry_date,
                food_id
            )
        )

        conn.commit()

        st.success("Food Listing Updated Successfully")


# -------------------------------
# DELETE FOOD 
# -------------------------------

elif operation == "Delete Food Listing":

    st.subheader("Delete Food Listing")

    food_id = st.number_input(
        "Food ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Food"):

        cursor.execute(
            """
            DELETE FROM food_listing_data
            WHERE food_id=%s
            """,
            (food_id,)
        )

        conn.commit()

        st.success("Food Listing Deleted Successfully")


# -------------------------------
# VIEW FOOD
# -------------------------------

elif operation == "View Food Listings":

    st.subheader("Food Listings")

    query = """
    SELECT *
    FROM food_listing_data
    ORDER BY food_id
    """

    df = pd.read_sql(query, conn)

    st.dataframe(
        df,
        use_container_width=True
    )
	


conn.close()