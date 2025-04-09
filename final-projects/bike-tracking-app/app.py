# import streamlit as st
# import requests
# import folium
# from streamlit_folium import st_folium

# response = requests.get("http://ip-api.com/json/")
# data = response.json()
# map_url = f"https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d115824.16752679084!2d{data["lon"]}!3d{data["lat"]}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2s!4v1743349480947!5m2!1sen!2s"

# m =folium.Map(location=[data["lat"], data["lon"]]) # lattitude first then longitude
# folium.Marker([data["lat"], data["lon"]], popup="Karachi, Pakistan", tooltip="Click for more").add_to(m)
# st_folium(m, width=400, height=400)
 
