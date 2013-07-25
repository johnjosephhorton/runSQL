runSQL 
------

This is utility to run SQL scripts on a database. 


Installlation
-------------

Get the code: 

    git clone git@github.com:johnjosephhorton/runSQL.git

Modify the connection string in `settings.py` to match the database you want to connect to: 

	cd runSQL
	emacs settings.py
	<made changes> 
	
Run the installation: 

	sudo python setup.py install 

Use
---

```
usage: runSQL [-h] [--sqlfile SQLFILE] [--csv CSV] [--query QUERY]
                 [--silent]

Run a SQL file and write output to stdout.

optional arguments:
  -h, --help            show this help message and exit
  --sqlfile SQLFILE, -f SQLFILE
                        SQL file to execute
  --csv CSV, -c CSV     write to passed CSV file
  --query QUERY, -q QUERY
                        Query to execute
  --silent, -s          Run query silently
```

Examples 
--------

Suppose you have a query file called `test.sql`: 

    echo -e "select count(*) from agg.b_assignment" > test.sql 

You can simply run 

	runSQL --sqlfile test.sql 
	
	['count']
	(2585753L,)

You can just run it by passing the query as a string, using the ``--query`` option.: 

    runSQL --query "select count(*) from agg.b_assignment"
	
	['count']
	(2585753L,)
	
You can write to a CSV file by passing the parameter `--csv` with a filename.

    runSQL --query "select count(*) from agg.b_assignment" --csv test.csv 
	
	['count']
	(2585753L,)

	cat test.csv 
	count
	2585753L
```

By default, the program fetches all the rows, but if you just want to get the side-effects (i.e., it runs the script but doesn't fetch the results), you can run: 


	runSQL -sqlfile test.sql --silent 



