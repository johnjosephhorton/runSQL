#!/usr/bin/env python

import argparse
import os
import psycopg2
from settings import connection_string
import csv 

__author__ = 'John J. Horton'
__copyright__ = 'Copyright (C) 2012  John Joseph Horton'
__license__ = 'All rights reserved'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'


def create_connection(connection_string): 
    '''
    Creat a connection to the databse defined in connection_string. 
    '''
    return psycopg2.connect(connection_string)
  
def execute_query(cursor, sql_stmt, silent, csv_file_name): 
    '''
    Execute the passed SQL statement with the passed cursor.
    If silent is not None, then output is written to stdout, otherwise it is surpressed. 
    Output can also be written to a passed CSV file. 
    '''
    cursor.execute(sql_stmt)
    header = [y[0].replace(" ","") for y in cursor.description]
    d = dict(zip(range(len(header)),header))
    if csv_file_name: 
        output = csv.writer(open(csv_file_name, 'w'), delimiter=",")
        output.writerow(header)
    if not silent: 
        print(header) 
    if csv_file_name or (not silent): 
        for line in cursor.fetchall():
            if csv_file_name: 
                output.writerow(line)
            if not silent: 
                print(line)
    return True 
   
def main():
    parser = argparse.ArgumentParser(
        description="Run a SQL file and write output to stdout.")
    parser.add_argument("--sqlfile", "-f", help="SQL file to execute")
    parser.add_argument("--csv", "-c", help="write to passed CSV file")
    parser.add_argument("--query", "-q", help="Query to execute")
    parser.add_argument("--silent", "-s", default = False, action = "store_true", help="Run query silently")
    args = parser.parse_args()
    
    conn = create_connection(connection_string)
    cursor = conn.cursor()

    if args.sqlfile: 
        with open(args.sqlfile, "r") as f: 
            script = ''.join(f.readlines())
            f.close() 

    if args.query: 
        script = args.query 

    execute_query(cursor, script, args.silent, args.csv)
  
if __name__ == '__main__':
    main()
