import streamlit as st
import pandas as pd
import numpy as np
import hmac
from datetime import timedelta

# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
# from random import randint
# from config.app_db_con import create_connection


# # from admin_page import get_tickets
# import admin_page

# # import offense categories
# import json

# # import psycopg2
# from psycopg2.extensions import register_adapter, AsIs

# register_adapter(np.int64, AsIs)


# # App Title
# st.header("Traffice Enforcement System")


# def is_admin(username):
#     with open("groups_list.json", "r") as admins:
#         admins_group = json.load(admins)
#         return True if username in admins_group.get("admins") else False


# def my_authentication():
#     with open("app_login.yaml") as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     authenticator = stauth.Authenticate(
#         config["credentials"],
#         config["cookie"]["name"],
#         config["cookie"]["key"],
#         config["cookie"]["expiry_days"],
#         config["preauthorized"],
#     )

#     authenticator.login("Login", "main")

#     # If Authenticated:
#     if st.session_state["authentication_status"]:
#         st.success(f'Welcome: *{st.session_state["name"]}*')
#         if authenticator.logout("Logout", "main", key="unique_key"):
#             on_logout()

#         return st.session_state.get("name")

#     elif st.session_state["authentication_status"] is False:
#         st.error("Username/password is incorrect")
#         st.stop()
#     elif st.session_state["authentication_status"] is None:
#         st.warning("Please enter your username and password")
#         st.stop()


# # Define Logout Actions:
# def on_logout():
#     for key in st.session_state.keys():
#         del st.session_state[key]
#         st.stop()


# def get_offense_category() -> dict:
#     with open("offense_dictionary.json", "r") as f:
#         offense_dictionary = json.load(f)
#         return offense_dictionary


# def select_offence(offence_dict: dict) -> tuple:
#     # Use a select box for the offense
#     selected_offense = st.selectbox(
#         "Choose an offense to begin:",
#         options=list(offence_dict.keys()),
#         index=0,
#         placeholder="Choose option",
#         key="selected_offense",
#     )
#     fine = offence_dict.get(f"{selected_offense}")
#     if fine != "":
#         st.write(f"${fine}")
#     return (selected_offense, fine)


# # Enter Form Details
# def create_offense() -> pd.DataFrame:
#     # Get the offence info
#     offense, fine = select_offence(get_offense_category())

#     # Input Offender Forms
#     with st.form(key="offense_form", clear_on_submit=True):
#         col1, col2 = st.columns(2)

#         # Use a select box for the offense
#         with col1:
#             first_name = st.text_input("First Name")
#             offense_date = st.date_input(
#                 "Date of Offense", value="today", format="MM/DD/YYYY", disabled=True
#             )
#             due_date = offense_date + timedelta(days=30)
#             st.date_input(
#                 "Pay By Due Date", value=due_date, format="MM/DD/YYYY", disabled=True
#             )
#         with col2:
#             last_name = st.text_input("Last Name")
#             plate_number = st.text_input("Plate Number")
#             phone_number = st.text_input("Mobile_no")
#         location = st.text_input("Location")
#         offense_description = st.text_area("Ticket Details")
#         submit_button = st.form_submit_button("create ticket", type="primary")

#     if submit_button:
#         if not first_name or not last_name or not plate_number or not phone_number:
#             st.error("Please fill in all the required fields.")
#             st.stop()
#         else:
#             st.write(
#                 f"Fine of ${fine} for offense of {offense} has been submited for {first_name}"
#             )
#         tkt_attributes = {
#             "First Name": first_name,
#             "Last Name": last_name,
#             "Offense": offense,
#             "Fine Amount": fine,
#             "License Plate": plate_number,
#             "Date Issued": offense_date,
#             "Due Date": due_date,
#             "Phone Number": phone_number,
#             "Location": location,
#             "Description": offense_description,
#         }
#         df = pd.DataFrame(tkt_attributes, index=[0])
#         st.write("Ticket Submitted")
#         return df


# def run_program(logged_on_officer: str) -> pd.DataFrame:
#     # Make sure Officer is logged on
#     if logged_on_officer:
#         tkt_issued = create_offense()
#         if tkt_issued is not None:
#             n = 6
#             my_df = pd.DataFrame(tkt_issued)
#             my_df["Officer Name"] = logged_on_officer
#             my_df["tkt_number"] = "".join(
#                 ["{}".format(randint(0, 9)) for num in range(0, n)]
#             )
#         else:
#             st.warning("Select a ticket to begin")
#             st.stop()
#     try:
#         return my_df
#     except UnboundLocalError as e:
#         st.write("Logged out")
#         st.stop()
#         return


# def insert_offense(db_connection, offense_details: pd.DataFrame):
#     # Hard coded because data_frame columns are different form actual table columns
#     cols = [
#         "first_name",
#         "last_name",
#         "offence_type",
#         "fine_amount",
#         "license_plate",
#         "date_issued",
#         "due_date",
#         "phone_number",
#         "location",
#         "description",
#         "officer_name",
#         "tkt_number",
#     ]

#     query = (
#         f"""INSERT INTO traffic_tickets ({', '.join([i for i in cols])}) VALUES %s;"""
#     )
#     offense_details["Fine Amount"] = offense_details["Fine Amount"].astype(int)
#     values = tuple(offense_details.iloc[0])
#     with db_connection() as conn:
#         with conn.cursor() as cursor:
#             mogrified_query = cursor.mogrify(query, (values,))
#             cursor.execute(mogrified_query)
#             conn.commit()
#             cursor.close()
#             return True


# # Main Streamlit app
# def main():
#     username = my_authentication()
#     if username:
#         # Check if the username is an admin or a regular user
#         if is_admin(username):
#             admin_page.display_data()
#         else:
#             insert_offense(create_connection, run_program(username))


# if __name__ == "__main__":
#     main()

""" Trying to Debug from here"""
import json


st.write("debugging deployment")


def get_offense_category() -> dict:
    with open("offense_dictionary.json", "r") as f:
        offense_dictionary = json.load(f)
        return offense_dictionary


def create_offense() -> pd.DataFrame:
    # Get the offence info
    # offense, fine = select_offence(get_offense_category())

    # Input Offender Forms
    with st.form(key="offense_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        # Use a select box for the offense
        with col1:
            first_name = st.text_input("First Name")
            offense_date = st.date_input(
                "Date of Offense", value="today", format="MM/DD/YYYY", disabled=True
            )
            due_date = offense_date + timedelta(days=30)
            st.date_input(
                "Pay By Due Date", value=due_date, format="MM/DD/YYYY", disabled=True
            )
        with col2:
            last_name = st.text_input("Last Name")
            plate_number = st.text_input("Plate Number")
            phone_number = st.text_input("Mobile_no")
        location = st.text_input("Location")
        offense_description = st.text_area("Ticket Details")
        submit_button = st.form_submit_button("create ticket", type="primary")

    if submit_button:
        if not first_name or not last_name or not plate_number or not phone_number:
            st.error("Please fill in all the required fields.")
            st.stop()
        else:
            st.write("Nothing to submit")
        # else:
        #     st.write(
        #         f"Fine of ${fine} for offense of {offense} has been submited for {first_name}"
        #     )
        tkt_attributes = {
            "First Name": first_name,
            "Last Name": last_name,
            # "Offense": offense,
            # "Fine Amount": fine,
            "License Plate": plate_number,
            "Date Issued": offense_date,
            "Due Date": due_date,
            "Phone Number": phone_number,
            "Location": location,
            "Description": offense_description,
        }
        df = pd.DataFrame(tkt_attributes, index=[0])
        st.write("Ticket Submitted")
        return df
