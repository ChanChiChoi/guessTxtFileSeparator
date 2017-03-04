# guessTxtFileSeparator
to guess the simple separator of each txt file.\n
the setps as follow:\n
  1 - read the first 10 lines
  2 - filter the empty lines
  3 - replace the '[0-9a-zA-Z\_]' into '@'
  4 - Count the number of occurrences of characters
  5 - preserve the ascii char which value between [1,126], and discard the '@' char
  6 - get the minimum subset of char in step 5 result
  7 - use re.findall('[{}]+'.format(subsetChars)) to get the candidate separator
  8 - verify whether the separator is valid 
