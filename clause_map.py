import re

# map structure: {syntax_in_questdb: syntax_in_postgres}

# for some complex mappings, it requires query mutations
# pattern: "_MUTATION_XXX"

class ClauseMapping:

    def __init__(self):
        pass

    def extract_in_operations(self, query):
        in_operations = []
        # assume no continous spaces in the query
        query_splits = query.split(' ')
        for i in range(len(query_splits)):
            if query_splits[i]=="IN":
                in_operations.append(
                    f"{query_splits[i-1]} IN {query_splits[i+1]}"
                ) if query_splits[i-1]!="NOT" else in_operations.append(
                    f"{query_splits[i-2]} NOT IN {query_splits[i+1]}"
                )
        return in_operations

    def _clause_mapping_in_mutation(self, query):
        # this mapping aims to bridge the semantic gap in questdb
        # NULL in questdb is a specific value
        # we need to nullify results when necessary, which aligns with postgres

        # query[0] -> questdb query

        in_operations = self.extract_in_operations(query[0])
        for each_in_operation in in_operations:
            in_list = each_in_operation.split(' ')[-1]
            if "'" not in in_list:
                in_list = in_list.replace('0',"'0'").replace('1',"'1'").replace('2',"'2'")
            query[0] = query[0].replace(
                each_in_operation,
                f"CASE WHEN NULL IN {in_list} THEN NULL ELSE {each_in_operation} END"
                )
        return query

    def _clause_mapping_string_type(self, query):
        questdb_map = {"STRING": "SYMBOL"}
        postgres_map = {"STRING": "VARCHAR(64)"}
        query[0] = query[0].replace("STRING", questdb_map["STRING"])
        query[1] = query[1].replace("STRING", postgres_map["STRING"])
        return query

    def _clause_mapping_between_symmetric(self, query):
        query[1] = query[1].replace(" BETWEEN ", " BETWEEN SYMMETRIC ")
        return query

    def _clause_mapping_count_distinct(self, query):
        # Note: the syntax here is not complete for easier match
        query[1] = query[1].replace(" COUNT_DISTINCT(", " COUNT(DISTINCT")
        return query

    def main(self, query):

        # format queries before mapping
        mapped_query = [self.formatting_query(query), self.formatting_query(query)]

        # mapping IN clause
        mapped_query = self._clause_mapping_in_mutation(mapped_query)

        # mapping STRING type
        mapped_query = self._clause_mapping_string_type(mapped_query)

        # mapping BETWEEN clause
        mapped_query = self._clause_mapping_between_symmetric(mapped_query)

        # mapping
        # mapped_query = self.

        return mapped_query

    def formatting_query(self, query):
        # we format the query for easier mapping:
        # 1. no continuous spaces
        query = re.sub('[ ]+', ' ', query)
        # 2. no space between commas
        query = re.sub(', ', ',', query)
        return query


def _clause_mapping_sample_by():
    return {"SAMPLE BY", "_MUTATION_SAMPLE_BY"}

def _clause_mapping_sample_by_mutation(questdb_query):
    postgres_query = ""
    # mutation goes here
    return postgres_query

def _clause_mapping_latest_on():
    return {"LATEST ON", "_MUTATION_LATEST_ON"}

def _clause_mapping_latest_on_mutation(questdb_query):
    postgres_query = ""
    # mutation goes here
    return postgres_query

def clauses_mapping(shared_clauses, reserved_clauses, questdb_api, postgres_api):
    extended_shared_clauses = shared_clauses+[]
    return extended_shared_clauses

def async_mapping(query):
    questdb_query = query
    postgres_query = query.replace("SYMBOL", "VARCHAR(64)")
    return [questdb_query, postgres_query]