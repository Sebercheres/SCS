from tkinter import Y
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


image = Image.open('logo.png')
st.image(image, use_column_width=True)

st.write("""
    # Statistic Counter For Student

    ***
""")

data = st.text_input("Insert the Data!", value="80, 90, 100, 95")
data = data.split(',')
st.write("Input values with commas Ex: 80, 90, 100, 95")

df = pd.DataFrame(data, columns=["Bob"])
try:
  df['Bob'] = df['Bob'].astype('double')
except ValueError:
  st.error('please enter input')


st.write("""***""")


fig, ax = plt.subplots()
ax.hist(df.Bob, bins=20)
st.write("""### Histogram""")
st.pyplot(fig)

st.write("""### Bar Chart""")
st.bar_chart(df.Bob)


fig = go.Figure(
    go.Pie(
    labels = df.Bob.value_counts().index,
    values = df.Bob.value_counts(),
    hoverinfo = "label+percent",
    textinfo = "value"
))

st.write("""### Pie Chart""")
st.plotly_chart(fig)

result_df = pd.DataFrame()
result_df['result'] = ['mean', 'median', 'max', 'min', 'variance', 'std', 'range']

result_df['number'] = [df.Bob.mean(), df.Bob.median(), df.Bob.max(),df.Bob.min(), df.Bob.var(), df.Bob.std(), df.Bob.max()-df.Bob.min()]

st.write("""### Describe""")
result_df.set_index('result')
result_df

mode = pd.DataFrame(df.Bob.mode(), columns=['mode'])
st.write(df.mode())

