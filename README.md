# Excel_to_SQL
This program convert excel files to SQL queries and add them into to sql ready file called 'script.sql'. It automaticaly check the value of each column and based on their format, decide the type of the column.
## As Notice
The type assignment is not always accurate, therefore, make sure to check the 'script.sql' to confirm that everything is correct.

## prerequisite
The prerequisite programs are:
```
phyton3
pip3
numpy
panda
xlrd
```
To run it:
```diff
python3 Converter.py
```
## Important
The excel file should be in the same directory as the ```Converter.py``` script.

## Contributing
Every contribution is welcome.
