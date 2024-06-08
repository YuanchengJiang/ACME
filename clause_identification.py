
def clauses_identifying(questdb_api, postgres_api):
    '''
    This file includes the shared clauses between QuestDB and Postgres.
    Note that it does not contain all the shared clauses for these two databases.
    For comprehensive details, refer to the official documentation of QuestDB and Postgres.
    '''

    shared_clauses = ["COUNT_DISTINCT","AVG","MAX","MIN","SUM","CROSS_JOIN","INNER_JOIN","CASE", "OVER_PARTITION", "IN", "BETWEEN", "COUNT","ORDER BY","UNION","EXCEPT","INTERSECT","JOIN","TABLE_SUBQUERY", "PARTITION", "SAMPLE", "OVER_PARTITION_ORDER", "DATEADD"]

    return shared_clauses
