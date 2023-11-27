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
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True
        # return st.session_state["username"]

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here now also
# st.subheader(f"Welcome {user_nme}")
st.button("Click me")


# Ticket Variables
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
    user_name = check_password()
    st.subheader(f"Welcome {user_name}")
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


# # Use a select box for the offense
# selected_offense = st.selectbox(
#     "Choose an offense:",
#     options=list(offense_fines.keys()),
#     index=0,
#     key="selected_offense",
# )

# # Display the corresponding fine amount
# fine = offense_fines[selected_offense]
# st.write(f"${fine}")

# Form Inputs
# st.text("Create a ticket")
# ticket = st.form("new_ticket")


# # Offence Details
# first_name = ticket.text_input("First Name")
# last_name = ticket.text_input("Last Name")
# offense_date = ticket.date_input("Date of Offense", value="today")
# plate_number = ticket.text_input("Plate Number")
# location = ticket.text_input("Location")
# offense_fine = ticket.text_input(
#     label=selected_offense, value=f"${fine}", disabled=True
# )

# offense_description = ticket.text_area("Ticket Details")

# submit = ticket.form_submit_button("create ticket")

# st.text("Testing Magic")
# df = pd.DataFrame({"col1": [1, 2, 3]})
# df  # 👈 Draw the dataframe

# x = 10
# "x", x  # 👈 Draw the string 'x' and then the value of x
