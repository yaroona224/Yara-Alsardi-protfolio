from sqlalchemy import create_engine,text
engine = create_engine("mysql+pymysql://admin:1234admin@sdatabase-1.cbuy2wsyk2rn.eu-north-1.rds.amazonaws.com/project?charset=utf8mb4")

with engine.connect() as conn:
  result = conn.execute(text("select * from trial"))
  print(result.all())