#!/usr/bin/env python3
#version: 0.2
# -*- coding: utf-8 -*-
#Author: YeonJoo Oh

# imported modules
import nltk 
from nltk.tokenize import sent_tokenize  
import sys
import re




#######################################################################
def read_file(file_name):

	with open(file_name) as f:

		token_string = f.read()
		tokenized = sent_tokenize(token_string)
	return tokenized
########################################################################

def to_lowercase(words):
	new_words = []
	for word in words:
		new_word = word.lower()
		new_words.append(new_word)
	return new_words

########################################################################
def remove_punctuation(words):

	new_words = []
	for word in words:
		new_word = re.sub(r'[^\w\s]', '', word)
		if new_word != '':
			new_words.append(new_word)
	return new_words
								
########################################################################
def main():
	
	result = remove_punctuation(to_lowercase(read_file(sys.argv[1])))
	filename = sys.argv[1]
	output_path = './'
	outputfile_name = output_path + filename + '.b.txt'
	output = open(outputfile_name, 'w')
	for x in result:
		output.write(str(x))
	

if __name__ == "__main__":
	main()

