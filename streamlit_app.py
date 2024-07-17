import streamlit as st
from PIL import Image
import input, admin


def main():
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

if __name__ == '__main__':
	main()

