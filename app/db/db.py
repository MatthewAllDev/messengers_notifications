import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import settings

engine: sqlalchemy.engine.base.Engine = sqlalchemy.create_engine(f'sqlite:///{settings.db_path}', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    phone_number: sqlalchemy.Column = sqlalchemy.Column('phone_number', sqlalchemy.String, primary_key=True)
    tg_user_id: sqlalchemy.Column = sqlalchemy.Column('tg_user_id', sqlalchemy.Integer)
    tg_name: sqlalchemy.Column = sqlalchemy.Column('tg_full_name', sqlalchemy.String)

    def __init__(self, phone_number: str, tg_user_id: int = None, tg_full_name: str = None):
        self.phone_number: str = phone_number
        self.tg_user_id: int = tg_user_id
        self.tg_name: str = tg_full_name
        Session: sqlalchemy.orm.session.sessionmaker = sessionmaker(bind=engine)
        self.session: sqlalchemy.orm.session.Session = Session()

    def __repr__(self):
        return f'<{type(self).__name__}({self.tg_name}, {self.phone_number}, {self.tg_user_id})>'

    def save(self):
        user_in_db: User = self.get()
        if user_in_db is not None:
            if not user_in_db.equal(self):
                for key, value in self.__dict__.items():
                    if key[0] != '_':
                        if value is not None:
                            setattr(user_in_db, key, value)
                self.session.add(user_in_db)
        else:
            self.session.add(self)
        self.session.commit()

    def get(self):
        return self.session.query(User).filter(User.phone_number == self.phone_number).first()

    def equal(self, sample):
        for key, value in self.__dict__.items():
            if key[0] != '_':
                if getattr(sample, key) != value:
                    return False
        return True


Base.metadata.create_all(engine)
