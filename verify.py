from driver import *

questdb_only = False

questdb_query = """
select * from test2 latest on c2 partition by c1
"""

postgres_query = """
select distinct * from (select t1.c0,t1.c1,t1.c2 from test as t1 join (select distinct
max(c0) over(partition by c1) as c0, c1 from test) as t2 on t1.c0=t2.c0 and t1.c1=t2.c1) latest_on
"""

postgres_api = PostgresConnector()
questdb_api = QuestDBConnector()

if "SELECT " in postgres_query:
    if not questdb_only:
        postgres_result = postgres_api.query(query=postgres_query)
    questdb_result = questdb_api.query(query=questdb_query)
else:
    if not questdb_only:
        postgres_result = postgres_api.write_query(query=postgres_query)
    questdb_result = questdb_api.write_query(query=questdb_query)

if not questdb_only:
    print("postgres_result:")
    print(postgres_result)
# print(len(postgres_result))
print("questdb_result:")
print(questdb_result)
# print(len(questdb_result))
