<h1>French Dutch Research Project</h1>
A Research to see the use of specific French words compared to their Dutch counterparts by using tweets.


<h2>How does it work</h2>

*extract_tweets.py*

This program extracts tweets, which are in .out.gz file format. The file itself must be formatted in .json per line.
Since every tweet is a separate json object, the program reads every line as a separate object.

Before the text is extracted, the program will check the *lang* key and see if the value is *nl*, if it is not then it will be ignored and not extracted.
From every object the value of the key *text* is extracted and added to a new json object, where all the texts of the tweets are collected.

*extract_words.py*

This program is used to find the specific given keywords: *Kado*, *Cadeau*, *Buro*, *Bureau*.
Every tweet is checked if it contains one of these words and if it does, it counted.

At the end the program will return the total checked tweets and the frequency of every word.


<h2>How to run</h2>
The two programs, *extract_tweets.py* and *extract_words.py*, are run seperately.

*extract_tweets.py*

`python3 extract_tweets.py input_path_to_folder path_of_where_to_put_output`

Example:

`python3 extract_tweets.py me/Documents/Tweets/2012Tweets/ me/Documents/Tweets`

The program will create an output file called: *tweetstext.json*


*extract_words.py*

`python3 extract_words.py path_to_input_file`

Example

`python3 extract_words.py me/Documents/tweets.json`

The output will be like this:


`Total Tweets: 29225
Kado: 7
Cadeau: 51
Buro: 5
Bureau: 37
`

<h2>Data</h2>
The used *processed* data is in the *tweets* folder. It contains the extracted and processed tweets of 2012, 2019 and 2020. I have only used the data of 2012 and 2020.

The data was acquired by downloading it from the karora database of the RUG univerisity using *scp*.
Used commands are:


For 2012
`
scp -r sxxxxxx@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2012/12 /home/user/Documents/Tweets/2020
`
For 2020
`
scp -r sxxxxxx@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2012/12 /home/user/Documents/Tweets/2020
`


<h2>Versions</h2>

Since only builtin libraries of Python are used, the versions of those libraries match the version of Python.

Python: 3.8.5

Linux Ubuntu: 5.8.0-44-generic
