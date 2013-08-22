from svnparser import SubversionHtmlParser
import urllib2, base64


class SvnCrawler:
  def __init__(self, user, password, fileSuffixList, searchString):
    self.counter = 0
    if user <> None and password <> None:
      self.encodedAuth = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    else:
      self.encodedAuth = None
    self.searchString = searchString
    self.fileSuffixList = fileSuffixList

  def fetchPage(self, baseUrl):
    request = urllib2.Request(baseUrl)
    if self.encodedAuth <> None:
      request.add_header("Authorization", "Basic %s" % self.encodedAuth)
    result = urllib2.urlopen(request)
    return result

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
        

  def followLink(self, url):
    if self.counter % 100 == 0:
      print self.counter
    result = self.fetchPage(url)
    parser = SubversionHtmlParser()
    parser.feed(result.read())
    for link in parser.linkList:
      if not (link == '../' or link == 'http://subversion.apache.org/' or link == 'branches/' or link == 'tags/' or link.startswith('.')) :
        self.evaluateLink(url+link)