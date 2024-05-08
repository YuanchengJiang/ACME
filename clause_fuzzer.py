


def clauses_fuzzing(questdb_api, postgres_api):
    shared_clauses = ["COUNT_DISTINCT","AVG","MAX","MIN","SUM","CROSS_JOIN","INNER_JOIN","CASE", "OVER_PARTITION", "IN", "BETWEEN", "COUNT","ORDER BY","UNION","EXCEPT","INTERSECT","JOIN","TABLE_SUBQUERY"]
    reserved_clauses = ["COUNT_DISTINCT"]
    # clause_targets = [
    #     "CASE_WHEN",
    #     "DISTINCT",
    #     "WINDOW_ORDER_BY",
    #     "TUMBLE",
    #     "WITH",
    #     "CAST_TIMESTAMP",
    #     "IN_SUBQUERY",
    #     "INSERT_SUBQUERY",
    #     "INDEX_QUERY",
    #     "WINDOW_FUNCTION",
    #     "DIVERSE_DATA",
    #     "BETWEEN_CLAUSE",
    #     "ORDER_BY_CLAUSE",
    #     "INTERSECT",
    #     "EXCEPT",
    #     "GROUP_BY_CLAUSE",
    #     "HAVING_CLAUSE",
    #     "DISTINCT"
    #     ]

    return shared_clauses, reserved_clauses