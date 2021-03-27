import os
import gzip
import json
import argparse
from datetime import datetime
import pathlib


def extract_tweet_text(tweets_file, tweets_output):
    """
    :param tweets_file: Input directory of tweets
    :param tweets_output: Where to output the JSON file.
    :return: Outputs a JSON file with only the text of the tweets.
    """
    # Get current time to see how long processing takes.
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Starting text extraction from tweets, at: {current_time}')

    # Scan the directory and make a list of all files.
    for file in os.scandir(tweets_file):
        tweet_texts = []

        # To see which file the program is currently processing, for debugging purposes (corruption or bad formatting).
        print(file.path)

        # Files are in gz format.
        with gzip.open(file.path, "r") as f:

            # Since every JSON object is on a different line, the normal json.loads method will not work.
            # Every line has to be read separately and then json.loads has to be run on it to read the tweet.
            json_file_path = f'{tweets_output}/tweetstext.json'
            for obj in f:
                tweet = json.loads(obj)

                # Tweets seems to have a different format, because of this an elif statement is added.
                # In older tweets, the lang tag is inside of the user tag. In the newer ones, it is outside of the
                # user tag.
                if 'lang' in tweet['user'] and tweet['user']['lang'] == 'nl':
                    tweet_texts.append(tweet['text'])
                elif 'lang' in tweet and tweet['lang'] == 'nl':
                    tweet_texts.append(tweet['text'])

            tweets_json = open(json_file_path, 'w')
            json.dump(tweet_texts, tweets_json, indent=4)
            tweets_json.close()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Done with text extraction from tweets, at: {current_time}')


def main():
    parser = argparse.ArgumentParser(description="Extracts data from tweets and outputs it in a given spot.")
    parser.add_argument("input_path", type=str, help="The path to the directory with the tweets. Only directories work with .gz format.")
    parser.add_argument("output_path", type=str, help="The path to where the output should be placed. Put none if output into program folder.")
    args = parser.parse_args()
    dir_input = f'{args.input_path}'
    dir_output = args.output_path

    if args.output == 'none':
        dir_output = pathlib.Path().absolute()

    extract_tweet_text(dir_input, dir_output)


if __name__ == '__main__':
    main()
