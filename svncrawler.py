from svnparser import SubversionHtmlParser
import urllib2, base64, traceback


class SvnCrawler:
  """
  This class crawls and searches a subversion repository that is hosted via HTTP. 
  For all files that end in the fileSuffixList, the content will be downloaded and searched for
  the searchString. The searchString is an exact lexical match.
  """
  def __init__(self, user, password, fileSuffixList, searchString):
    self.counter = 0
    if user <> None and password <> None:
      self.encodedAuth = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    else:
      self.encodedAuth = None
    self.searchString = searchString
    self.fileSuffixList = fileSuffixList
    self.foundStart = True

  def fetchPage(self, baseUrl):
    """
    Fetch a single page and return a file-like object representing the resource at baseUrl. 
    If the class was initialized with a username/password, an Authorization
    header will be added to the request. 
    """
    request = urllib2.Request(baseUrl)
    if self.encodedAuth <> None:
      request.add_header("Authorization", "Basic %s" % self.encodedAuth)
    try:
      result = urllib2.urlopen(request)
      return result
    except Exception:
      print "Could not load %s" % (baseUrl)
      return None

  def evaluateLink(self,link):
    """
    Check if a link represents a file with a name that ends in one of the suffixes for which it is looking
    and search it for the search string.
    Both the searchString and suffixList are set upon instance initialization. 
    The file is only downloaded if its name ends with a target suffix.
    """
    self.counter = self.counter+1
    for suffix in self.fileSuffixList:
      if link.lower().endswith(suffix):
        self.searchData(link)
      elif link.endswith("/"):
         self.followLink(link)
   
  def searchData(self,link):
    """
    fetch the page from the link passed in, read it as text and check if it contains the searchString
    """
    content = self.fetchPage(link).read()
    if self.searchString in content:
      print "FOUND %s in %s" % (self.searchString, link)
        

  def followLink(self, url, startLink = None):
    """
    Loads the url passed in and treats it as an HTML page. Extract all hyperlinks from the page and 
    follow them. If a startLink is passed in, the links extracted from the page will be ignored until the startLink is found.
    This method currently ignores the standard subversion  links for branches, tags as well as 
    hidden directories (those that start with ".")
    """
    if self.counter % 100 == 0:
      print "%d: %s" % (self.counter, url)
    if startLink is not None:
        self.foundStart = False
    result = self.fetchPage(url)
    if result <> None:
      parser = SubversionHtmlParser()
      try:
        parser.feed(result.read())
        for link in parser.linkList:
          if not (link == 'branches/' or link == 'tags/' or link.startswith('.')) :
            if not self.foundStart and startLink == link:
              self.foundStart = True
              print "Starting from %s" % (url + link)
            if self.foundStart:
              self.evaluateLink(url+link)
      except Exception:
        print "Could not parse %s" % (url)
        traceback.print_exc()