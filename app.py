import streamlit as st

string = "Largest"
st.set_page_config(page_title=string)

st.write("""
# Largest Among Three Numbers App

This app gives largest number from three numbers
(It returns -1 if there is not a single largest number available.)
""")

st.header('User Input Parameters')

def user_input_features():
    n1 = st.number_input("Enter Number-1")
    n2 = st.number_input("Enter Number-2")
    n3 = st.number_input("Enter Number-3")
    return n1, n2, n3

n1, n2, n3 = user_input_features()

def largestNumber(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    return -1

if st.button('Calculate'):
    st.write(largestNumber(n1, n2, n3))