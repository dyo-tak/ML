import streamlit as st
import base64


def  get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64_of_bin_file('photo_2023-02-04_09-22-41.jpg')

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.pinimg.com/736x/c0/33/e2/c033e2bcf11b95513f4c08dfa564fd4d.jpg");
    background-size: cover;
    background-position: center;
    # background-repeat: no-repeat;
    # background-attachment: local;

 
}}


</style>
"""


st.markdown(page_bg_img, unsafe_allow_html = True)
st.title("Edit this.")