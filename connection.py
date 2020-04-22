from sqlalchemy import create_engine, MetaData, Table, Integer, Column, JSON, Text, DateTime
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()


def connect(db_URI: str) -> Session:
    database_URI = db_URI
    created_engine = create_engine(database_URI, echo=True)
    session = sessionmaker(bind=created_engine, )
    session = session()
    _create_table_if_needed('news_article', created_engine)
    return session


def _create_table_if_needed(table_name: str, created_engine: Engine) -> None:
    metadata = MetaData()
    new_table = Table(table_name, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('author', JSON),
                      Column('body', Text),
                      Column('categories', JSON),
                      Column('characters_count', Integer),
                      Column('entities', JSON),
                      Column('hashtags', Text),
                      Column('keywords', Text),
                      Column('language', Text),
                      Column('links', JSON),
                      Column('media', JSON),
                      Column('paragraphs_count', Integer),
                      Column('published_at', DateTime),
                      Column('sentences_count', Integer),
                      Column('sentiment', JSON),
                      Column('social_shares_count', JSON),
                      Column('source', JSON),
                      Column('summary', JSON),
                      Column('title', Text),
                      Column('words_count', Integer),
                      mysql_charset='utf8')
    metadata.create_all(created_engine, tables=[new_table], checkfirst=True)
