import streamlit as st
import pandas as pd
import plotly.express as px

# Define file paths
agriculture_files = {
    "Ground Water Level": 'DataSets/Agriculture/Telangana_GrounWaterLevel_Overall/Telangana_GrounWaterLevel_Overall.csv',
    "Suryapet Crop": 'DataSets/Agriculture/Suryapet_mandal_wise_crop/Suryapet_mandal_wise_crop.csv',
    "Cash Crops": 'DataSets/Agriculture/Cash_crops_2016-2017/Cash_crops_2016-2017.csv',
    "Adilabad Crop": 'DataSets/Agriculture/Adilabad_mandal_wise_crop/Adilabad_mandal_wise_crop.csv',
    "Cereals and Millets": 'DataSets/Agriculture/Cereals_and_Millets_2016-2017/Cereals_and_Millets_2016-2017.csv'
}

health_files = {
    "Urban Health Centers": 'DataSets/Health/Urban Health Centers.csv',
    "Primary Health Centers": 'DataSets/Health/Primary Health Centers.csv',
    "District Health Assets": 'DataSets/Health/District wise health general asset .csv',
    "Area of Hospitals": 'DataSets/Health/Area of Hospitals .csv',
    "Community Health Centers": 'DataSets/Health/Community Health Centers.csv',
    "Overview of Hospitals": 'DataSets/Health/overview_of_hospitals.csv'
}

infrastructure_files = {
    "Classification of Roads": 'DataSets/infrastructure/Classification of Roads.csv',
    "Mission Kakateeya": 'DataSets/infrastructure/Mission Kakateeya.csv',
    "Electricity Connections": 'DataSets/infrastructure/Electricity Connections.csv',
    "2BHK Housing Scheme": 'DataSets/infrastructure/2BHK Housing Scheme.csv'
}

# Define a function to load and display data
def load_and_display_data(file_path):
    df = pd.read_csv(file_path)
    st.write(df)
    return df

def home():
    st.markdown("<h2 style='text-align: center; font-size: 24px;'>Welcome to the Visual Space!</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Overview
        Explore Telangana's diverse sectors—Agriculture, Health, and Infrastructure—with interactive data visualizations.
        Gain valuable insights and make informed decisions with our comprehensive data analysis tools.

        
        ![Telangana Symbol](https://www.telangana.gov.in/wp-content/uploads/2022/10/Telangana-Map-HomePage-33districts.png)

        ### About Us
        We are a team of 5 passionate individuals dedicated to providing easy access to valuable data with enhanced data visualization and analysis capabilities. Our goal is to empower users with insightful tools to explore and understand Telangana's key sectors.

        Choose a sector and sub-sector from the sidebar to explore detailed information and visualize data.
    """)


def future_implementations():
    st.write("""Here we are using Adilabad weather data to predict wind speed using temperature and humidity as inputs. This can be extended to any other districts data. """)
    st.link_button("Click here for the prediction","https://wind-speed-prediction.streamlit.app/")

# Assuming these functions are defined elsewhere in your code
def load_and_display_data(file_path):
    # Placeholder function for loading and displaying data
    # Replace this with actual logic to load and display data
    return pd.DataFrame()  # Return a sample DataFrame for demonstration

# Example dictionaries for agriculture, health, and infrastructure files
agriculture_files = {
    'Ground Water Level': 'path/to/gw_level.csv',
    'Suryapet Crop': 'path/to/suryapet_crop.csv',
    # Add other agriculture files here
}

health_files = {
    'Urban Health Centers': 'path/to/urban_health_centers.csv',
    'Primary Health Centers': 'path/to/primary_health_centers.csv',
    # Add other health files here
}

infrastructure_files = {
    '2BHK Housing Scheme': 'path/to/2bkhousing_scheme.csv',
    'Classification of Roads': 'path/to/classification_of_roads.csv',
    # Add other infrastructure files here
}

# # Define your sectors function
# def sectors():
#     # Sector selection
#     sector_options = ['Agriculture', 'Health', 'Infrastructure']
#     selected_sector = st.selectbox('Select a sector', sector_options)

#     if selected_sector == 'Agriculture':
#         agriculture_options = list(agriculture_files.keys())
#         selected_agriculture_sector = st.selectbox('Select a sub-sector', agriculture_options)

#         st.header(f'Agriculture Data: {selected_agriculture_sector}')
#         df_agriculture = load_and_display_data(agriculture_files[selected_agriculture_sector])

#         # Visualization for Agriculture data
#         if selected_agriculture_sector == 'Ground Water Level':
#             fig = px.bar(df_agriculture, x='mandal', y='value', title='Ground Water Level by Mandal')
#         elif selected_agriculture_sector == 'Suryapet Crop':
#             fig = px.bar(df_agriculture, x='mandalname', y='actualareasown', title='Suryapet Crop Area by Mandal')
#         elif selected_agriculture_sector == 'Cash Crops':
#             fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cash Crops Area by Crop')
#         elif selected_agriculture_sector == 'Adilabad Crop':
#             fig = px.bar(df_agriculture, x='mandal_name', y='actual_area', title='Adilabad Crop Area by Mandal')
#         elif selected_agriculture_sector == 'Cereals and Millets':
#             fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cereals and Millets Area by Crop')
#         else:
#             fig = px.bar(df_agriculture, x='crop', y='area_total', title='General Agriculture Data')

#         st.plotly_chart(fig)

#     elif selected_sector == 'Health':
#         health_options = list(health_files.keys())
#         selected_health_sector = st.selectbox('Select a sub-sector', health_options)

#         st.header(f'Health Data: {selected_health_sector}')
#         df_health = pd.read_csv(health_files[selected_health_sector])

#         # Visualization for Health data
#         if 'Urban Health Centers' in selected_health_sector:
#             fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
#         elif selected_health_sector == 'Primary Health Centers':
#             fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Primary Health Centers by District')
#         elif selected_health_sector == 'District Health Assets':
#             fig = px.bar(df_health, x='Districts_Hospital', y='SITE AREA ACRES', title='District Health Assets by Hospital')
#         elif selected_health_sector == 'Community Health Centers':
#             fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Community Health Centers by District')
#         elif selected_health_sector == 'Overview of Hospitals':
#             fig = px.bar(df_health, x='record_number', y='area_hospitals', title='Overview of Hospitals')
#         elif selected_health_sector == 'Area of Hospitals':
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Area of Hospitals by Village')
#         else:
#             fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='General Health Data')

#         st.plotly_chart(fig)

#     elif selected_sector == 'Infrastructure':
#         infrastructure_options = list(infrastructure_files.keys())
#         selected_infrastructure_sector = st.selectbox('Select a sub-sector', infrastructure_options)

#         st.header(f'Infrastructure Data: {selected_infrastructure_sector}')
#         df_infrastructure = pd.read_csv(infrastructure_files[selected_infrastructure_sector])

#         # Visualization for Infrastructure data
#         if selected_infrastructure_sector == '2BHK Housing Scheme':
#             fig = px.bar(df_infrastructure, x='Districts', y=['Houses Allotted', 'Houses Allotted Rural', 'Houses Allotted Urban', 'Houses Sanctioned'],
#                          title='2BHK Housing Scheme by District')
#         elif selected_infrastructure_sector == 'Classification of Roads':
#             fig = px.bar(df_infrastructure, x='District', y=['Four Lane Roads', 'Double Lane Roads', 'Intermediate Lane Roads', 'Single Lane Roads'],
#                          title='Classification of Roads by District')
#         elif selected_infrastructure_sector == 'Electricity Connections':
#             fig = px.bar(df_infrastructure, x='Districts', y=['Domestic Connections', 'Industrial Connections', 'Agriculture Connections', 'Commercial Connections', 'Other Connections'],
#                          title='Electricity Connections by District')
#         elif selected_infrastructure_sector == 'Gram Panchayat Roads':
#             fig = px.bar(df_infrastructure, x='Districts', y=['GPs having BT roads', 'GPs to be covered with BT roads', 'Total Habitations (other than GPs)', 'Habitations having all weather roads', 'Habitations not having all weather roads'],
#                          title='Gram Panchayat Roads by District')
#         elif selected_infrastructure_sector == 'Mission Kakateeya':
#             fig = px.bar(df_infrastructure, x='Districts', y=['Minor Irrigation Tanks', 'Sanctions Mission Kakatiya Phase-I', 'Sanctions Mission Kakatiya Phase-II'],
#                          title='Mission Kakateeya by District')
            
#         st.plotly_chart(fig)


# # Page configuration
# pages = {
#     "Home": home,
#     "Sectors": sectors,
#     "Future Implementations": future_implementations
# }

# def main():
#     # Navigation sidebar
#     st.sidebar.title("Navigation")
#     selection = st.sidebar.radio("Go to", list(pages.keys()))
    
#     # Display the selected page with its contents
#     pages[selection]()

# if __name__ == "__main__":
#     main()



# Sector selection
sector_options = ['Agriculture', 'Health', 'Infrastructure']
selected_sector = st.sidebar.selectbox('Select a sector', sector_options)

if selected_sector == 'Agriculture':
    agriculture_options = list(agriculture_files.keys())
    selected_agriculture_sector = st.sidebar.selectbox('Select a sub-sector', agriculture_options)

    st.header(f'Agriculture Data: {selected_agriculture_sector}')
    df_agriculture = load_and_display_data(agriculture_files[selected_agriculture_sector])

    # Visualization for Agriculture data
    if selected_agriculture_sector == 'Ground Water Level':
        fig = px.bar(df_agriculture, x='mandal', y='value', title='Ground Water Level by Mandal')
        st.plotly_chart(fig)
    elif selected_agriculture_sector == 'Suryapet Crop':
        fig = px.bar(df_agriculture, x='mandalname', y='actualareasown', title='Suryapet Crop Area by Mandal')
        st.plotly_chart(fig)
    elif selected_agriculture_sector == 'Cash Crops':
        fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cash Crops Area by Crop')
        st.plotly_chart(fig)
    elif selected_agriculture_sector == 'Adilabad Crop':
        fig = px.bar(df_agriculture, x='mandal_name', y='actual_area', title='Adilabad Crop Area by Mandal')
        st.plotly_chart(fig)
    elif selected_agriculture_sector == 'Cereals and Millets':
        fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cereals and Millets Area by Crop')
        st.plotly_chart(fig)
    elif 'Weather' in selected_agriculture_sector:
        df_weather_2021 = load_and_display_data(agriculture_files['Weather 2021'])
        df_weather_2022 = load_and_display_data(agriculture_files['Weather 2022'])
        df_weather_2023 = load_and_display_data(agriculture_files['Weather 2023'])
        
        df_weather_2021['Year'] = '2021'
        df_weather_2022['Year'] = '2022'
        df_weather_2023['Year'] = '2023'
        
        df_weather = pd.concat([df_weather_2021, df_weather_2022, df_weather_2023])
        
        fig = px.line(df_weather, x='date', y='value', color='Year', title='Temperature Trends (2021, 2022, 2023)')
        st.plotly_chart(fig)

elif selected_sector == 'Health':
    health_options = list(health_files.keys())
    selected_health_sector = st.sidebar.selectbox('Select a sub-sector', health_options)

    st.header(f'Health Data: {selected_health_sector}')
    df_health = pd.read_csv(health_files[selected_health_sector])

    # Visualization for Health data
    if 'Urban Health Centers' in selected_health_sector:
        fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
        st.plotly_chart(fig)
    
    elif selected_health_sector == 'Primary Health Centers':
        fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Primary Health Centers by District')
        st.plotly_chart(fig)
    
    elif selected_health_sector == 'District Health Assets':
        fig = px.bar(df_health, x='Districts_Hospital', y='SITE AREA ACRES', title='District Health Assets by Hospital')
        st.plotly_chart(fig)

    elif selected_health_sector == 'Community Health Centers':
        fig = px.bar(df_health, x='Districts', y='SITE AREA ACRES', title='Community Health Centers by District')
        st.plotly_chart(fig)

    elif selected_health_sector == 'Overview of Hospitals':
        fig = px.bar(df_health, x='record_number', y='area_hospitals', title='Overview of Hospitals')
        st.plotly_chart(fig)

    elif selected_health_sector == 'Area of Hospitals':
        fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Area of Hospitals by Village')
        st.plotly_chart(fig)



elif selected_sector == 'Infrastructure':
    infrastructure_options = list(infrastructure_files.keys())
    selected_infrastructure_sector = st.sidebar.selectbox('Select a sub-sector', infrastructure_options)

    st.header(f'Infrastructure Data: {selected_infrastructure_sector}')
    df_infrastructure = pd.read_csv(infrastructure_files[selected_infrastructure_sector])

    # Visualization for Infrastructure data
    if selected_infrastructure_sector == '2BHK Housing Scheme':
        fig = px.bar(df_infrastructure, x='Districts', y=['Houses Allotted', 'Houses Allotted Rural', 'Houses Allotted Urban', 'Houses Sanctioned'],
                     title='2BHK Housing Scheme by District')
        st.plotly_chart(fig)

    elif selected_infrastructure_sector == 'Classification of Roads':
        fig = px.bar(df_infrastructure, x='District', y=['Four Lane Roads', 'Double Lane Roads', 'Intermediate Lane Roads', 'Single Lane Roads'],
                     title='Classification of Roads by District')
        st.plotly_chart(fig)

    elif selected_infrastructure_sector == 'Electricity Connections':
        fig = px.bar(df_infrastructure, x='Districts', y=['Domestic Connections', 'Industrial Connections', 'Agriculture Connections', 'Commercial Connections', 'Other Connections'],
                     title='Electricity Connections by District')
        st.plotly_chart(fig)

    elif selected_infrastructure_sector == 'Gram Panchayat Roads':
        fig = px.bar(df_infrastructure, x='Districts', y=['GPs having BT roads', 'GPs to be covered with BT roads', 
                                                     'Total Habitations (other than GPs)', 'Habitations having all weather roads', 
                                                     'Habitations not having all weather roads'],
                 title='Gram Panchayat Roads by District')
        st.plotly_chart(fig)


    elif selected_infrastructure_sector == 'Mission Kakateeya':
        fig = px.bar(df_infrastructure, x='Districts', y=['Minor Irrigation Tanks', 'Sanctions Mission Kakatiya Phase-I', 'Sanctions Mission Kakatiya Phase-II'],
                     title='Mission Kakateeya by District')
        st.plotly_chart(fig)

# -----------------------------------------------------------
