##1. First of all open the pyspark shell and load the datasets you created for the previous assignment from HDFS:

> fileA = sc.textFile("input/join1_FileA.txt")

##2. Make sure the file content is correct:

> fileA.collect()

should return:

Out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']

##3. Then load the second dataset:

fileB = sc.textFile("input/join1_FileB.txt")

same verification:

> fileB.collect()

Out[29]: 
[u'Jan-01 able,5',
 u'Feb-02 about,3',
 u'Mar-03 about,8 ',
 u'Apr-04 able,13',
 u'Feb-22 actor,3',
 u'Feb-23 burger,5',
 u'Mar-08 burger,2',
 u'Dec-15 able,100']

##4. Create mapper for fileA: create a map function for fileA that takes a line, splits it on the comma and turns the count to an integer.

##5. Test function by defining a test variable:

> test_line = "able,991"

make sure that:

> split_fileA(test_line)

returns:

Out[]: ('able', 991)

##6. roceed on running the map transformation to the fileA RDD:

> fileA_data = fileA.map(split_fileA)

result:

fileA_data.collect()
Out[]: [(u'able', 991), (u'about', 11), (u'burger', 15), (u'actor', 22)]
Make sure that the key of each pair is a string (i.e. is delimited by ' ' ) and the value is an integer.

##7. Create mapper for fileB: the mapper for fileB is more complex because we need to extract

> fileB_data = fileB.map(split_fileB)

gathering the output back to the pyspark Driver console:

>fileB_data.collect()

result:

Out[]: 
[(u'able', u'Jan-01 5'),
 (u'about', u'Feb-02 3'),
 (u'about', u'Mar-03 8 '),
 (u'able', u'Apr-04 13'),
 (u'actor', u'Feb-22 3'),
 (u'burger', u'Feb-23 5'),
 (u'burger', u'Mar-08 2'),
 (u'able', u'Dec-15 100')]

##8. Run join

The goal is to join the two datasets using the words as keys and print for each word the wordcount for a specific date and then the total output from A.
Basically for each word in fileB, we would like to print the date and count from fileB but also the total count from fileA.
Spark implements the join transformation that given a RDD of (K, V) pairs to be joined with another RDD of (K, W) pairs, returns a dataset that contains (K, (V, W)) pairs.

> fileB_joined_fileA = fileB_data.join(fileA_data)

Verify the result:

> fileB_joined_fileA.collect()fileB_joined_fileA.collect()

##9. Output:

[(u'able', (u'Jan-01 5', 991)),
 (u'able', (u'Apr-04 13', 991)),
 (u'able', (u'Dec-15 100', 991)),
 (u'burger', (u'Feb-23 5', 15)),
 (u'burger', (u'Mar-08 2', 15)),
 (u'about', (u'Feb-02 3', 11)),
 (u'about', (u'Mar-03 8', 11)),
 (u'actor', (u'Feb-22 3', 22))]










