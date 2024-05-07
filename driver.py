import psycopg2

class PostgresConnector:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres", user = "postgres", password = "12344321", host = "127.0.0.1", port = "5432")

    def reconnect(self):
        self.conn = psycopg2.connect(database="postgres", user = "postgres", password = "12344321", host = "127.0.0.1", port = "5432")

    def query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows

    def write_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        return None

class QuestDBConnector:
    conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'
    def __init__(self):
        pass

    def query(self, query):
        with psycopg2.connect(self.conn_str) as connection:
            with connection.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
                return results

    # write query needs commits, but no need results
    # QuestDB seems no difference on write query
    def write_query(self, query):
        with psycopg2.connect(self.conn_str) as connection:
            with connection.cursor() as cur:
                cur.execute(query)
                return None