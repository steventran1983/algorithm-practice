class URl_Shortener:
  url2id = {}
  id = 1000
  urltoid64 = {}
  
  def shorten_url(self,url):
    if url in self.url2id:
      return "shorten_url/" + str(self.url2id[url])
    else:
      self.url2id[url] = self.encode(self.id)
      short_url = self.encode(self.id)
      self.id += 1
    return "shorten_url/" + str(short_url)
    
  def encode(self,id):
    chars = "0123456789abcdefABCDEEF"
    base = len(chars)
    ret=[]
    
    while id > 0: 
      val = id % base
      ret.append(chars[val])
      id = id // base
      
    return "".join(ret)
  
  def url_convert(self,short_url):
    id = short_url.split("/")[1]
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
print(shortener.url_convert("shorten_url/bE1"))
print(shortener.url_convert("shorten_url/eE1"))

