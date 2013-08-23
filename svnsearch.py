#!/usr/bin/python
import argparse

from svncrawler import SvnCrawler

def handleArgs():
    argparser = argparse.ArgumentParser(description="Search a Subversion repository over HTTP.")
    argparser.add_argument('baseUrl',metavar='baseUrl', help='Fully qualified URL of root')
    argparser.add_argument('fileFilter', metavar='fileFilter', help='Comma-delimited list of file extensions to search')
    argparser.add_argument('searchString',metavar='searchString', help='String for which to search')
    argparser.add_argument('-start', metavar='link', help='link on the page at baseUrl from which to start the search', dest='start')
    argparser.add_argument('-u', metavar='username', help='SVN Username', dest='user')
    argparser.add_argument('-p', metavar='password',help='SVN Password', dest='password')
    return argparser.parse_args()



args = handleArgs()
suffixes = args.fileFilter.split(',')

crawler = SvnCrawler(args.user,args.password, suffixes, args.searchString)
crawler.followLink(args.baseUrl, args.start)
