#%%
import hashlib


class Codec:

    def __init__(self):
        self.database = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shorturl = "http://tinyurl.com/" + hashlib.md5(
            longUrl.encode('utf-8')).hexdigest()
        self.database.update({shorturl: longUrl})
        return shorturl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.database[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

a = Codec()
a.encode("www.baidu.com")
# %%
