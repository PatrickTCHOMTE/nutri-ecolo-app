import streamlit as st
from st_files_connection import FilesConnection
import skimpy as skim
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("nutri-ecolo-app-data/open_food_data_final_cleaned.csv", input_format="csv")

#
def recommander_produits_meilleurs_eco_nutri_score(product_name, dataframe):
    liste_noms_produits = list(dataframe['product_name'].unique())
    liste_noms_produits_miniscules = [nom_produit.lower() for nom_produit in liste_noms_produits]

    if product_name == '':
        return
    elif product_name.lower() not in liste_noms_produits_miniscules:
        return
    else:
        # group_pnns_1 = dataframe[dataframe['product_name'] == product_name].iat[0, 3]
        product_pnns_group_2 = dataframe[dataframe['product_name'] == product_name].iat[0, 4]
        # product_score = dataframe[dataframe['product_name'] == product_name].iat[0, 19]

        df_produit = dataframe[dataframe['product_name'] == product_name].sort_values('ECO-NUTRI-SCORE', ascending=False).head(1)
        nom = df_produit.iat[0, 1]
        marque = df_produit.iat[0, 2]
        score = df_produit.iat[0, 19]
        recommandations = \
        dataframe[(dataframe['pnns_groups_2'] == product_pnns_group_2) & (dataframe['ECO-NUTRI-SCORE'] > score)][
            ['product_name', 'brands_tags', 'pnns_groups_2', 'ECO-NUTRI-SCORE']].sort_values('ECO-NUTRI-SCORE', ascending=False)
        return nom, marque, product_pnns_group_2, score, recommandations


# Display a dataframe as an interactive table
st.dataframe(df)
# st.write(skim(df))
pr = df.profile_report()
st_profile_report(pr)


