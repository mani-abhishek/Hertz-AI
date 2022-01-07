from sqlalchemy import Table,Column
# from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import String,Integer
from config.db import meta

users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('bookName',String(255)),
    Column('pageNumber',Integer),
    Column('topicName',String(255)),
    Column('chapterName',String(255)),
    Column('text1',String(255)),
)