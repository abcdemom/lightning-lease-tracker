import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- Page Config ---
st.set_page_config(page_title="Ford Lightning Lease Finder", layout="wide")
st.title("⚡ Ford F-150 Lightning Lease Tracker")
st.write("See real lease offers for your dream truck — filtered by color, cab size, and ZIP!")

# --- Input ---
zip_code = st.text_input("Enter ZIP code:", value="14450")
search_button = st.button("🔍 Search Deals")

# --- Scraper Function ---
def scrape_edmunds(zip_code):
    url = f"https://www.edmunds.com/inventory/srp.html?extcolor=Dark%20Blue%2CGray%2CSilver&inventorytype=new&make=ford&model=ford%7Cf-150-lightning&paymenttype=lease&radius=500&truckCabSize=Crew%20Cab%20Pickup&wz={zip_code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("a", class_="usurp-inventory-card-vdp-link")
    
    listings = []
    for card in cards[:10]:
        parent = card.find_parent("li")
        title = card.text.strip()
        link = card.get("href", "")
        full_url = "https://www.edmunds.com" + link
        listings.append({
            "title": title or "Ford F-150 Lightning",
            "link": full_url
        })
    return listings

# --- Show Results ---
if search_button:
    with st.spinner("Searching for the best Lightning deals..."):
        listings = scrape_edmunds(zip_code)

        if not listings:
            st.warning("No listings found. Try a different ZIP.")
        else:
            st.success("Here are your listings!")
            for item in listings:
                st.markdown(f"### [{item['title']}]({item['link']})")
                st.markdown("---")