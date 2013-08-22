from svnparser import SubversionHtmlParser
import urllib2, base64, traceback


class SvnCrawler:
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
    self.counter = self.counter+1
    for suffix in self.fileSuffixList:
      if link.lower().endswith(suffix):
        self.searchData(link)
      elif link.endswith("/"):
         self.followLink(link)
   
  def searchData(self,link):
    content = self.fetchPage(link).read()
    if self.searchString in content:
      print "FOUND %s in %s" % (self.searchString, link)
        

  def followLink(self, url, startLink = None):
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
          if not (link == '../' or link == 'http://subversion.apache.org/' or link == 'branches/' or link == 'tags/' or link.startswith('.')) :
            if not self.foundStart and startLink == link:
              self.foundStart = True
              print "Starting from %s" % (url + link)
            if self.foundStart:
              self.evaluateLink(url+link)
      except Exception:
        print "Could not parse %s" % (url)
        traceback.print_exc()