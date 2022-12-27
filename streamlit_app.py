import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My friends are happy')
streamlit.header('🍞 Dinner menu')
streamlit.text(' 🐔 Murg Khalipha')
streamlit.text('Daru tochan')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

my_fruit_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[my_fruit_selected]
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

streamlit.header("Fruityvice Fruit Advice!")
# normalise json data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# show the normalise data as table
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row_all = my_cur.fetchall()
streamlit.header("Fruit List")
streamlit.dataframe(my_data_row_all)

fruit_choice = streamlit.text_input('What fruit would you like to add?','kiwi')
streamlit.write('The user entered ', fruit_choice)





