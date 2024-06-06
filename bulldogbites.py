import streamlit as st
from datetime import datetime as dt

st.set_page_config(page_title="Bulldog Bites", page_icon="logo.png", layout="wide")

page = st.sidebar.radio("**Navigate:**", ["Home", "Food Information", "Order Online", "QuickBites Subscription™"])

if page == "Home":

    intro = """
    ---
    We are a catering service located in Sir Winston Churchill High School's cafeteria. We work to bring nutritious and
    delicious lunches to the people of Churchill in the most effective and convenient way possible.
    """

    st.write("---")
    st.title(":red[Bulldog] :blue[Bites]")
    st.write(intro)

    c1, c2 = st.columns(2)
    ex1, ex2 = c1.expander(":red[Our Mission]"), c2.expander(":red[Our Vision]")

    ex1.write("*“To serve tasty, fresh food in a friendly and inviting atmosphere”*")
    ex2.write("*“To be the top spot for delicious and wholesome food, creating a community hub where everyone feels welcome”*")

    st.write("---")

else:

    titleft = page.split(" ")

    st.write("---")
    st.title(f":red[{titleft[0]}] :blue[{titleft[1]}]")
    st.write("---")

    if page == "Food Information":
        pass

    if page == "Order Online":
        pass

    if page == "QuickBites Subscription™":
        pass
