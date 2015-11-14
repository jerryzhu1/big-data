
##1.Make mapper and reducer executable

> chmod +x wordcount_mapper.py

> chmod +x wordcount_reducer.py

##2.See what directory you are in

> pwd

##3.Create some data:

> echo "A long time ago in a galaxy far far away" > /home/cloudera/testfile1

> echo "Another episode of Star Wars" > /home/cloudera/testfile2

##4.Create a directory on the HDFS file system (if already exists that’s OK):

> hdfs dfs -mkdir /user/cloudera/input

##5.Copy the files from local filesystem to the HDFS filesystem:

> hdfs dfs -put /home/cloudera/testfile1 /user/cloudera/input

> hdfs dfs -put /home/cloudera/testfile2 /user/cloudera/input

##6.Check files on HDFS

> hdfs dfs -ls /user/cloudera/input

##7.Run the Hadoop WordCount example with the input and output specified.

Note that your file paths may differ. The ‘\’ just means the command continues on next line.

> hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar   -input /user/cloudera/input   -output /user/cloudera/output_new   -mapper /home/cloudera/wordcount_mapper.py   -reducer /home/cloudera/wordcount_reducer.py

##8.Hadoop prints out a whole lot of logging or error information. If it runs you will see something like the following on the screen scroll by:

....

INFO mapreduce.Job: map 0% reduce 0%

INFO mapreduce.Job: map 67% reduce 0%

INFO mapreduce.Job: map 100% reduce 0%

INFO mapreduce.Job: map 100% reduce 100%

INFO mapreduce.Job: Job job_1442937183788_0003 completed successfully

...

##9.Check the output file to see the results:

> hdfs dfs -cat /user/cloudera/output_new/part-r-00000

##10.View the output directory:

> hdfs dfs -ls /user/cloudera/output_new

##11. Look at the files there and check out the contents, e.g.:

hdfs dfs -cat /user/cloudera/output_new/part-r-00000

##12. Streaming options:

Try: hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar --help

or see hadoop.apache.org/docs/r1.2.1/

##13. Get the output file from this run:

> hdfs dfs -getmerge /user/cloudera/output_new_0/* wordcount_num0_output.txt
