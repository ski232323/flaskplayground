from tinydb import TinyDB, Query, where
import unidecode

db = TinyDB('db.json')
DATA = Query()

el=db.get(DATA.name=='admin')
el.doc_id()
