import sqlite3
import hashlib

def make_hashes(password):
    
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_pass):
    
    if make_hashes(password) == hashed_pass:
        return hashed_pass
    else:
        return False


def create_table():
    
    DATABASE = './data/admin.db'
    con = sqlite3.connect(DATABASE)
    c = con.cursor()
    
    create_table = 'CREATE TABLE IF NOT EXISTS admin(username TEXT PRIMARY KEY, password TEXT)'
    c.execute(create_table)
    
    user_default = 'hirano'
    pass_default = 'agtm'
    pass_hashes = make_hashes(pass_default)
    admin_table = 'REPLACE INTO admin(username, password) VALUES (?, ?)'
    c.execute(admin_table, (user_default, pass_hashes))  
    con.commit()
      
    c.close()
    con.close()


def login_user(username, password):
    
    DATABASE = './data/admin.db'
    con = sqlite3.connect(DATABASE)
    c = con.cursor()
    
    login_user = 'SELECT * FROM admin WHERE username = ? AND password = ?'
    c.execute(login_user, (username, password))
    data = c.fetchall()
    return data

    c.close()
    con.close()

if __name__ == '__main__':
    make_hashes()
    check_hashes()
    create_table()
    login_user()
    
  



