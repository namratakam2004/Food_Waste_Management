import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://neondb_owner:npg_5GAOUeQaZp4W@ep-shiny-frog-atr05zw4-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(DATABASE_URL)

# # Upload Providers
# providers = pd.read_csv("data/cleaned/Providers_data_cleaned.csv")
# providers.to_sql(
#     "providers_data",
#     engine,
#     if_exists="append",
#     index=False
# )

# # Upload Receivers
# receivers = pd.read_csv("data/cleaned/Receivers_data_cleaned.csv")
# receivers.to_sql(
#     "receivers_data",
#     engine,
#     if_exists="append",
#     index=False
# )

# # Upload Food Listings
# food = pd.read_csv("data/cleaned/Food_listing_data_cleaned.csv")
# food.to_sql(
#     "food_listing_data",
#     engine,
#     if_exists="append",
#     index=False
# )

# Upload Claims
claims = pd.read_csv("data/cleaned/Claims_data_cleaned.csv")
claims.to_sql(
    "claims_data",
    engine,
    if_exists="append",
    index=False
)

print("All data uploaded successfully!")