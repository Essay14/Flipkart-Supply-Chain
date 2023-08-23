#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas


# In[1]:


pip install pandas folium


# In[2]:


import pandas as pd
import folium

# Load the Excel file
df = pd.read_excel('Pincodes_FK.xlsx')

# Create a Folium map centered around the mean latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# Create a heat map layer
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
heat_map = folium.plugins.HeatMap(heat_data)

# Add the heat map layer to the map
heat_map.add_to(m)

# Save the map to an HTML file
m.save('heatmap.html')

# Open the HTML file in a web browser for interactive zooming and panning
import webbrowser
webbrowser.open('heatmap.html')


# In[5]:


import pandas as pd
import folium
import folium.plugins as plugins

# Load the Excel file
df = pd.read_excel('Pincodes_FK.xlsx')

# Create a Folium map centered around the mean latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# Create a list of latitudes and longitudes
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# Add the HeatMap layer to the map
folium.plugins.HeatMap(heat_data).add_to(m)

# Save the map to an HTML file
m.save('heatmap.html')

# Open the HTML file in a web browser for interactive zooming and panning
import webbrowser
webbrowser.open('heatmap.html')


# In[12]:


import pandas as pd
import folium
from sklearn.cluster import KMeans
import folium.plugins as plugins

# Load the Excel file
df = pd.read_excel('Pincodes_FK.xlsx')

# Create a Folium map centered around the mean latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# Create a list of latitudes and longitudes
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# Perform K-means clustering with k=6
kmeans = KMeans(n_clusters=12, random_state=0).fit(df[['Latitude', 'Longitude']])
df['Cluster'] = kmeans.labels_

# Define colors for clusters
cluster_colors = ['yellow', 'green', 'blue', 'purple', 'orange', 'gray', 'red', 'black', 'white', 'green', 'pink','brown']

# Add data points and clusters to the map
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=cluster_colors[row['Cluster']],
        fill=True,
        fill_color=cluster_colors[row['Cluster']]
    ).add_to(m)

# Save the map to an HTML file
m.save('clustered_heatmap.html')

# Open the HTML file in a web browser for interactive zooming and panning
import webbrowser
webbrowser.open('clustered_heatmap.html')


# In[42]:


import pandas as pd
import folium
from sklearn.cluster import KMeans
import folium.plugins as plugins

# L U C K N O W

# Load the Excel file
df = pd.read_excel('Pincodes_FK.xlsx')

# Create a Folium map centered around the mean latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

# Create a list of latitudes and longitudes
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# Perform K-means clustering with k=6
kmeans = KMeans(n_clusters=10, random_state=0).fit(df[['Latitude', 'Longitude']])
df['Cluster'] = kmeans.labels_

# Define colors for clusters
cluster_colors = ['black', 'blue', 'green', 'purple', 'orange', 'gray','white','red', 'blue','yellow']

# Add data points and clusters to the map
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=cluster_colors[row['Cluster']],
        fill=True,
        fill_color=cluster_colors[row['Cluster']]
    ).add_to(m)

# Add cluster centers as crosses with latitude and longitude in the popups
for center in kmeans.cluster_centers_:
    folium.Marker(
        location=[center[0], center[1]],
        icon=folium.Icon(icon='store'),  # You can choose a different icon here
        popup=f'Cluster Center\nLatitude: {center[0]}, Longitude: {center[1]}',
    ).add_to(m)

# Save the map to an HTML file
m.save('clustered_heatmap_with_coordinates.html')

# Open the HTML file in a web browser for interactive zooming and panning
import webbrowser
webbrowser.open('clustered_heatmap_with_coordinates.html')


# In[51]:


import pandas as pd
import folium
from sklearn.cluster import KMeans
import folium.plugins as plugins

# P U N E
# Load the Excel file
df = pd.read_excel('Pincodes_Pune.xlsx')

# Create a Folium map centered around the mean latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)

# Create a list of latitudes and longitudes
coordinates = df[['Latitude', 'Longitude']]

# Perform K-means clustering with k=5
kmeans = KMeans(n_clusters=14, random_state=0).fit(coordinates)
df['Cluster'] = kmeans.labels_

# Define colors for clusters
cluster_colors = ['red', 'blue', 'green', 'purple', 'orange','yellow', 'black', 'grey', 'pink', 'cyan','brown', 'violet', 'purple', 'green']

# Add data points and clusters to the map
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=cluster_colors[int(row['Cluster'])],
        fill=True,
        fill_color=cluster_colors[int(row['Cluster'])]
    ).add_to(m)

# Add cluster centers as markers
for center in kmeans.cluster_centers_:
    folium.Marker(
        location=[center[0], center[1]],
        icon=folium.Icon(icon='store'),  # You can choose a different icon here
        popup=f'Cluster Center\nLatitude: {center[0]}, Longitude: {center[1]}',
    ).add_to(m)

# Save the map to an HTML file
m.save('clustered_map_with_centers.html')

# Open the HTML file in a web browser for interactive zooming and panning
import webbrowser
webbrowser.open('clustered_map_with_centers.html')


# In[ ]:




