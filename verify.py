from driver import *

postgres_query = """
SELECT NULL IN (NULL)
"""

questdb_query = """
SELECT CASE WHEN NULL IN (NULL) THEN NULL ELSE NULL IN (NULL) END
"""
# SELECT CASE WHEN NULL IN (1,NULL) THEN NULL ELSE NULL IN (1,NULL) END
# SELECT CASE WHEN False IN (False) THEN False ELSE False IN (False) END
# SELECT CASE WHEN NULL IN (NULL) THEN NULL ELSE NULL IN (NULL) END
# SELECT CASE WHEN NULL IN (NULL) THEN NULL ELSE NULL IN (NULL) END

postgres_api = PostgresConnector()
questdb_api = QuestDBConnector()

postgres_result = postgres_api.query(query=postgres_query)
questdb_result = questdb_api.query(query=questdb_query)

print("postgres_result:")
print(postgres_result)
print("questdb_result:")
print(questdb_result)
