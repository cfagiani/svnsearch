svnsearch
=========

##Utility to search a SVN repository that is exposed over http


This simple script will search the files in an HTTP-hosted subversion repository for an arbitrary search string.

The search can be restricted to a comma-delimited set of file extensions and can be set up to start from a specific repository link.

##Usage
		python svnsearch.py [-h] [-start link] [-u username] [-p password] baseUrl fileFilter searchString

positional arguments:
  baseUrl       Fully qualified URL of root
  fileFilter    Comma-delimited list of file extensions to search
  searchString  String for which to search

optional arguments:
  -h, --help    show this help message and exit
  -start link   link on the page at baseUrl from which to start the search
  -u username   SVN Username
  -p password   SVN Password


##TODO:
- Multithread