import streamlit as st

st.title("⚡ Ford F-150 Lightning Lease Tracker")

if st.button("Show Deals"):
    st.write("🚙 Here's where your Edmunds listings will go!")

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# --- Page config ---
st.set_page_config(page_title="Ford Lightning Lease Finder", layout="wide")
st.title("⚡ Ford Lightning Lease Finder")
st.write("See real lease offers for your dream truck — filtered by color, cab size, and ZIP!")

# --- Get user input ---
zip_code = st.text_input("Enter ZIP code:", value="14450")
search_button = st.button("🔍 Search Deals")

if search_button:
    with st.spinner("Searching for the best Lightning deals..."):

        # -- Set up driver --
        chrome_path = "/Users/rachelkennedy/Desktop/chromedriver-mac-arm64/chromedriver"  # Update if needed
        service = Service(chrome_path)
        driver = webdriver.Chrome(service=service)

        # -- Filtered Edmunds URL --
        base_url = f"https://www.edmunds.com/inventory/srp.html?extcolor=Dark%20Blue%2CGray%2CSilver&inventorytype=new&make=ford&model=ford%7Cf-150-lightning&paymenttype=lease&radius=500&truckCabSize=Crew%20Cab%20Pickup&wz={zip_code}"
        driver.get(base_url)
        time.sleep(10)  # Let JS load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.find_all("div", class_="srp-card")

        if not cards:
            st.warning("No listings found. Try a different ZIP code.")
        else:
            for card in cards[:10]:  # Limit to first 10 listings
                try:
                    title = card.find("h2").text.strip()
                    price = card.find("span", class_="heading-3 text-black").text.strip()
                    dealer = card.find("div", class_="dealer-name").text.strip()
                    location = card.find("div", class_="dealer-location").text.strip()
                    msrp = card.find("div", string=lambda s: s and "MSRP" in s)
                    msrp_value = msrp.find_next("div").text.strip() if msrp else "N/A"

                    st.markdown(f"### {title}")
                    st.write(f"**Price:** {price}")
                    st.write(f"**Dealer:** {dealer}, {location}")
                    st.write(f"**MSRP:** {msrp_value}")
                    st.markdown("---")
                except Exception as e:
                    st.write("⚠️ Skipping listing due to error.")
        
        driver.quit()