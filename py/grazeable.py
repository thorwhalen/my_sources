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
        
        
