import argparse
import json
import re


def extract_words(input_file):
    """
    :param input_file: Tweet file to read, with every tweet text in a list format.
    :return: Prints out the frequency of the 4 keywords.
    """
    # Extract from JSON
    with open(input_file, 'r') as json_file:
        convert_file = json.load(json_file)

    # 4 keywords it will look for
    kado_total = 0
    cad_total = 0
    buro_total = 0
    bureau_total = 0

    # Look for the patterns per found tweet text
    for tweet in convert_file:
        kado_pattern = re.compile('[Kk][Aa][Dd][Oo]')
        cadeau_pattern = re.compile('[Cc][Aa][Dd][Ee][Aa][Uu]')
        buro_pattern = re.compile('[Bb][Uu][Rr][Oo]')
        bureau_pattern = re.compile('[Bb][Uu][Rr][Ee][Aa][Uu]')

        # Add the frequency to the keywords.
        if kado_pattern.search(tweet):
            kado_total += 1
        if cadeau_pattern.search(tweet):
            cad_total += 1
        if buro_pattern.search(tweet):
            buro_total += 1
        if bureau_pattern.search(tweet):
            bureau_total += 1

    # Print out the results
    print(f'Total Tweets: {len(convert_file)}')
    print(f'Kado: {kado_total}')
    print(f'Cadeau: {cad_total}')
    print(f'Buro: {buro_total}')
    print(f'Bureau: {bureau_total}')


def main():
    parser = argparse.ArgumentParser(description="Extracts specific word pattern from tweets. This case: Cadeau, Kado"
                                                 ", Bureau and Buro")
    parser.add_argument("input", type=str, help="The path to the input file in .json format.")
    args = parser.parse_args()
    dir_input = f'{args.input}'

    extract_words(dir_input)


if __name__ == '__main__':
    main()
