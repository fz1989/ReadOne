from django.db import models

# Create your models here.

from simplemediawiki import MediaWiki

wiki = MediaWiki('http://zh.wikipedia.org/w/api.php')

def searchItem(name):
    try:
        content = wiki.call({'format':'json', 'action':'query', 'prop':'revisions', 'rvprop':'content', 'rvlimit':1, 'titles':name})
    
        pageid = content['query']['pages'].keys()[0]
        page = content['query']['pages'][pageid]['revisions'][0]['*']
        return page
    except:
        return None

