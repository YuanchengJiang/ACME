import os
import time
from random import choice, randint
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

def questdb_execute_query(questdb_api, query):
    if "SELECT " in query:
        try:
            result = questdb_api.query("EXPLAIN "+query)
            questdb_query_plan = extract_query_plan(result)
            if questdb_query_plan not in questdb_query_plans:
                questdb_query_plans.append(questdb_query_plan)
                print(1)
            return result
        except Exception as e:
            return -1
    else:
        try:
            questdb_api.write_query(query)
        except Exception as e:
            return -1
        return None

def main():
    """
    this is the script to measure the query plan
    """
    questdb_api = QuestDBConnector()
    start = time.time()
    logtime = 60
    next_logtime = 60
    stoptime = 60*60*24 + 60
    query_plan_statistics = []

    logpath = "/home/jyc/Desktop/DatabaseTesting/sqlancer/target/logs/questdb/"

    alllogs = os.listdir(logpath)
    print(alllogs)

    for eachlog in alllogs:
        f = open(f"{logpath}{eachlog}","r")
        lines = f.read().split('\n')
        f.close()
        for i in tqdm(range(len(lines))):
            each_query = lines[i]
            if "SELECT" in each_query and each_query[0]=="S":
                questdb_execute_query(questdb_api, each_query)
                end = time.time()
                length = end - start
                if length>next_logtime:
                    query_plan_statistics.append(len(questdb_query_plans))
                    print(f"Mapping:{EVAL_CONFIG_CLAUSE_MAPPING} Result: {next_logtime/60} -- ", query_plan_statistics)
                    next_logtime += logtime
                if length>stoptime:
                    input("end")
            else:
                questdb_execute_query(questdb_api, each_query)

main()
