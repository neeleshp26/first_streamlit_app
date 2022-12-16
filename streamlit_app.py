import streamlit
import pandas
streamlit.title('My friends are happy')
streamlit.header('🍞 Dinner menu')
streamlit.text(' 🐔 Murg Khalipha')
streamlit.text('Daru tochan')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
