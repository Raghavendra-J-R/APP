import sqlite3


conn=sqlite3.connect('employee.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
    emp_ssn INTEGER PRIMARY KEY,
    emp_name TEXT,
    emp_category TEXT,
    gross_sal REAL,
    basic_sal REAL
)              
               ''')

employees_data = [
    (123456789, 'John Doe', 'Category A', 5000.00, 4000.00),
    (987654321, 'Jane Smith', 'Category B', 6000.00, 4500.00),
    (555555555, 'Alice Johnson', 'Category C', 7000.00, 5000.00)
]

cursor.executemany('''INSERT INTO Employee (emp_ssn, emp_name, emp_category, gross_sal, basic_sal)
                    VALUES (?, ?, ?, ?, ?)''', employees_data)
conn.commit()

def compute_net_salary(category, gross_sal, basic_sal):
    if category == 'Category A':
        tax_deducted = 0.30 * gross_sal
        dearness_allowance = 0.80 * basic_sal
    elif category == 'Category B':
        tax_deducted = 0.20 * gross_sal
        dearness_allowance = 0.50 * basic_sal
    elif category == 'Category C':
        tax_deducted = 0.10 * gross_sal
        dearness_allowance = 0.30 * basic_sal
    else:
        return None  # Invalid category
    
    net_salary = gross_sal - tax_deducted + dearness_allowance
    return net_salary

cursor.execute('''SELECT emp_name, emp_category, gross_sal, basic_sal FROM Employee''')
for row in cursor.fetchall():
    name, category, gross_sal, basic_sal = row
    net_salary = compute_net_salary(category, gross_sal, basic_sal)
    if net_salary is not None:
        print(f"{name}: Net Salary = ${net_salary:.2f}")

# Close the cursor and connection
cursor.close()
conn.close()