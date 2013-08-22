svnsearch
=========

##Utility to search a SVN repository that is exposed over http


This simple script will search the files in an HTTP-hosted subversion repository for an arbitrary search string.

The search can be restricted to a comma-delimited set of file extensions and can be set up to start from a specific repository link.

##Usage
		python svnsearch.py <baseurl> <username> <password> <fileFilter> <searchString> [startLink]
where:
**baseurl** is the starting url for the repository
**username** is the username to use for the http auth challenge
**password** is the password to use for the http auth challenge
**fileFilter** is a comma-delimited list of file extensions to check (i.e. *java,xml* )
**startLink**  (optional) is the link from which to start the search (as it appear in the html on the page located at baseUrl)


##TODO:
- Clean up command line arguments
- Make auth optional
- Multithread