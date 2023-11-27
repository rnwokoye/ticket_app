import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

st.title("New Healthy Diner")


st.header("Breakfast Favorites")

st.text("🥣 Omega 3 & Blueberry Oatmea")
st.text("🥗 Kale, Spinach & Rocket Smoothi")
st.text("🐔 Hard-Boiled Free-Range Eg")
st.text("🥑🍞 Avocado Toa")

st.header("🍌🥭 Build Your Own Fruit Smoothie 🍇")

my_fruit_list = pd.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
).set_index("Fruit")


# Fruit list here
fruits_selected = st.multiselect(
    "Pick some fruits for yourself:",
    list(my_fruit_list.index),
    ["Avocado", "Strawberries"],
)

# fruits to show
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
st.dataframe(fruits_to_show)

# # New section to display fruity vice api response
# st.header("Fruityvice Fruit Advice!")

# # request the data
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

# # normalize the json output
# fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# # Put the data in a DF and let streamlit display it
# st.dataframe(fruityvice_normalized)


# New Function
def get_fruityvice_data(this_fruit_chice):
    fruityvice_response = requests.get(
        "https://fruityvice.com/api/fruit/" + fruit_choice
    )
    user_fruitchoice = pd.json_normalize(fruityvice_response.json())
    return user_fruitchoice


# New Section to display fruitvice API response
st.header("Fruitvice Fruit Advice!")
try:
    fruit_choice = st.text_input("What fruit would you like information about?")
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
        user_choice = get_fruityvice_data(fruit_choice)
        st.dataframe(user_choice)
except URLError as e:
    st.error()


# Move the fruitLoadListQuery and Load into a button
st.header("View Our Fruit List - Add Your Favorites!")

# colnames = [desc[0] for desc in cur.description]


# Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        data = my_cur.fetchall()
        cols = [desc[0] for desc in my_cur.description]
        my_cnx.close()
        return (data, cols)


# Add a button to load the fruit:
if st.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows, my_cols = get_fruit_load_list()
    my_cnx.close()
    all_fruits = pd.DataFrame(my_data_rows, columns=my_cols)
    st.dataframe(all_fruits)


# Now to use our function and button to add fruit name submissions to our table
# Allow User to Add Fruits
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute(f"INSERT INTO fruit_load_list VALUES ('{new_fruit}')")
        my_cnx.close()
        return "Thanks for adding " + new_fruit


add_my_fruit = st.text_input("What fruit would you like to add?")
if st.button("Add a Fruit to the list"):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    fruit_added = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    st.text(fruit_added)
