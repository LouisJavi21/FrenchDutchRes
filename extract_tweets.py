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

        # To see which file it is at, for debugging purposes (corruption or bad formatting).
        print(file.path)

        # Files are in gz format.
        with gzip.open(file.path, "r") as f:
            total_tweets = []

            # Since every JSON object is on a different line, this piece of code will load every line
            # and put it in a list.
            for obj in f:
                tweet_dict = json.loads(obj)
                total_tweets.append(tweet_dict)

            for tweet in total_tweets:
                tweet_texts.append(tweet['text'])

            json_file_path = f'{tweets_output}/tweetstext.json'
            with open(json_file_path, 'w', encoding='utf-8') as tweets_json:
                json.dump(tweet_texts, tweets_json, indent=4)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Done with text extraction from tweets, at: {current_time}')


def main():
    parser = argparse.ArgumentParser(description="Extracts data from tweets and outputs it in a given spot.")
    parser.add_argument("input", type=str, help="The path to the directory with the tweets. Only directories work with .gz format.")
    parser.add_argument("output", type=str, help="The path to where the output should be placed. Put none if output into program folder.")
    args = parser.parse_args()
    dir_input = f'{args.input}'
    dir_output = args.output

    if args.output == 'none':
        dir_output = pathlib.Path().absolute()

    extract_tweet_text(dir_input, dir_output)


if __name__ == '__main__':
    main()
