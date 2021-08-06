import geocoder
import folium
import GoogleMyMaps

g = geocoder.ip("36.81.172.149")

myAdress = g.latlng

my_map1 = folium.Map(Location=myAdress,
                     zoom_start= 12)

folium.CircleMarker(location=myAdress,
                    radius=50, popup="yorkshire").add_to(my_map1)

my_map1.save("my_map.html")
