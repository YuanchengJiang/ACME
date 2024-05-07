from driver import *
from clause_fuzzer import clauses_fuzzing
from clause_map import clauses_mapping
from query_generation import AsyncQueryGenerator


def questdb_execute_query(questdb_qpi, query):
    pass

def postgres_execute_query(postgre_api, query):
    pass

def result_analysis(questdb_result, postgres_result):
    pass

def main():
    """
    this is a demo code for testing one emerging database system QuestDB
    with the reference to mature relational database system Postgres
    """
    questdb_api = QuestDBConnector()
    postgres_api = PostgresConnector()
    # step 1: get shared clauses
    shared_clauses, reserved_clauses = clauses_fuzzing(questdb_api, postgres_api)
    # step 2: extend the set of shated clauses via clause mappings
    extended_shared_clauses = clauses_mapping(
        shared_clauses, reserved_clauses, questdb_api, postgres_api
        )
    # step 3: generate asynchornous differential inputs for testing
    query_generator = AsyncQueryGenerator(extended_shared_clauses)
    # step 4: testing and analyzing
    while True:
        query = query_generator.random_query()
        questdb_result = questdb_execute_query(questdb_api, query)
        postgres_result = postgres_execute_query(postgres_api, query)
        result_analysis(questdb_result, postgres_result)

main()