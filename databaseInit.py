pw="Turnbull01!"


# Zoltan Biro  
# 101220698

import psycopg

with psycopg.connect(f"dbname=COMP3005a3q1 user=postgres password={pw}") as conn:
    with conn.cursor() as cur:
            cur.execute("""
CREATE TABLE students(
    student_id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL Unique,
    enrollment_date Date)
""")
            
            cur.execute("""
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
""")
            conn.commit()