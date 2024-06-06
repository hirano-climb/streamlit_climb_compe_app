import streamlit as st
from PIL import Image
import sqlite3
from back import main_db, admin_db, excel
import input, admin
import pandas as pd
import openpyxl as op
from io import BytesIO


image = Image.open('./data/photo-165790233.jpg')
st.set_page_config(
    page_title="climb compe result", 
    page_icon=image, 
    layout="centered", 
    initial_sidebar_state="auto"
    )

page_names = {
    "入力": input.input, 
    "管理": admin.admin
    }
pages = st.sidebar.selectbox(
    "メニュー", 
    page_names.keys()
    )
page_names[pages]()



