# Introduction to Map/Reduce Module, Programming Assignment, Lesson 2

## Exercise in Joining data with streaming using Python code

##1. Follow the steps from the Wordcount assignment to set up the following files on Cloudera: join1_mapper.py join1_reducer.py join1_FileA.txt join1_FileB.txt

##2. Make mapper and reducer excutable

> chmod +x join1_mapper.py 

> chmod +x join1_reducer.py

##3. Set up the data in HDFS

> hdfs dfs -put /home/cloudera/join1_FileA /user/cloudera/input

> hdfs dfs -put /home/cloudera/join1_fileB /user/cloudera/input

##4. Test the program in serial execution using the following Unix utilities and piping commands:

(‘cat’ prints out the text files standard output; ‘|’ pipes the standard output to the standard input of the join_mapper program, etc.. )

>cat join1_File*.txt | join1_mapper.py | sort | join1_reducer.py

To debug programs in serial execution one should use small datasets and possibly extra print statements in the program. Debugging with map/reduce is harder but hopefully not necessary for this assignment, but see the –..debug option in the streaming command, which will help view standard input/output/error from the map/reduce functions.

##5. Run the Hadoop streaming command: 

> hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar  -input /user/cloudera/input  -output /user/cloudera/output_join  -mapper /home/cloudera/join1_mapper.py  -reducer /home/cloudera/join1_reducer.py
