from branca.element import IFrame
import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"]) 
lon = list(data["LON"])
elev = list(data["ELEV"])

def elevation_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 2000 <= elevation < 3000:
        return 'orange' 
    else:
        return 'red'

html = """<h4>Volcano Information:</h4> Height: %s m"""
map = folium.Map(location=[29.408101, -98.797383], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev): #using zip() allows you to take to lists and put them in pairs. ie. i[1] goes with j[1] etc.
    iframe = folium.IFrame(html=html % str(el), width=200, height=100) 
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color = elevation_color(el), color = 'grey', fill_opacity = 0.7)) #house coords


fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)

map.save("VolcanoMap.html")
