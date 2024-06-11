import streamlit as st
from PIL import Image
import sqlite3
from back import main_db


def input():
    
    image = Image.open('./data/photo-165790233.jpg')
    st.header('Climbing Gym')
    st.title('Climbing Competition')
    st.divider()
    st.image(image, use_column_width=True)
    st.divider()
    st.subheader('player profile')
    st.text('プロフィールを入力してください')

    ss = st.session_state
    
    if 'n' not in ss:
        ss.n = None
    ss.temp_n = ss.n 
    def update_n():
        ss.n = ss.temp_n 
    name = st.text_input(
        'ニックネーム', 
        max_chars=20, 
        placeholder='入力してください', 
        key='temp_n',
        on_change=update_n
        )
    
    if 'c' not in ss:
        ss.c = None
    ss.temp_c = ss.c 
    def update_c():
        ss.c = ss.temp_c  
    category_list = [
        'キッズ', 
        'ファン', 
        'ミドル男子', 
        'ミドル女子', 
        'オープン'
        ]
    category = st.selectbox(
        '出場カテゴリー', 
        category_list, 
        index=None,
        placeholder='選択してください', 
        key='temp_c',
        on_change=update_c
        ) 
    
    if 't' not in ss:
        ss.t = None
    ss.temp_t = ss.t 
    def update_t():
        ss.t = ss.temp_t  
    time_category_list = [
        '9:20～', 
        '11:00～', 
        '13:00～'
        ]
    time_category = st.selectbox(
        '出場時間帯', 
        time_category_list, 
        index=None,
        placeholder='選択してください', 
        key='temp_t',
        on_change=update_t
        )
    
    st.divider()
    st.subheader('result')
    st.text('完登した課題を選択してください')

    if 'r' not in ss:
        ss.r = []
    ss.temp_r = ss.r
    def update_r():
        ss.r = ss.temp_r 
    num_list = []
    for i in range(1, 37):
        num_list.append(str(i))   
    result = st.multiselect(
        '完登した課題の番号', 
        num_list,
        placeholder='選択してください', 
        key='temp_r',
        on_change=update_r
        )
    join_list = ','.join(result)
    
    st.divider()                           
    con_btn = st.button('確認')
    
    @st.experimental_dialog("最終確認")
    def sub_btn():
        st.warning("入力内容を確認してください")
        st.write(f'・ニックネーム  \n{name}')
        st.write(f'・出場カテゴリー  \n{category}')
        st.write(f'・出場時間帯  \n{time_category}')
        st.write(f'・完登した課題の番号  \n{join_list}')
        con = st.button("送信")
        if con:
            main_db.replace_table(
                name, 
                category, 
                time_category, 
                join_list
                )
            st.success("送信が完了しました")
    
    if con_btn: 
        if name and category and time_category and result:           
            main_db.create_table()
            sub_btn()             
        else:
            st.warning("入力されていない項目があります")
      
                
if __name__ == '__main__':
	input()
