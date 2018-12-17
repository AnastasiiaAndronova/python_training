import datetime
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

from pony.orm import *

class ORMFicture:
    db=Database()

    class ORMGroup(db.Entity):
        _table_= 'grouplist'
        id= PrimaryKey(int,column='group_id')
        name=Optional(str,column='group_name')
        header=Optional(str,column='group_header')
        footer=Optional(str,column='group_Footer')
    class ORMContact(db.Entity):
        _table_= 'adressbook'
        id= PrimaryKey(int,column='id')
        firstname=Optional(str,column='firstname')
        lastname=Optional(str,column='lastname')
        deprecated=Optional(datetime,column='deprecated')

    def __init__(self,host,name,user,password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()

    def get_group_list(self):
        list(select(g for g in ORMFicture.ORMGroup))