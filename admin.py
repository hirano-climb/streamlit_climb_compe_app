import streamlit as st
from back import main_db, admin_db, excel


def admin(): 
    
    ss = st.session_state
    
    if 'push_2' not in ss:
        ss.push_2 = 0
    
    username = st.sidebar.text_input(
        'ユーザー名', 
        placeholder='入力してください', 
        key='username'
    )
    password = st.sidebar.text_input(
        'パスワード', 
        placeholder='入力してください', 
        type='password',
        key='password'
    )

    submit_btn = st.sidebar.button('ログイン')
    if submit_btn:      
        admin_db.create_table()            
        hashed_pass = admin_db.make_hashes(password)
        result = admin_db.login_user(username, admin_db.check_hashes(password, hashed_pass))       
            
        if result:            
            ss.push_2 = 1        
            st.sidebar.success('ログインしました')          
        else:
            st.sidebar.warning('入力に誤りがあります')
		
    if ss.push_2 == 1:      
        st.subheader('administrator form')

        admin_list = [
            '入力データを確認します', 
            '入力データを全て削除します', 
            '入力データをexcelファイルで出力します'
            ]
        admin_category = st.selectbox(
            '管理項目', 
            admin_list, 
            index = None, 
            placeholder='選択してください', 
            key='admin_category'
            )
        
        @st.experimental_dialog("最終確認")
        def ap_btn():
            st.warning("本当に入力データを全て削除しますか？")
            ap = st.button("承認")
            if ap:
                main_db.delete_table()
                st.success('入力データの削除が完了しました')
                
        @st.experimental_dialog("リザルトのダウンロード")
        def dw_btn():
            excel.download_excel()      
                
        exe_btn = st.button('実行')
        if exe_btn:            
            if admin_category == '入力データを確認します':
                main_db.check_table()
                st.success('入力データの確認が完了しました')                             
            elif admin_category == '入力データを全て削除します':
                ap_btn()
            elif admin_category == '入力データをexcelファイルで出力します':
                excel.create_excel()
                dw_btn()
            else:
                st.warning("入力されていない項目があります")
        
                    
if __name__ == '__main__':
	admin()
