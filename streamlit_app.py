import streamlit
import pandas
streamlit.title('My friends are happy')
streamlit.header('🍞 Dinner menu')
streamlit.text(' 🐔 Murg Khalipha')
streamlit.text('Daru tochan')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avacado'])
streamlit.dataframe(my_fruit_list)

