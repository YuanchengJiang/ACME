import os
import time
from tqdm import tqdm
from driver import *
from eval_query_plan import extract_query_plan
from clause_fuzzer import clauses_fuzzing
from query_generation import AsyncQueryGenerator

EVAL_CONFIG_CLAUSE_MAPPING = False

questdb_api = QuestDBConnector()
postgres_api = PostgresConnector()

start = time.time()

logtime = 600
next_logtime = 600
stoptime = 36000 + 60

questdb_query_plans = []

def questdb_execute_query(questdb_qpi, query):
    if "SELECT " in query:
        try:
            result = questdb_qpi.query("EXPLAIN "+query)
            questdb_query_plan = extract_query_plan(result)
            if questdb_query_plan not in questdb_query_plans:
                questdb_query_plans.append(questdb_query_plan)
            return result
        except Exception as e:
            return -1
    else:
        try:
            questdb_qpi.write_query(query)
        except Exception as e:
            return -1
        return None

def postgres_execute_query(postgre_api, query):
    if "SELECT " in query:
        try:
            result = postgre_api.query(query)
            return result
        except Exception as e:
            postgre_api.reconnect()
            return -1
    else:
        try:
            postgre_api.write_query(query)
        except Exception as e:
            postgre_api.reconnect()
            return -1
        return None

def main():
    """
    this is the script to measure the query plan
    """
    questdb_api = QuestDBConnector()
    postgres_api = PostgresConnector()
    # step 1: get shared clauses
    shared_clauses = clauses_fuzzing(questdb_api, postgres_api)
    # step 2: extend the set of shated clauses via clause mappings
    # step 3: generate asynchornous differential inputs for testing
    query_generator = AsyncQueryGenerator(shared_clauses, EVAL_CONFIG_CLAUSE_MAPPING)
    # step 4: testing and analyzing
    testing_round = 0
    start = time.time()
    logtime = 60*30
    next_logtime = 60*30
    stoptime = 60*60*24 + 60
    query_plan_statistics = []
    while True:
        query_generator.init_table(questdb_api, postgres_api)
        testing_round += 1
        print(f"testing round {testing_round}")
        for i in tqdm(range(2000)):
            query = query_generator.random_query()
            questdb_execute_query(questdb_api, query[0])
            postgres_execute_query(postgres_api, query[1])
            end = time.time()
            length = end - start
            if length>next_logtime:
                query_plan_statistics.append(len(questdb_query_plans))
                print(f"Mapping:{EVAL_CONFIG_CLAUSE_MAPPING} Result: {next_logtime/60} -- ", query_plan_statistics)
                next_logtime += logtime
            if length>stoptime:
                input("end")

main()
