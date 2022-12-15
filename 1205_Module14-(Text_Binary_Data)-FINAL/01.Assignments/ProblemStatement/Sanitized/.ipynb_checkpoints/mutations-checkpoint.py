#!/usr/bin/env python



import io
import os
import sys

import pandas as pd
import numpy as np


#1

# Method:
class Cart():
    def __init__(self):
        self.cart = []
        self.total = 0

    def add_to_cart(self, item):
        self.cart.append(item)
        self.total += item.price

'''
Answers
-------
Inheritance: No, Class cart does not inherit from other class
Polymorphism: No, there is not two or more function with the same name
Object-Oriented programming: Yes, it is a class..
Top-down design: ???
Functional programming: No, Object-oriented programming combines logic with data into objects, while functional programming keeps logic and data separate.
'''

def g(): pass
print(type(g))

# as g is declared as function (that is doing nothing), the type of the g would be function of course

def g(): pass
print(type(g()))

# the difference here is that we call the function before we asked for its type. This call
# return nothing and thus the type of the returned element is None


#2

#a
def count_lower_vowels(phrase):
    v = {}
    for letter in phrase:
        if letter.isupper():
            continue
        if not letter.isalpha():
            continue
        if letter in v:
            v[letter] += 1
        else:
            v[letter] = 1
    return v

example_text = "I love coding in python!"
print(count_lower_vowels(example_text))


#b
import pandas

# creating a data frame from scratch - list of lists

data = [
         [101, 'AC'],
         [102, 'Heat Pump'],
         [103, 'Air Con'],
         [104, 'Air Conditioning'],
         [105, 'Fan'],
         [106, 'None'],
         [107, 'EvapCooler'],
         [108, None],
         [109, 'EC'],
         [110, 'Evaporative Cooler'],
         [111, 'geothermal'],
         [112, 8],
         [113, 'Air Con']
       ]

# create a data frame with column names - list of lists

col_names = ['Cust_Number', 'Cooling_System']
df = pandas.DataFrame(data, columns=col_names)

map_air = {1:['Air Conditioning','Air Con','AC'],2:['Heat Pump','HP'],3:['Evaporative Cooler','EvapCooler','EC'],4:['Fan']}

new_values = []
for index,row in df.iterrows():
    value = row['Cooling_System']
    z = 0;
    for key in map_air:
        if value in map_air[key]:
            z = key
            break
    new_values.append(z)

df['cooling_type'] = z
df_filtered = df[df['cooling_type']>0]

#c
import pandas

# creating a data frame from scratch - list of lists

data = [ ['marco', 165, 'blue', 'FL'],
         ['jeb', 35, 'red', 'FL'],
         ['chris', 0, 'white', 'NY'],
         ['donald', 1543, 'white', 'NY'],
         ['ted', 559, 'blue', 'NY'],
         ['john', 161, 'red', 'OH']
       ]

# create a data frame with column names - list of lists

col_names = ['name', 'delegates', 'color', 'state']
df = pandas.DataFrame(data, columns=col_names)
print(df.groupby(['state'])['state'].count())

#d



data = ({"Initial": 1000}, {"Jan 2018":1200},{"Feb 2018":1400},{"Mar 2018":700},{"Apr 2018":800},{"May 2018":500})

def bitcoin_invest(monthly_data):
    # add code here
    ret = []
    growth = []
    gain = []
    periods = []
    for item in monthly_data:
        for key in item:
            balance = item[key]
            if key == 'Initial':
                start_balance = balance
        periods.append(key)
        gain.append(balance - start_balance)
        growth.append(balance/start_balance)
        ret.append(balance/start_balance - 1)
    data = zip(periods,gain,growth,ret)
    col_names = ['period', 'gain', 'growth', 'return']
    df = pandas.DataFrame(data, columns=col_names)
    return df

df = bitcoin_invest(data)
print(df.head())


#4
def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('#')]
    return pd.read_csv(io.StringIO(''.join(lines)),dtype={'CHROM': str, 'POS': str, 'ID': str, 'REF': str, 'ALT': str,'QUAL': str, 'FILTER': str, 'INFO': str},sep='\t').rename(columns={'#CHROM': 'CHROM'})

def parse_info(line):
    info = {}
    attributes = line.split(';')
    for attr in attributes:
        if ':' in attr and '=' in attr:
            name = attr.split('=')[0]
            value = attr.split('=')[1]
        elif ':' in attr and not '=' in attr:
            name = attr.split(':')[0]
            value = attr.split(':')[1]
        elif '=' in attr and not ':' in attr:
            name = attr.split('=')[0]
            value = attr.split('=')[1]
        info[name] = value
    return info

df = read_vcf('clinvar_final.txt')

a = []
b = []
c = []
for index, row in df.iterrows():
    value = parse_info(row['INFO'])
    try:
        x = value['GENEINFO']
        y = value['CLNSIG']
        z = value['CLNDN']
    except Exception as e:
        x='Not_given'
        y='-'
        z='-'
    a.append(x)
    b.append(y)
    c.append(z)


df['GENE'] = a
df['SIGNIFICANCE'] = b
df['DISEASE'] = c

df['MutationPos'] = df['CHROM'] + df['POS']
df['MutationValue'] = df['REF'] + df['ALT']
df.drop(['CHROM','POS','REF','ALT','FILTER','QUAL','INFO'],axis=1,inplace=True)

df_mutations = df[df['GENE'] !='Not_given']
df_final = df_mutations[:100]
print(df_final['SIGNIFICANCE'].value_counts())



