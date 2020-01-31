[![Build Status](https://travis-ci.com/matt-palmer-tfs/rpg_namer.svg?branch=master)](https://travis-ci.com/matt-palmer-tfs/rpg_namer)
![types](https://img.shields.io/badge/python-3.6%2B-yellow)

# rpg namer
This is a simple package to generate random item names from pre-compiled lists of descriptions and item types

Some example names generated:

```
Lusca's Fists
Consternation Dress
The Intimidation Footpads
Kushtaka's Spangenhelm
The Actual Nasal Helmet
Yuki-Onna's Greaves
Footguards of the Edged Antaeus
Trepidity Warboots of the Svartálfar
Possible Anklet
Horrible Trousers
Tanktop of the Shikoku
Legwraps of the Dismay Familiar Spirit
Suit of the Real Suangi
Devilish Gloves of the Heikegani
```

## Installing and Usage

### Installation
```
python -m pip install rpg_namer
```

### Upgrading
```
python -m pip install rpg_namer --upgrade
```


### Basic Usage

```python
from rpg_namer import RPGItems


gen = RPGItems()
print(gen.random_item())

# Output: Horrible Trousers

```

Additional overrides for the items, adjectives and target nouns are provided as keywords, and support list 
functionality:

```python
from rpg_namer import RPGItems

override_items = ['buckler']
override_nouns = ['serpent']
override_adjectives = ['flaming']


gen = RPGItems(items=override_items,
               adjectives=override_adjectives,
               nouns=override_nouns)
print(gen.random_item())

# Output: Flaming Buckler of the Serpent
```

Generation of the item name will be done using random selections from each list and fabricated by static item formats 
in the class. For additional suggested formats, or new word lists, please add a suggestion via branch/PR.

### Word List generation

Generation of the word lists or stripping tools from source can eb found under the examples directory which includes 
some base code for generating word lists and formatting python lists for consumption. This can assit in new list 
generation. 
