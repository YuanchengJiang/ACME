from driver import *

# SELECT COUNT(T1.c2) FROM wnkvvhhg AS T1 WHERE CASE WHEN T1.c0 IS NULL THEN NULL::BOOLEAN ELSE T1.c0 NOT IN (0,1,2,NULL) END
questdb_query = """
SELECT CASE WHEN T1.c0 IN (0,1,2,NULL) THEN NULL::BOOLEAN ELSE T1.c0 IN (0,1,2,NULL) END FROM wnkvvhhg AS T1
"""
# select sample_by_d_result from (SELECT count(*) as sample_by_d_result, extract(day from c2) as h from hgjopowp group by h)

#
#SELECT count(*), (c2/3600 as hour) from zjldmnec SAMPLE BY 1d
#SELECT CAST(c2 AS INT)/3600 AS h from dxcuijjy
# SELECT sample_by_result from ( SELECT COUNT(*) AS sample_by_result, EXTRACT(DAY FROM T1.c2) AS d FROM mjypnsxk AS T1 WHERE True AND T1.c0 IN (0,NULL) AND True AND True GROUP BY d )
# SELECT '2' IN (NULL,'2',NULL)

# SELECT COUNT(T1.c2) FROM wnkvvhhg AS T1 WHERE T1.c0 NOT IN (0,1,2,NULL)
postgres_query = """
SELECT T1.c0 IN (0,1,2,NULL) FROM wnkvvhhg AS T1
"""
# select case when '0' IS null then null when null in ('0', null) then null else '0' in ('0', null) end
# SELECT count(*) from zyzsbegn where 1 AND (CASE WHEN NULL IN (NULL) THEN NULL ELSE NULL IN (NULL) END)
# SELECT CASE WHEN NULL IN (NULL) THEN NULL ELSE NULL IN (NULL) END
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