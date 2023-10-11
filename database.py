from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Check this url minute 10:00
# URL_DATABASE = 'postgresql://postgres://mvbsyumc:7y_gPbYHZ-5XMX0qr1whmJzKqOwqyNWF@bubble.db.elephantsql.com/mvbsyumc'
URL_DATABASE = 'postgresql://mvbsyumc:7y_gPbYHZ-5XMX0qr1whmJzKqOwqyNWF@bubble.db.elephantsql.com/mvbsyumc'
# URL_DATABASE = 'postgresql://postgres:123456@localhost:5432/QuizApplicationYT'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

