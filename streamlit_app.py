import streamlit

streamlit.title('My parents New Healthy Dinner')

streamlit.header('Breakfast Favourites')
streamlit.text (' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale , Spinach and Rocket Smoothie')                
streamlit.text (' 🐔 Hard-boiled free-range Egg')
streamlit.text (' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.readc_csv(htpps://"https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlist.dataframe(my_fruit_list)
