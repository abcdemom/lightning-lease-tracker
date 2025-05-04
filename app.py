import streamlit as st

# --- Page config must be first ---
st.set_page_config(page_title="Ford Lightning Lease Finder", layout="wide")

# --- Title ---
st.title("⚡ Ford F-150 Lightning Lease Tracker")
st.write("See real lease offers for your dream truck — filtered by color, cab size, and ZIP!")

# --- Get user input ---
zip_code = st.text_input("Enter ZIP code:", value="14450")
search_button = st.button("🔍 Search Deals")

# --- Simulated Search Results (for now) ---
if search_button:
    with st.spinner("Searching for the best Lightning deals..."):
        st.success("Done! (Simulated data for now)")

        # 🚧 Placeholder listings until scraping/API is resolved
        fake_listings = [
            {
                "title": "2025 Ford F-150 Lightning XLT",
                "price": "$628/mo lease",
                "dealer": "Bob Johnson Ford of Avon",
                "location": "Avon, NY",
                "msrp": "$69,115"
            },
            {
                "title": "2025 Ford F-150 Lightning Lariat",
                "price": "$712/mo lease",
                "dealer": "West Herr Ford of Rochester",
                "location": "Rochester, NY",
                "msrp": "$75,000"
            }
        ]

        for listing in fake_listings:
            st.markdown(f"### {listing['title']}")
            st.write(f"**Price:** {listing['price']}")
            st.write(f"**Dealer:** {listing['dealer']} ({listing['location']})")
            st.write(f"**MSRP:** {listing['msrp']}")
            st.markdown("---")