from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class SubversionHtmlParser(HTMLParser):
  """
  Subclass of HTMLParser that will extract all hyperlinks from an HTML page. This class will filter out SVN specific links
  such as "http://subversion.apache.org" and back links (like "../")
  """
  def __init__(self):
    HTMLParser.__init__(self)
    self.linkList = []
  def handle_starttag(self, tag, attrs):
    for attr in attrs:
      if attr[0] == 'href':
        if not (attr[1] == '../' or attr[1] == 'http://subversion.apache.org/'):
          self.linkList.append(attr[1])


