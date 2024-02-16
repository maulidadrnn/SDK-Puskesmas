import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('DINAS KESEHATAN KOTA SEMARANG')

st.info('Form Tenaga Kesehatan Teladan Puskesmas Kota Semarang')

icon_size = 20

st_button('google forms', 'https://forms.gle/sfZT9CVAU3p1HqM76', 'Form Tenaga Kesehatan Perawat', icon_size)
st_button('google forms', 'https://forms.gle/ToDgL54TH1DTuLfi6', 'Form Tenaga Kesehatan Bidan', icon_size)
st_button('google forms', 'https://forms.gle/WBWbyBiy6d3ChhDW7', 'Form Tenaga Kesehatan Dokter', icon_size)
st_button('google forms', 'https://forms.gle/LanZSeHxJFgXEHYw9', 'Form Tenaga Kesehatan ATLM', icon_size)
st_button('google forms', 'https://forms.gle/Rh9sP8SXncEVZCBJA', 'Form Tenaga Kesehatan Nutrisionis', icon_size)
st_button('google forms', 'https://forms.gle/ADXhMyMYVYEa3Vqe9', 'Form Tenaga Kesehatan Farmasi - TTK', icon_size)
st_button('google forms', 'https://forms.gle/YC74GULEYvojusBn9', 'Form Tenaga Kesehatan Farmasi - Apoteker', icon_size)
