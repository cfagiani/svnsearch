#!/usr/bin/python
import sys

from svncrawler import SvnCrawler

def checkargs():
  if len(sys.argv) !=6:
    print 'Bad command.\nUsage: svnsearch <baseurl> <username> <password> <fileFilter> <searchString>'
    sys.exit(1)



checkargs()
suffixes = sys.argv[4].split(',')

crawler = SvnCrawler(sys.argv[2],sys.argv[3], suffixes, sys.argv[5])
crawler.followLink(sys.argv[1])
