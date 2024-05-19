import geopandas as gpd
import pandas as pd

# Load shapefile
shapefile_path = r"C:\Users\Desktop\MYS.shp"  #your shp file path
gdf = gpd.read_file(shapefile_path)

# Load CSV file with lat/long coordinates, specify encoding
csv_file_path = r"C:\Users\Desktop\LBT2020_latest.csv" #your data in csv format
try:
    df = pd.read_csv(csv_file_path, encoding='latin1')
except UnicodeDecodeError:
    df = pd.read_csv(csv_file_path, encoding='utf-8')

# Convert lat/long coordinates to GeoDataFrame
geometry = gpd.points_from_xy(df['Longitude'], df['Latitude'])
points = gpd.GeoDataFrame(df, geometry=geometry, crs=gdf.crs)

# Perform spatial join
joined = gpd.sjoin(points, gdf, how="inner", op='within')

# Drop unnecessary columns from the joined DataFrame
joined.drop(columns=['index_right'], inplace=True)

# Save the result to CSV
result_csv_path = r"C:\Users\Desktop\LBT2020_latest_cleaned.csv" #your cleansed data save path
joined.to_csv(result_csv_path, index=False)

print("Data has been saved")
