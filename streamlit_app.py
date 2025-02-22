import streamlit as st
#import snowflake.connector 
import numpy as np
import pandas as pd
  
st.title('Papeleria') 

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({ 'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40] }))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
chart_data = pd.DataFrame( np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)


map_data = pd.DataFrame( np.random.randn(1000, 2) / [50, 50] + [19.24, -98.99], columns=['lat', 'lon']) 
st.map(map_data)

x = st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.text_input("Your name", key="name") 
# You can access the value at any point with: st.session_state.name



if st.checkbox('Show dataframe'): 
  vchart_data = pd.DataFrame( 
    np.random.randn(20, 3), 
    columns=['a', 'b', 'c']) 
  chart_data


df = pd.DataFrame({ 
  'first column': [1, 2, 3, 4], 
  'second column': [10, 20, 30, 40] }) 
option = st.selectbox( 
  'Which number do you like best?', 
  df['first column']) 

'You selected: ', option



# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2) 
# You can use a column just like st.sidebar: 
left_column.button('Press me!') 
# Or even better, call Streamlit functions inside a "with" block: 
with right_column: 
  chosen = st.radio( 
    'Sorting hat', 
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")) 
  st.write(f"You are in {chosen} house!")


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
 # connect to snowflake 
 #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]) 
 #my_cur = my_cnx.cursor() 
 # run a snowflake query and put it all in a var called my_catalog 
 #my_cur.execute("select color_or_style from catalog_for_website") 
 #my_catalog = my_cur.fetchall() 
 # put the dafta into a dataframe 
 #df = pandas.DataFrame(my_catalog) 
 # temp write the dataframe to the page so I Can see what I am working with 
 # streamlit.write(df) 
 # put the first column into a list 
 #color_list = df[0].values.tolist() 
 # print(color_list) 
 # Let's put a pick list here so they can pick the color 
 #option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list)) 
 # We'll build the image caption now, since we can 
 #product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!' 
 # use the option selected to go back and get all the info from the database 
 #my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';") 
 #df2 = my_cur.fetchone() 
 #streamlit.image( 
 #df2[0], 
 #width=400, 
 #caption= product_caption 
 #) 
 #streamlit.write('Price: ', df2[1]) 
 #streamlit.write('Sizes Available: ',df2[2]) 
 #streamlit.write(df2[3])