import streamlit as st

# st.title('Expense Management System')
# expense_dt = st.date_input('Expense Date: ')
# if expense_dt:
#     st.write(f'fetching expense for {expense_dt}')

# Text Elements


st.header('streamlit core features')
st.subheader('Text Elements')
st.text('This is simple text element.')

# Data display

# st.subheader('Data Display')
# st.write('Here is a simple table: ')
# st.table({'column 1': [1,2,3], 'column 2': [4,5,6]})
#
# st.subheader('charts')
#
# data = [20,30,50,60]
# st.bar_chart(data= data)
# st.line_chart(data=data)

value = st.slider(label='Ratings', min_value=1, max_value=5)
if value:
    st.write(f'Feedback taken as {value} ⭐ ')

option = st.selectbox(label='select category', options=['Food', 'Rent', 'Shopping'])
if option:
    st.write(f'you select {option}')

value = st.checkbox(label='Yes/No')
print(value)
