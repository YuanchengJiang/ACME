def clauses_fuzzing(questdb_api, postgres_api):
    shared_clauses = ["COUNT_DISTINCT","AVG","MAX","MIN","SUM","CROSS_JOIN","INNER_JOIN","CASE", "OVER_PARTITION", "IN", "BETWEEN", "COUNT","ORDER BY","UNION","EXCEPT","INTERSECT","JOIN","TABLE_SUBQUERY", "PARTITION", "SAMPLE", "OVER_PARTITION_ORDER"]

    return shared_clauses