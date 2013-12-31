#!/bin/bash

for i in 0 1 2 3 5;
do 
	java -jar sqlScriptRunner.jar $i | grep -v "rows returned." | grep -v "get connection" | grep -v "done" |grep -v "sql:"; 
done
