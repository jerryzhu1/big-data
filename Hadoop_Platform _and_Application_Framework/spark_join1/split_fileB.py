#! /usr/bin/env python
def split_fileB(line):
    key_value, count_string = line.split(',')
    date, word = key_value.split(' ')
    return (word, date + ' ' + count_string)

