import pandas as pd
from geopy.geocoders import nominatim
from geopy.exc import GeocoderTimedOut

#Load the excel file
df = pd.read_excel(r"C:\Users\Desktop\LBT2020.xlsx")

#Fill missing values in 'Negeri', 'Daerah', 'Date' and 'Ruj No' column with values from the rows above
df['Negeri'].fillna(method='ffill', inplace=True)
df['Daerah'].fillna(method='ffill', inplace=True)
df['Date'].fillna(method='ffill', inplace=True)
df['Ruj No'].fillna(method='ffill', inplace=True)

#Function to geocode addresses and get latitude and longitude
def geocode_address(address)
    geolocator = Nominatim(user_agent="flood_geocoder", timeout=10) #Adjust timeout as needed
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut
        return None, None

# Fill missing latitude and longitude values using geocoding
for index, row in df.iterrows():
    if pd.isnull(row['Latitude']) or pd.isnull(row['Longitude']):
        address = f"{row['Kawasan Banjir']}, {row['Daerah']}, {row['Negeri']}, Malaysia" 
        latitude, longitude = geocode_address(address)
        df.at[index, 'Latitude'] = latitude
        df.at[index, 'Longitude'] = longitude

# Save the updated DataFrame to a new Excel file
df.to_excel(r"C:\Users\Desktop\LBT2022_latest.xlsx")

print("File has been saved.")
