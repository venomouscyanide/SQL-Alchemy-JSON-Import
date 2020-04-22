from sqlalchemy import Column, Integer, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NewsArticle(Base):
    __tablename__ = 'news_article'
    id = Column(Integer, primary_key=True)
    author = Column(JSON)
    body = Column(Text)
    categories = Column(JSON)
    characters_count = Column(Integer)
    entities = Column(JSON)
    hashtags = Column(Text)
    keywords = Column(Text)
    language = Column(Text)
    links = Column(JSON)
    media = Column(JSON)
    paragraphs_count = Column(Integer)
    published_at = Column(DateTime)
    sentences_count = Column(Integer)
    sentiment = Column(JSON)
    social_shares_count = Column(JSON)
    source = Column(JSON)
    summary = Column(JSON)
    title = Column(Text)
    words_count = Column(Integer)

    def __repr__(self):
        return "<News Articles(id='{}', body='{}', author={})>" \
            .format(self.id, self.body, self.author)
