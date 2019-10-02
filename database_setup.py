from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="category")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'          : self.name,
            'id'            : self.id
        }

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(250))
    picture = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref=backref('items', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="items")



engine = create_engine('sqlite:///catalog.db')
blueprint = make_github_blueprint(
    client_id="my-key-here",
    client_secret="my-secret-here",
)
app.register_blueprint(blueprint, url_prefix="/login")

Base.metadata.create_all(engine)
