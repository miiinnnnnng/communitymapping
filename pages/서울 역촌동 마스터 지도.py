import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium
import folium
import os

# Initialize the app
st.title("개인용기 지참 시 혜택을 주는 가게")

# Initialize the geolocator
geolocator = Nominatim(user_agent="community-mapping")

# File path for CSV storage
DATA_FILE = "locations.csv"

# Load existing data or create a new DataFrame
if os.path.exists(DATA_FILE):
    locations_df = pd.read_csv(DATA_FILE)
else:
    locations_df = pd.DataFrame(columns=["location", "latitude", "longitude", "info"])

# Input fields for address and related information
st.sidebar.header("새로운 장소를 입력하세요.")
address = st.sidebar.text_input("주소:")
info = st.sidebar.text_input("가게명과 혜택 정보:")
add_button = st.sidebar.button("장소 저장")

# Process the input when the button is clicked
if add_button:
    if address and info:
        try:
            # Get geolocation
            location = geolocator.geocode(address)
            if location:
                new_data = {
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                    "info": info
                }
                new_data_df = pd.DataFrame([new_data])  # 새로운 데이터를 DataFrame으로 변환
                locations_df = pd.concat([locations_df, new_data_df], ignore_index=True)  # 데이터 병합
                locations_df.to_csv(DATA_FILE, index=False)  # Save to CSV
                st.sidebar.success("Location added successfully!")
            else:
                st.sidebar.error("Could not find the address. Try again.")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
    else:
        st.sidebar.error("Please enter both address and information.")

# Display the map
st.subheader("지도에 표시된 장소들을 확인해보세요.")
m = folium.Map(location=[37.601640, 126.914521], zoom_start=15)  # Center on Seoul by default

# Add CircleMarkers for each location
for _, loc in locations_df.iterrows():
    folium.CircleMarker(
        location=[loc["latitude"], loc["longitude"]],  # 마커 위치
        radius=5,  # 점의 크기
        color="green",  # 점의 테두리 색상
        fill=True,  # 점 내부 채우기 활성화
        fill_color="green",  # 점 내부 색상
        fill_opacity=0.8,  # 점 투명도
        popup=loc["info"]  # 팝업 내용
    ).add_to(m)


# Render the map in Streamlit
st_folium(m, width=700, height=500)
