import os
import time
from tqdm import tqdm
from driver import *
from eval_query_plan import extract_query_plan

# reset coverage
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco001.exec --reset")
os.system("rm /tmp/jacoco001.exec")

if not os.path.exists("./diff_input.log"):
    print("no log available")
    exit(-1)

questdb_api = QuestDBConnector()
postgres_api = PostgresConnector()

f = open("./diff_input.log","r")
lines = f.readlines()
f.close()

start = time.time()

logtime = 600
next_logtime = 600
stoptime = 3600 + 60

questdb_query_plans = []

for i in tqdm(range(len(lines))):
    each_line = lines[i]
    questdb_query = eval(each_line)[0]
    postgres_query = eval(each_line)[1]
    if "SELECT " in questdb_query:
        result = questdb_api.query("EXPLAIN "+questdb_query)
        questdb_query_plan = extract_query_plan(result)
        if questdb_query_plan not in questdb_query_plans:
            questdb_query_plans.append(questdb_query_plan)
        postgres_api.query(postgres_query)
    else:
        questdb_api.write_query(questdb_query)
        postgres_api.write_query(postgres_query)
    end = time.time()
    length = end - start
    if length>next_logtime:
        print(f"{next_logtime}", len(questdb_query_plans))
        # os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco_xDiff_{next_logtime}.exec")
        print(f"{next_logtime} logged")
        next_logtime += logtime
    if length>stoptime:
        break

# collect coverage
# os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco001.exec")
# os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco001.exec --html report-html --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")