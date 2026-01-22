from datetime import datetime
import streamlit as st
import requests
import pandas as pd


API_URL = 'http://localhost:8000'

def analytics_tab():

    col1,col2 = st.columns(2)

    with col1:
        selected_start_date = st.date_input(' start date', datetime(2024, 8, 1))

    with col2:
        selected_end_date = st.date_input(' end date', datetime(2024, 8, 5),)

    if st.button('Get analytics'):
        payload = {
            'start_date'  : selected_start_date.strftime('%Y-%m-%d'),
            'end_date' : selected_end_date.strftime('%Y-%m-%d')
        }
        response = requests.post(f'{API_URL}/analytics/', json=payload)
        if response.status_code == 200 :
            data = response.json()
            df = pd.DataFrame({
                'Category' : list(data.keys()) ,
                'Total' : [ data[category]['total'] for category in data],
                'Percentage' : [  data[category]['percentage'] for category in data]
            })
            df_sorted = df.sort_values(by='Percentage', ascending=False)

            st.title('Expense Breakdown By Category')
            st.bar_chart(data = df_sorted.set_index('Category')['Percentage'])

            st.table(df_sorted)

        else:
            st.error('Failed to retrieve data')
