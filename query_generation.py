import string
import datetime
from clause_map import ClauseMapping
from random import choice, randint, random


# generating random strings for insert statements
def random_string():
    return "{}".format(''.join(choice(string.ascii_lowercase) for _ in range(randint(1,5))))

# generating random timestamps for insert statements

def random_timestamp():
    return datetime.datetime.now()

# generating random table name with 8 lowercase letters
def random_8_letters():
    return "{}".format(''.join(choice(string.ascii_lowercase) for _ in range(8)))

def valid_expression():
    valid_expressions = [
        "CAST(1 AS FLOAT)", "CAST(NULL AS FLOAT)", "CAST(0.0 AS FLOAT)", "CAST('0' AS FLOAT)", "CAST(0-0 AS FLOAT)", "CAST(CAST(NULL AS INT) AS FLOAT)", "CAST(CAST('0' AS INT) AS FLOAT)", "CAST(CAST('0' AS FLOAT) AS INT)", "~CAST(NULL AS INT)", "~CAST(0.0 AS INT)", "~NULL::INT", "CAST(NULL AS INT)&CAST(NULL AS INT)", "CAST(NULL AS INT)&(~NULL::INT)", "CAST(NULL AS INT)^CAST(NULL AS INT)", "CAST(NULL AS INT)^(~NULL::INT)", "CAST(NULL AS INT)|CAST(NULL AS INT)", "CAST(NULL AS INT)|(~NULL::INT)", "'5'<>'5'", "'123'<'456'", "CAST(CAST('123'<'456' AS INT)|(~NULL::INT) AS INT)^CAST(NULL AS INT)"
    ]
    return choice(valid_expressions)

class QueryGenerator:
    """
    this is only for SQL demonstration
    differential query generation aims to generate semantically equivalent
    but in different representations differential inputs for testing
    """

    columns = ["c0", "c1", "c2"]

    def __init__(self, shared_clauses, EVAL_CONFIG_CLAUSE_MAPPING):
        self.EVAL_CONFIG_CLAUSE_MAPPING = EVAL_CONFIG_CLAUSE_MAPPING
        self.clause_mapping = ClauseMapping()
        self.shared_clauses = shared_clauses
        self.shared_predicate_clauses = None
        self.concats = []
        if "UNION" in self.shared_clauses:
            self.concats.append("UNION")
        if "EXCEPT" in self.shared_clauses:
            self.concats.append("EXCEPT")
        if "INTERSECT" in self.shared_clauses:
            self.concats.append("INTERSECT")

    def fuzzy_exp(self):
        return choice(["NULL"])

    """
    0. predicates part
    TODO: still many interesting or complex predicates not implemented ;(
    """

    def random_int_predicates(self, column_name):
        predicates = ["True"]
        if not self.shared_predicate_clauses:
            self.shared_predicate_clauses = []
            predicate_clauses = ["IN","BETWEEN"]
            for each_clause in predicate_clauses:
                if each_clause in self.shared_clauses:
                    self.shared_predicate_clauses.append(each_clause)
        for each_shared_clause in self.shared_predicate_clauses:
            if choice([True,False]):
                if each_shared_clause=="IN":
                    in_predicates = [
                        f"{column_name} IN (0,NULL)",
                        f"{column_name} NOT IN (0,1,2,NULL)",
                        f"{column_name} NOT IN (0,NULL)",
                        f"{column_name} NOT IN (0)",
                    ]
                    predicates.append(choice(in_predicates))
                elif each_shared_clause=="IN_SUBQUERY":
                    # TODO
                    pass
        return ' AND '.join(predicates)

    def random_string_predicates(self, column_name):
        predicates = ["True"]
        if not self.shared_predicate_clauses:
            self.shared_predicate_clauses = []
            predicate_clauses = ["IN","BETWEEN"]
            for each_clause in predicate_clauses:
                if each_clause in self.shared_clauses:
                    self.shared_predicate_clauses.append(each_clause)
        for each_shared_clause in self.shared_predicate_clauses:
            if choice([True,False]):
                if each_shared_clause=="IN":
                    in_predicates = [
                        f"{column_name} IN ('0',NULL)",
                        f"{column_name} NOT IN ('0','1','2',NULL)",
                        f"{column_name} NOT IN ('0','1','2')",
                        f"{column_name} NOT IN ('0')",
                    ]
                    predicates.append(choice(in_predicates))
                elif each_shared_clause=="IN_SUBQUERY":
                    # TODO
                    pass
        return ' AND '.join(predicates)

    def random_timestamp_predicates(self, column_name):
        predicates = ["True"]
        if not self.shared_predicate_clauses:
            self.shared_predicate_clauses = []
            predicate_clauses = ["IN","BETWEEN"]
            for each_clause in predicate_clauses:
                if each_clause in self.shared_clauses:
                    self.shared_predicate_clauses.append(each_clause)
        for each_shared_clause in self.shared_predicate_clauses:
            if choice([True,False]):
                if each_shared_clause=="IN":
                    in_predicates = [
                        f"{column_name} IN ('2000-01-01T00:00:00', NULL)",
                        f"{column_name} NOT IN ('2000-01-01T00:00:00', NULL)",
                        f"{column_name} NOT IN ('2000-01-01T00:00:00', '2000-01-01T00:00:00')",
                    ]
                    predicates.append(choice(in_predicates))
                elif each_shared_clause=="IN_SUBQUERY":
                    # TODO
                    pass
                elif each_shared_clause=="BETWEEN":
                    between_predicates = [
                        f"{column_name} BETWEEN {column_name} AND NOW()",
                        f"{column_name} NOT BETWEEN {column_name} AND NULL",
                        f"{column_name} NOT BETWEEN NULL AND {column_name}",
                        f"{column_name} NOT BETWEEN NULL AND NOW()",
                    ]
                    predicates.append(choice(between_predicates))
        return ' AND '.join(predicates)

    def random_predicates_no_join(self):
        predicates = []
        predicates.append(self.random_int_predicates("c0"))
        predicates.append(self.random_string_predicates("c1"))
        predicates.append(self.random_timestamp_predicates("c2"))
        return ' AND '.join(predicates)

    def random_predicates_for_joins(self, talias=None):
        predicates = []
        predicates.append(self.random_int_predicates("c0" if talias==None else f"{choice(talias)}.c0"))
        predicates.append(self.random_string_predicates("c1" if talias==None else f"{choice(talias)}.c1"))
        predicates.append(self.random_timestamp_predicates("c2" if talias==None else f"{choice(talias)}.c2"))
        return ' AND '.join(predicates)

    """
    1. simple CREATE statement implementations
    """

    def random_create_query(self):
        random_table_name = random_8_letters()
        create_query = f"CREATE TABLE {random_table_name} (c0 INT, c1 STRING, c2 TIMESTAMP);"
        if self.EVAL_CONFIG_CLAUSE_MAPPING:
            queries = self.clause_mapping.main(create_query)
            queries[0] = queries[0].replace(';',' timestamp(c2);')
        else:
            # having an ad-hoc patch for string type
            # otherwise no comparison result
            query0 = create_query.replace('STRING','SYMBOL')
            query1 = create_query.replace('STRING','VARCHAR(32)')
            queries = [query0, query1]
        return random_table_name, queries

    def init_table(self, questdb_api, postgres_api):
        table1_name, table1_create_query = self.random_create_query()
        table2_name, table2_create_query = self.random_create_query()
        table3_name, table3_create_query = self.random_create_query()
        try:
            questdb_api.write_query(table1_create_query[0])
            questdb_api.write_query(table2_create_query[0])
            questdb_api.write_query(table3_create_query[0])
        except Exception as e:
            print("questdb init table failed!")
            print(str(e))
            exit(-1)
        try:
            postgres_api.write_query(table1_create_query[1])
            postgres_api.write_query(table2_create_query[1])
            postgres_api.write_query(table3_create_query[1])
        except Exception as e:
            print("postgres init table failed!")
            print(str(e))
            exit(-1)
        self.tables = [table1_name, table2_name, table3_name]
        print("tables init finished!")
        return self.tables, table1_create_query, table2_create_query, table3_create_query

    """
    2. INSERT statement
    """

    def random_insert_query(self, table_name):
        self.init_query()
        random_INT = randint(-1000, 1000)
        random_STRING = random_string()
        random_TIMESTAMP = random_timestamp()
        values = f"{random_INT}, '{random_STRING}', '{random_TIMESTAMP}+00'"
        insert_query = f"INSERT INTO {table_name} VALUES ({values});"
        return insert_query

    """
    3. UPDATE statement
    """

    def random_update_query(self, table_name):
        self.init_query()
        # TODO: update can be complex with JOINs, etc.
        random_INT = randint(-1000, 1000)
        random_STRING = random_string()
        random_TIMESTAMP = random_timestamp()
        updates = f"c0={random_INT},c1='{random_STRING}',c2='{random_TIMESTAMP}'"
        random_predicate = self.random_predicates_no_join()
        predicates = f"WHERE {random_predicate}"
        update_query = f"UPDATE {table_name} SET {updates} {predicates}"
        return update_query

    """
    4. SELECT statement
    """

    def random_clause_with(self):
        _with = []
        _with.append("max_int AS (SELECT max(c0) from {})".format(choice(self.tables)))
        _with.append("min_int AS (SELECT min(c0) from {})".format(choice(self.tables)))
        _with.append("max_timestamp AS (SELECT max(c2) from {})".format(choice(self.tables)))
        _with.append("min_timestamp AS (SELECT min(c2) from {})".format(choice(self.tables)))
        _with = "WITH {}".format(','.join(_with))
        return _with

    def random_aggregation(self):
        aggregation_foos = []
        if "COUNT" in self.shared_clauses:
            aggregation_foos.append("COUNT")
        if "AVG" in self.shared_clauses:
            aggregation_foos.append("AVG")
        if "MAX" in self.shared_clauses:
            aggregation_foos.append("MAX")
        if "MIN" in self.shared_clauses:
            aggregation_foos.append("MIN")
        if "SUM" in self.shared_clauses:
            aggregation_foos.append("SUM")
        if len(aggregation_foos)==0:
            print("Alert: no available aggregate function!")
            return "1"
        else:
            return f"{choice(aggregation_foos)}({choice(self.columns)})"

    def random_over_partition_aggregation(self):
        aggregation_foos = []
        if "AVG" in self.shared_clauses:
            aggregation_foos.append("AVG")
        return f"{choice(aggregation_foos)}({choice(self.columns)})"

    def random_data(self):
        _data = ["COUNT(*)", f"COUNT({valid_expression()})"]
        if "CASE" in self.shared_clauses:
            column = choice(self.columns)
            _data.append(
                f"(CASE WHEN True THEN {column} ELSE {column} END)"
                )
        if "COUNT" in self.shared_clauses:
            _data.append(f"COUNT({choice(self.columns)})")
        if "OVER_PARTITION" in self.shared_clauses:
            _over_partition_order = ""
            if "OVER_PARTITION_ORDER" in self.shared_clauses and choice([True,False]):
                _over_partition_order = f"ORDER BY {choice(self.columns)}"
            _data.append(
                f"AVG(c0) OVER(PARTITION BY {choice(self.columns)} {_over_partition_order})"
                )
        return choice(_data)

    def random_table(self):
        if "TABLE_SUBQUERY" not in self.shared_clauses:
            table = self.tables
            self.tt.append(table)
            return table
        else:
            # TODO: add predicates
            _table_subquery = f"(SELECT * FROM {choice(self.tables)})"
            return _table_subquery

    def random_clause_join(self):
        _join_tables = randint(0,2)
        _joins = ["JOIN"]
        if "CROSS_JOIN" in self.shared_clauses:
            _joins.append("CROSS JOIN")
        if "INNER_JOIN" in self.shared_clauses:
            _joins.append("INNER JOIN")
        # TODO: LEFT/RIGHT OUTER JOIN
        joins = []
        for i in range(_join_tables):
            join_clause = choice(_joins)
            join_table = choice(self.tables)
            next_join = f"{join_clause} {join_table} AS T{i+2}"
            self.tt.append(join_table)
            self.tt.append(f"T{i+2}")
            self.talias.append(f"T{i+2}")
            if join_clause!="CROSS JOIN":
                next_join += " ON "+self.random_predicates_for_joins(self.talias)
            joins.append(next_join)
        return ' '.join(joins)

    def random_predicate(self):
        return " WHERE "+self.random_predicates_for_joins()

    def random_clause_partition(self):
        _partition = ""
        return _partition

    def random_clause_window(self):
        return ""

    def random_clause_group(self):
        return ""

    def random_clause_order(self):
        return ""

    def random_clause_limit(self):
        return ""

    def random_clause_sample(self):
        if "SAMPLE" in self.shared_clauses and choice([True,False]):
            _sample = "SAMPLE BY 1d"
        else:
            _sample = ""
        return _sample

    """
    5. overall mutation
    """
    def query_mutation_add_cast(self, query):
        query = query.replace(" c0", " CAST(c0 AS STRING)", randint(0,2))
        query = query.replace(" c1", " CAST(c1 AS STRING)", randint(0,2))
        query = query.replace(" c2", " CAST(c2 AS STRING)", randint(0,2))
        return query

    """
    6. sanitize check
    to pre-check grammar issues
    """
    def select_query_sanitize_check(self, query):
        if "T1" in self.tt:
            query = query.replace(" c0 ", f" {choice(self.talias)}.c0 ")
            query = query.replace(" c1 ", f" {choice(self.talias)}.c1 ")
            query = query.replace(" c2 ", f" {choice(self.talias)}.c2 ")
            query = query.replace("(c0)", f"({choice(self.talias)}.c0)")
            query = query.replace("(c1)", f"({choice(self.talias)}.c1)")
            query = query.replace("(c2)", f"({choice(self.talias)}.c2)")
            query = query.replace(" c0)", f" {choice(self.talias)}.c0)")
            query = query.replace(" c1)", f" {choice(self.talias)}.c1)")
            query = query.replace(" c2)", f" {choice(self.talias)}.c2)")
            query = query.replace("(c0,", f"({choice(self.talias)}.c0,")
            query = query.replace("(c1,", f"({choice(self.talias)}.c1,")
            query = query.replace("(c2,", f"({choice(self.talias)}.c2,")
        return query

    def adhoc_final_query_sanitize_check(self, query):
        biased_talias = ["T1","T1","T1","T1","T1","T1","T2","T2","T3"]
        if "T1" in self.tt:
            query = query.replace(" c0 ", f" {choice(biased_talias)}.c0 ")
            query = query.replace(" c1 ", f" {choice(biased_talias)}.c1 ")
            query = query.replace(" c2 ", f" {choice(biased_talias)}.c2 ")
            query = query.replace("(c0)", f"({choice(biased_talias)}.c0)")
            query = query.replace("(c1)", f"({choice(biased_talias)}.c1)")
            query = query.replace("(c2)", f"({choice(biased_talias)}.c2)")
            query = query.replace(" c0)", f" {choice(biased_talias)}.c0)")
            query = query.replace(" c1)", f" {choice(biased_talias)}.c1)")
            query = query.replace(" c2)", f" {choice(biased_talias)}.c2)")
            query = query.replace("(c0,", f"({choice(biased_talias)}.c0,")
            query = query.replace("(c1,", f"({choice(biased_talias)}.c1,")
            query = query.replace("(c2,", f"({choice(biased_talias)}.c2,")
        return query

    def random_select_query(self, _data=None):
        self.init_query()
        _with = self.random_clause_with() if "WITH" in self.shared_clauses else ""
        _data = self.random_data() if _data==None else _data
        _table = self.random_table()
        _alias = "AS T1"
        self.tt.append("T1")
        self.talias.append("T1")
        _join = self.random_clause_join() if "JOIN" in self.shared_clauses else ""
        _predicate = self.random_predicate()
        _partition = self.random_clause_partition()
        _window = self.random_clause_window()
        _group = self.random_clause_group()
        _order = self.random_clause_order()
        _limit = self.random_clause_limit()
        _sample = self.random_clause_sample() if _join=="" else ""

        # it might need some constrains
        if _sample!="":
            _data = "COUNT(*)"

        select_query = f"{_with} SELECT {_data} FROM {_table} {_alias} {_join} {_predicate} {_partition} {_sample} {_window} {_group} {_order} {_limit}"

        if "CAST" in self.shared_clauses:
            select_query = self.query_mutation_add_cast(select_query)

        return select_query, _data

    def init_query(self):
        # available/usable tables/alias
        self.tt = []
        # alias
        self.talias = []
        # available/usable columns/expressions/alias
        self.ee = []

    def random_query(self):
        select_query = 0.8
        insert_query = 0.2
        update_query = 0
        return_query = ""
        if random()<select_query:
            select_query, _data = self.random_select_query()
            select_query = self.select_query_sanitize_check(select_query)
            if len(self.concats)>0:
                query_complexity = randint(0,2)
                for i in range(query_complexity):
                    next_query, _data = self.random_select_query(_data)
                    next_query = self.select_query_sanitize_check(next_query)
                    concat = choice(self.concats)
                    select_query = f"({select_query}) {concat} ({next_query})"
            if self.EVAL_CONFIG_CLAUSE_MAPPING:
                select_query = self.clause_mapping.main(select_query)
            else:
                select_query = [select_query, select_query]
            return_query = select_query
        elif random()>=1-update_query:
            update_query = self.random_update_query(choice(self.tables))
            if self.EVAL_CONFIG_CLAUSE_MAPPING:
                update_query = self.clause_mapping.main(update_query)
            else:
                update_query = [update_query, update_query]
            return_query = update_query
        else:
            insert_query = self.random_insert_query(choice(self.tables))
            if self.EVAL_CONFIG_CLAUSE_MAPPING:
                insert_query = self.clause_mapping.main(insert_query)
            else:
                insert_query = [insert_query, insert_query]
            return_query = insert_query
        return_query[0] = self.adhoc_final_query_sanitize_check(return_query[0])
        return_query[1] = self.adhoc_final_query_sanitize_check(return_query[1])
        return return_query
