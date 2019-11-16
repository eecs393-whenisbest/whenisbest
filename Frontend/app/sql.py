import sqlalchemy
import pymysql
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username="root",
        password="Shannara",
        database="whenisbest",
        query={
            'unix_socket': '/cloudsql/{}'.format("whenisbest:us-central1:wib")
        }
    ),
    pool_size = 5,
    max_overflow = 2,
    pool_timeout = 30,
    pool_recycle = 1800,
    # ... Specify additional properties here.
    # ...
)

def createQuery(query, values):
    try:
        with db.connect() as cursor:
            cursor.execute(query,values)
    except Exception as e:
        return Response(
            status = 500,
            response = "error logged"
        )

def getQueryResults(query, values):
    with db.connect() as cursor:
        return cursor.execute(query, values).fetchall()
