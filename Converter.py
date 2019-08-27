import pandas as pd
import numpy
import os 
from dateutil.parser import parse

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


# Get the current directory and add the name of the excel file to open.

dir_path = os.path.dirname(os.path.realpath(__file__))
to_open = input("Enter the name of the file you would like to open?\n")
dir_path += f'/{to_open}.xls'

# Read Excel file.
data = pd.read_excel (dir_path) 
df = pd.DataFrame(data)

# Create Tables.

table_crea = []
for ind, col  in enumerate(df.columns):
    if (type(df[col].loc[1]) == str) and (is_date(str(df[col].loc[1])) == False):
        inp = input(f"{col} is it null or not? Type 'N' for null or 'P' for not null \n")
        if inp.lower() == 'n':
            table_crea.append(f"{col} VARCHAR2(20) NULL")
        else:
            table_crea.append(f"{col} VARCHAR2(20) NOT NULL")
    elif (type(df[col].loc[1]) == str) and (is_date(str(df[col].loc[1])) == True):
        inp = input(f"{col} is it null or not? Type 'N' for null or 'P' for not null \n")
        if inp.lower() == 'n':
            table_crea.append(f"{col} DATE NULL")
        else:
            table_crea.append(f"{col} DATE NOT NULL")
    elif (type(df[col].loc[1]) == int) and (is_date(str(df[col].loc[1])) == False):
        inp = input(f"{col} is it null or not? Type 'N' for null or 'P' for not null \n")
        if inp.lower() == 'n':
            table_crea.append(f"{col} NUMBER(10) NULL")
        else:
            table_crea.append(f"{col} NUMBER(10) NOT NULL")
    elif (isinstance(df[col].loc[1], (float, numpy.float)) == True):
        inp = input(f"{col} is it null or not? Type 'N' for null or 'P' for not null \n")
        if inp.lower() == 'n':
            table_crea.append(f"{col} NUMBER(10) NULL")
        else:
            table_crea.append(f"{col} NUMBER(10) NOT NULL")
    elif (isinstance(df[col].loc[1], (int, numpy.integer)) == True):
        inp = input(f"{col} is it null or not? Type 'N' for null or 'P' for not null \n")
        if inp.lower() == 'n':
            table_crea.append(f"{col} NUMBER(10) NULL")
        else:
            table_crea.append(f"{col} NUMBER(10) NOT NULL")
# print(table_crea)


# Create insert queries.

length_col = len(df.columns)
insert_methods = []
for index, row in df.iterrows():
    str_query = 'INSERT INTO test_employee VALUES ( '
    for i in range(length_col):
        if (type(row[df.columns[i]]) == str) and (is_date(str(row[df.columns[i]])) == True):
            to_append = f"{row[df.columns[i]]}".strip()
            str_query += f"'{to_append}', "
        elif (type(row[df.columns[i]]) == str) and (is_date(str(row[df.columns[i]])) == False):
            to_append = f"{row[df.columns[i]]}".strip()
            str_query += f"'{to_append}', "
        elif (type(row[df.columns[i]]) == int) and (is_date(str(row[df.columns[i]])) == False):
            to_append = f"{int(row[df.columns[i]])}".strip()
            str_query += f"'{to_append}', "
        else:
            if f"{row[df.columns[i]]}".strip() == "nan":
                str_query += 'null, '

            else:
                to_append = f"{int(row[df.columns[i]])}".strip()
                str_query += f"{to_append}, "

       
    str_query = str_query[:-2]
    str_query += " );"
    insert_methods.append(str_query)
    print(str_query)


# Write to SQL file.

f = open("script.sql", "a")
f.write(f"CREATE TABLE {to_open} ( \n")
for key, table in enumerate(table_crea):
    
    f.write(table)
    f.write("\n")
    if key != (len(table_crea) -1 ):
        f.write(', ')
f.write(");")
f.write("\n\n")
for insert_method in insert_methods:
    f.write(insert_method)
    f.write("\n")
f.write("\n\n")
f.close()
