from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# your code here
engine = create_engine("sqlite:///./admin.db")
# session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_session(session=None):
    if not session:
        return Session(bind=engine, autocommit=False)
    return session
