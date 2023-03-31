import pandas as pd
from sqlalchemy import create_engine
import pandas as pd
db_connection_str ='mysql+pymysql://star:pavithra555@localhost/myhcl'
db_connection = create_engine(db_connection_str)
df=pd.read_excel("",sheet_name='Sheet1')
try:
    df.to_sql(name='mytable',con=db_connection)
except Exception as e:
    print(e)