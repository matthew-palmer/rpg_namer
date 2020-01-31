from bs4 import BeautifulSoup
import requests


"""
Brute Force extractor for lists on Wikipedia for naming extraction.

Logical flow may not work if lists are nested in a non-expected way (e.g. ul>li>ul)

This also is assuming that post-processing of each list will be done, as some values will be extracted incorrectly.
"""


def extract(url, outfile, letter_filter=None, other_filters=None):
    titles = list()

    filter_attrs = {
        'class': None
    }

    resp = requests.get(url).content
    bs = BeautifulSoup(resp, "html.parser")
    uls = bs.findAll("ul")
    for ul in uls:
        for li in ul.findAll('li'):
            for a in li.findAll('a', attrs=filter_attrs):
                title = str(a.get('title')).lower()
                entry = a.get('title')
                add_to = True
                if letter_filter:
                    if not title.startswith(letter_filter):
                        add_to = False
                if other_filters:
                    if other_filters in title:
                        add_to = False
                if not letter_filter and not other_filters:
                    titles.append(a.get('title'))
                elif add_to:
                    titles.append(entry)

    for item in titles:
        try:
            if '(' in item or ')' in item:
                titles.remove(item)
        except TypeError as err:
            print("%s on item %s" % (err, item))
    with open(outfile, 'w+') as file:
        for item in titles:
            file.write("%s\n" % item)


def legendaries():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in letters:
        base_url = "https://en.wikipedia.org/wiki/List_of_legendary_creatures_(%s)" % char
        file = "%s.txt" % char
        filter = "%s" % char.lower()
        other = "myth"
        extract(base_url, file, filter, other)


if __name__ == "__main__":
    _url = input("Enter target url: ")
    _outfile = input("Enter output file:")
    _letter_filter = input("Enter letter filter (if any): ") or None
    _other_filter = input("Enter any other filter to exclude: ") or None
    extract(_url, _outfile, _letter_filter, _other_filter)


# Example information:
# url = "https://en.wikipedia.org/wiki/List_of_legendary_creatures_(A)"
# outfile = "legendary_creatures_a.txt"
# letter_filter = "a"
# other_filter = "myth"