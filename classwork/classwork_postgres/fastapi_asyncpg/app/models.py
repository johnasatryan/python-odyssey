# Create User model with pydantic
CREATE_USERS_TABLE_QUERY = """
  CREATE TABLE IF NOT EXISTS users(
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) CHECK(char_length(username)>=3 AND char_length(username)<=50) NOT NULL,
  password VARCHAR(50) CHECK(char_length(password)>=6) NOT NULL,
  email TEXT NOT NULL UNIQUE,
  image_url TEXT,
  full_name TEXT,
  is_admin BOOLEAN DEFAULT FALSE
  )
"""

INSERT_USER_QUERY="""
INSERT INTO users(
username,
password,
email,
image_url,
full_name,
is_admin) VALUES($1,$2,$3,$4,$5,$6) 
RETURNING id,username,password,email,image_url,full_name,is_admin
"""

GET_USER_BY_ID="""
SELECT * FROM users WHERE id = $1
""" 

GET_USER_BY_EMAIL="""
SELECT * FROM users WHERE email = $1
""" 
