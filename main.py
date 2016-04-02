import sys

import pandas as pd

from blessings import Terminal

def move_down(n):
    for i in range(n):
        print(t.move_down)

def print_category_list():
    for i in range(len(params['categories'])):
        print(t.bold(str(i)) + '\t' + params['categories'][i])

def get_category_choice():
    user_input = input('Enter category: ')

    if user_input.lower() == 'q':
        save_output()
        sys.exit()
    elif user_input.isnumeric() and int(user_input) < len(params['categories']):
        return params['categories'][int(user_input)]
    else:
        # New category name
        params['categories'].append(user_input)
        return user_input

def save_output():
    df.to_csv('output.csv', index=False)


# Read config file
params = {}
exec(open(sys.argv[1]).read(), params)
del params['__builtins__']
print(params)

cat_col = params['category_column']

# Load data
exec("df = " + params['input_code'])

t = Terminal()

print(t.enter_fullscreen)

df[cat_col] = None

cols_to_ignore = [cat_col]

# Iterate through data, and ask for category
for i, s in df.iterrows():
    for item in s.index:
        if item not in cols_to_ignore:
            print(t.bold("%s:" % item) + " %s" % (s[item]))

    move_down(1)
    print_category_list()

    move_down(1)
    cat = get_category_choice()
    df.ix[i, cat_col] = cat

    print(t.clear)

    save_output()
