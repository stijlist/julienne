julienne
=====

a python lib for slicing n' dicing html tables 
----

### Examples: 

Julienne a table:
    
    # table can be a beautifulsoup tag or a block of text
    julienned = Julienne(table)
    
validate a table: 

    # checks that table has same number of ths as tds in each column
    julienned.validate() # => true of false

enumerate columns: 
    
    julienned.columns() # => ['Player','Points', 'Rebounds', 'Assists']

enumerate rows: TODO: return dicts instead of lists
    
    julienned.rows() # => ['Kevin Durant', 'LeBron James']

select rows and columns from the table: 

    julienned.select(columns=['Points'], rows=['Kevin Durant']) # => 32.0

convert to csv:

    julienned.csv() # => Player,Points,Rebounds,Assists
                    # ...Kevin Durant,32.0,7.4,5.5
                    # ...LeBron James,27.4,6.3,6.9



