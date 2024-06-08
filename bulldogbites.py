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

    plan = """
    At Bulldog Bites, we are going to have an in-school area where you can buy breakfast during tutorial, and buy snacks and other items during lunch. These will be bought and shipped from our supplier Costco.
    Some items that we may decide to use are: chips, cookies, lemonade, salads, instant foods and cold foods.

    We will also have a subscription. In this people can pay an amount of money (eg. **\$50** for food items up to **\$35** per month - see chart above). With this
    subscription, customers pay a sum of money in advance to order food without payment for a month. This can help customers who forget their cash or card, so the money
    from the subscription can be used for their order. We will also be giving custom orders. These custom orders will have to be ordered through our website any time
    before **8 AM** on that day. Our supplier for these will be **EthniCity**, who are willing to drop off the food as a delivery at the start of lunch. Through our
    website, people can easily find information about our food and order online, giving fast and easy transactions so that people can just pay, grab and go. Our initial
    startup budget would be around **\$760**, which includes initial costs for food as well. Our projected revenue is **\$320** a day. From the profits we make, all the
    extra money we make will be used for charity donations, school fundraisers and events, to help our school become even more successful.
    """

    staffing = """
    Staffing members will include Churchill volunteers, people form this class, friends, and volunteering teachers. Our staffing could be any person that we trust as a
    group to maintain our business standards. These staffing members will still have to be trained enough to know how to handle basic tasks and keep quality customer
    service. 

    For a day-to-day staffing operation, we will have designated and pre-assigned schedules for people who want to participate in this business. If someone who has been
    scheduled for a shift doesn't show up they must find a replacement themselves, who will then be approved by us to volunteer.
    """

    contact = """
    *Email:* *Bulldog.bites.cafe@gmail.com*
    
    We respond in less than 24 hours (after business startup)
    """
    
    st.write("---")
    st.title(":red[Bulldog] :blue[Bites]")
    st.subheader(":green[*Coming Soon*]")
    st.write(intro)

    c1, c2 = st.columns(2)
    ex1, ex2 = c1.expander(":red[**Our Mission**]"), c2.expander(":red[**Our Vision**]")

    ex1.write("*“To serve tasty, fresh food in a friendly and inviting atmosphere”*")
    ex2.write("*“To be the top spot for delicious and wholesome food, creating a community hub where everyone feels welcome”*")

    st.write("---")
    st.header(":red[Our] :blue[Plan]")
    st.write(plan)

    st.header(":blue[Staffing]")
    st.write(staffing)

    st.header(":red[Contact] :blue[Us]")
    st.write(contact)

else:

    titleft = page.split(" ")

    st.write("---")
    st.title(f":blue[{titleft[0]}] :red[{titleft[1]}]")
    st.write("---")

    if page == "Food Information":
        pass

    if page == "Order Online":
        
        st.sidebar.write("Required fields are indicated by a **:red[*]** symbol.")
        st.sidebar.write("---")

        st.subheader("Name & Date of Birth")

        c1, c2, c3 = st.columns(3)

        firstname = c1.text_input("**First Name:red[ *]**")
        middlename = " "+c2.text_input("**Middle Name (Optional):**")
        lastname = c3.text_input("**Last Name:red[ *]**")

        if firstname != "" and lastname != "":
            fullname = f"{firstname}{middlename} {lastname}"
            fullnameft = f"{lastname}, {firstname}{middlename}"
        else:
            fullname = ""
            fullnameft = "N/A"


        c1, c2, c3 = st.columns(3)
        
        st.write("---")

        dob = {
            "Month": "January",
            "Year": 2024,
            "Day": 1
        }

        dob["Year"] = c3.selectbox("**Year:**", ["N/A"]+[i for i in range(2000, 2025)])
        dob["Month"] = c1.selectbox("**Month:**", ["N/A", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        
        if dob["Month"] == "February":
            
            if dob.Year % 4 == 0:
                days = [i for i in range(1, 30)]
            else:
                days = [i for i in range(1, 29)]

        elif dob["Month"] in ["January", "March", "May", "July", "August", "October", "December"]:
            days = [i for i in range(1, 32)]
        
        else:
            days = [i for i in range(1, 31)]
        

        dob["Day"] = c2.selectbox("**Day:**", ["N/A"]+days)

        st.subheader("Contact & Student Informaiton")

        c1, c2 = st.columns(2)

        email = c1.text_input("**Email (name@company.extension) - For Contacting Purposes**:")
        phonenumber = "".join("".join("".join("".join("".join("".join("".join(c2.text_input("**Phone Number (###-###-####) - For Contacting Purposes**:").split("-")).split("(")).split(")")).split("|")).split("/")).split(" ")).split("."))

        try:
            invnum = False
            phonenumber = int(phonenumber)
            phonenumber = str(phonenumber)
        except:
            if phonenumber != "":
                st.sidebar.write("**:red[Please enter a valid phone number.]**")
                invnum = True

        st.write("**:green[Enter at least one of these pieces of information below:]**")

        c1, c2 = st.columns(2)

        pronouns = c1.radio("**Pronouns: :red[*]**", ["Prefer Not to Say", "He/Him (Male)", "She/Her (Female)", "They/Them (Non-Binary)", "Other (Please Specify Below)"])
        grade = c2.radio("**Grade** :red[*]", [10, 11, 12, "Not a Student at SWC"])

        if "Other" in pronouns:
            otherpronouns = c1.text_input("**Other Pronouns:**")
            

        if email == "":
            email = "N/A"
        
        if phonenumber != "" and not invnum:
            phonenumber = f"*({phonenumber[:3]}) {phonenumber[3:6]}-{phonenumber[6:10]}*"
        else:
            phonenumber = "N/A"

        if dob["Day"] != "N/A" and dob["Month"] != "N/A" and dob["Year"] != "N/A":
            dobstr = f"{dob['Month']} {dob['Day']}, {dob['Year']}"
        else:
            dobstr = "N/A"

        info = {
            "First Name": firstname,
            "Middle Name": middlename,
            "Last Name": lastname,
            "Pronouns": pronouns,
            "Email": email,
            "Phone Number": phonenumber
        }

        infostr = f"""
        **Name**: {fullnameft}
        
        **Pronouns**: {pronouns}

        **Grade**: {grade}

        **Date of Birth**: {dobstr}

        **Email**: *{email}*
        
        **Phone Number**: *{phonenumber}*
        
        ---
        """

        st.sidebar.write(infostr)

    if page == "QuickBites Subscription™":
        pass
