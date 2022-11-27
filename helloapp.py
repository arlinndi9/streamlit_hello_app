import streamlit as st
from datetime import date
st.title('streamlit')
st.text('hello')
st.subheader('helloapp')
today=date.today()
f_date = today
l_date = date(2023, 4, 3)
delta = l_date - f_date

st.write(today)
st.text('github')
st.header('my name is arlind ')
st.title(f'ditelindja ime eshte edhe {delta.days} dite ')