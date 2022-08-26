import streamlit as st

#Sets df size with width 1000 and height 300, but width has a limited range
st.dataframe(df, 1000, 300) 

st.dataframe(df, use_container_width=True) 

st.write(df, use_container_width=True)
