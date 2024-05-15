from driver import *

questdb_query = """
SELECT COUNT(*) FROM (SELECT * FROM zghekjhf) AS T1 WHERE True AND CASE WHEN T1.c0 IS NULL THEN NULL::SYMBOL WHEN NULL IN ('0') THEN NULL::SYMBOL ELSE T1.c0 NOT IN (0) END AND True AND True SAMPLE BY 1d
"""
# select sample_by_d_result from (SELECT count(*) as sample_by_d_result, extract(day from c2) as h from hgjopowp group by h)

#


#SELECT count(*), (c2/3600 as hour) from zjldmnec SAMPLE BY 1d
#SELECT CAST(c2 AS INT)/3600 AS h from dxcuijjy

postgres_query = """
select case when null IS null then null when null in ('0', null) then null else null in ('0', null) end
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