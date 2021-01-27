from graze import Graze

g = Graze()

def add_url_attr(url):
    def add_url(obj):
        obj.url = url
        return obj
    return add_url


class GrazeAndPrep:
    # TODO: url repeated twice. descriptor or decorator to get rid of this?
    @add_url_attr('https://unicode.org/emoji/charts/full-emoji-list.html')
    def emojis_01(self):
        html = g['https://unicode.org/emoji/charts/full-emoji-list.html'] 
        html = html.decode()
        t = pd.read_html(html)[0]
        tt = t.droplevel([0, 1], axis=1)
        return tt.iloc[list(map(str.isnumeric, tt['№']))]
        
    @add_url_attr('https://raw.githubusercontent.com/thorwhalen/my_sources/master/github_emojis.json')
    def emojis_02(self):
        from functools import cached_property
        import json

        from py2store import KvReader
        from graze import graze

        class EmojiUrls(KvReader):
            """A store of emoji urls. Will automatically download and cache emoji (name, url) map to a local file when first used."""
            data_source_url = 'https://raw.githubusercontent.com/thorwhalen/my_sources/master/github_emojis.json'

            @cached_property
            def data(self):
                b = graze(self.data_source_url)  # does the same thing as Graze()[url]
                return json.loads(b.decode())

            def __iter__(self):
                yield from self.data

            def __getitem__(self, k):
                return self.data[k]
            
        return EmojiUrls()
        
        
