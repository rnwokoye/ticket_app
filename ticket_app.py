import streamlit as st
import pandas as pd
import numpy as np
import hmac


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
            return True

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            authenticated_user = st.session_state.username
            st.write(f"Welcome {authenticated_user}")
            del st.session_state["password"]  # Don't store the username or password.
            # del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
            if "authenticated_user" in st.session_state:
                del st.session_state["authenticated_user"]

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here now also
logout = st.button("log_out")
if logout:
    for key in st.session_state.keys():
        del st.session_state[key]


# Ticket Variables changed?
offense_fines = {
    "Choose An Option": "",
    "Speeding": 100,
    "Running a Red Light": 200,
    "Illegal Parking": 50,
    "Driving Without a License": 300,
    "Drunk_Driving": 400,
    "Overtaking": 250
    # ... more offenses
}

# App Title
st.header("Traffice Enforcement System")


def select_offence():
    # Use a select box for the offense
    selected_offense = st.selectbox(
        "Choose an offense:",
        options=list(offense_fines.keys()),
        index=0,
        placeholder="Choose an option",
        key="selected_offense",
    )
    fine = offense_fines[selected_offense]
    if fine == "":
        st.write("Please select an Offense to start")
    else:
        st.write(f"${fine}")

    return (selected_offense, fine)


# Enter Form Details
def create_offense():
    offense, fine = select_offence()
    # Start a form
    with st.form(key="offense_form", clear_on_submit=True):
        # Create 2 columns
        col1, col2 = st.columns(2)

        # Use a select box for the offense
        with col1:
            first_name = st.text_input("First Name")
            offense_date = st.date_input("Date of Offense", value="today")

        with col2:
            last_name = st.text_input("Last Name")
            plate_number = st.text_input("Plate Number")

        location = st.text_input("Location")
        offense_description = st.text_area("Ticket Details")

        submit_button = st.form_submit_button("create ticket")

    if submit_button:
        st.write(
            f"Fine of ${fine} for offense of {offense} has been submited for {first_name}"
        )


if __name__ == "__main__":
    create_offense()
