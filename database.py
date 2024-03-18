from sqlalchemy import create_engine,text
import os
db_connection_string=os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

with engine.connect() as conn:
  result = conn.execute(text("select * from myprojects"))
  print(result.all())
  from sqlalchemy import create_engine, text



  def load_projects_from_db():
     with engine.connect() as conn:
        result = conn.execute(text("select * from myprojects"))
        myprojects = []
        for row in result.all():
          myprojects.append(dict(row._mapping))
        return myprojects
    