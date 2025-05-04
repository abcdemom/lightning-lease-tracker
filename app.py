import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Ford Lightning Lease Tracker", layout="wide")

# --- App Header ---
st.title("⚡ Ford F-150 Lightning Lease Tracker")
st.write("See real lease offers for your dream truck — filtered by color, cab size, and ZIP!")

# --- Input ---
zip_code = st.text_input("Enter ZIP code:", value="14450")
search_button = st.button("🔍 Search Deals")

# --- Your filtered Edmunds link ---
filtered_url = f"https://www.edmunds.com/inventory/srp.html?extcolor=Dark%20Blue%2CGray%2CSilver&inventorytype=new&make=ford&model=ford%7Cf-150-lightning&paymenttype=lease&radius=500&truckCabSize=Crew%20Cab%20Pickup&wz={zip_code}"

if search_button:
    with st.spinner("Searching for the best Lightning deals..."):

        # --- Placeholder Listings ---
        listings = [
            {
                "title": "2025 Ford F-150 Lightning XLT",
                "price": "$628/mo lease",
                "dealer": "Bob Johnson Ford of Avon (Avon, NY)",
                "msrp": "$69,115"
            },
            {
                "title": "2025 Ford F-150 Lightning Lariat",
                "price": "$712/mo lease",
                "dealer": "West Herr Ford of Rochester (Rochester, NY)",
                "msrp": "$75,000"
            }
        ]

        # --- Show Listings ---
        st.success("Done! (Simulated data for now)")
        for listing in listings:
            st.markdown(f"### {listing['title']}")
            st.write(f"**Price:** {listing['price']}")
            st.write(f"**Dealer:** {listing['dealer']}")
            st.write(f"**MSRP:** {listing['msrp']}")
            st.markdown("---")

        # --- Link to Edmunds ---
        st.markdown(f"🔗 [View more on Edmunds]({filtered_url})")