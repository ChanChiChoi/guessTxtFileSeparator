#! /opt/python2
# -*- coding: utf-8 -*-
'''
  guess the separator, the file should not be less than 2 column
  example: 1 - aaa,bbb
           2 - aaa bbb
           3 - aaa\tbbb
           4 - aaa----bbb
           5 - aaa # bbb
  action: 1 - the file should more than 10 lines
          2 - the sep should occur in each line, and has the same times
'''
import os
import re
import sys
import os.path as osp
from collections import *
gReNormalChar = re.compile('[\w@]')
gReIp = re.compile('@+\.@+\.@+\.@+')

def isValidSep(checkLines1,sep):

    splitLinesLen = map(lambda line: len(line.split(sep)), checkLines1)
    ans = [ a-b != 0 for a,b in zip(splitLinesLen,splitLinesLen[2:]+splitLinesLen[:2]) ]
    return not any(ans)
    
def handle_onefile(file):

    with open(file,'rb') as fr:
        '''1 - read the first 10 lines'''
        checkLines = [ next(fr).strip() for _ in range(10) ]
        checkLines = filter(lambda line: line, checkLines)
        '''replace the [\w_] into @ '''
        checkLines1 = [gReNormalChar.sub('@',line)  for line in checkLines]
        checkLines1 = [gReIp.sub('@',line) for line in checkLines1]
        '''stat the @ and other char  '''
        checkLines2 = [Counter(line) for line in checkLines1]
        '''remain the sep metachar,which value should between [0,126]  '''
        checkLines3 = [filter(lambda key:ord(key) > 0 and ord(key) <126 and key != '@' ,cnt) for cnt in checkLines2]
        '''get the minimum subsetr of metachars in checkLines2 '''
        minNumMetaChar = min([len(cnt) for cnt in checkLines3])
        minLencheckLine = filter(lambda cnt: len(cnt) == minNumMetaChar, checkLines3)[0]
        #matrix = [ [cnt[metachar] for metachar in maxLencheckLine ] for cnt in checkLines2]
        '''get the longest combination of the sep metachar '''
        #ans = [[a - b for a,b in zip(matrix[0],line)] for line in matrix]
        #metaCharsFlag = [ not any([line[ind]!=0 for line in ans ])for ind,char in enumerate(maxLencheckLine)]
        #metaChars = [b for a,b in zip(metaCharsFlag,maxLencheckLine) if a]
        lReSep = re.compile('[{}]+'.format(''.join(minLencheckLine)))
        sep = list(set(lReSep.findall(checkLines[0])))
        '''verify whether the sep chars is valid separator'''
        sep = filter(lambda sepT: isValidSep(checkLines1,sepT), sep)
        print '{} choices, the first separator word is:[{}],sec[]'.format(len(sep),list(sep)[0])

if __name__ == '__main__':

   file = sys.argv[1]
   handle_onefile(file)  


