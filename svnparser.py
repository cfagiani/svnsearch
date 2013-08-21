from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class SubversionHtmlParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.linkList = []
  def handle_starttag(self, tag, attrs):
    for attr in attrs:
      if attr[0] == 'href':
        self.linkList.append(attr[1])


