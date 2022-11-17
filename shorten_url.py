class URl_Shortener:
  url2id = {}
  id = 1
  
  def shorten_url(self,url):
    if url in self.url2id:
      return "shorten_url/" + str(self.url2id[url])
    else:
      self.url2id[url] = self.id
      short_url = self.id
      self.id += 1
    return "shorten_url/" + str(short_url)
    
  def url_convert(self,short_url):
    id = short_url.split("/")[1]
    print(id)
    for key,value in self.url2id.items():
      if str(value) == str(id):
        return key

shortener = URl_Shortener()

print(shortener.shorten_url("www.goole.com"))
print(shortener.shorten_url("www.goole.com"))
print(shortener.shorten_url("www.yeahoo.com"))
print(shortener.shorten_url("www.t-mobile.com"))
print(shortener.shorten_url("www.gilab.com"))
print(shortener.shorten_url("www.gilab.com"))
print(shortener.url_convert("shorten_url/1"))

