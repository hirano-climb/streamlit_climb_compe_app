import streamlit as st
import sqlite3
import pandas as pd

def create_table():
    
    DATABASE = './data/profile_result.db'
    con = sqlite3.connect(DATABASE)
    c = con.cursor()
    
    create_table = 'CREATE TABLE IF NOT EXISTS profile_result(name TEXT PRIMARY KEY, category TEXT, time_category TEXT, result TEXT)'
    c.execute(create_table)
    
    c.close()
    con.close()


def replace_table(name, category, time_category, join_list):
    
    DATABASE = './data/profile_result.db'
    con = sqlite3.connect(DATABASE)
    c = con.cursor()
    
    insert_table = 'REPLACE INTO profile_result(name, category, time_category, result) VALUES (?, ?, ?, ?)'
    c.execute(insert_table, (name, category, time_category, join_list))
    con.commit()
    
    c.close()
    con.close()  


def check_table():
    
    DATABASE = './data/profile_result.db'
    con = sqlite3.connect(DATABASE)
   
    select_value_column = 'SELECT * FROM profile_result'
    df = pd.read_sql_query(select_value_column, con)
    df_1 = df.set_index('name')
    st.write(df_1)

    con.close()


def delete_table():
    
    DATABASE = './data/profile_result.db'
    con = sqlite3.connect(DATABASE)
    c = con.cursor()

    drop_table = 'DROP TABLE IF EXISTS profile_result'
    c.execute(drop_table)
    con.commit()
    
    c.close()
    con.close()

if __name__ == '__main__':
    create_table()
    replace_table()
    check_table()
    delete_table()
