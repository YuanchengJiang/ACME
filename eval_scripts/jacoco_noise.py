import os
import time
import datetime
from tqdm import tqdm
from driver import *
from random import randint, choice
from eval_query_plan import extract_query_plan

# reset coverage
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco001.exec --reset")
os.system("rm /tmp/jacoco001.exec")

if not os.path.exists("./diff_input.log"):
    print("no log available")
    exit(-1)

questdb_api = QuestDBConnector()
postgres_api = PostgresConnector()

start = time.time()

insert_query = f"EXPLAIN INSERT INTO kkzkhtob VALUES (-423,'g','{datetime.datetime.now()}');"

logtime = 600
next_logtime = 600
stoptime = 3600 + 60

questdb_query_plans = []

while True:
    query = choice(["EXPLAIN SELECT COUNT(*) FROM kkzkhtob","EXPLAIN SELECT COUNT(NULL) FROM kkzkhtob"])
    questdb_query = query
    postgres_query = query
    if randint(1,100)>98:
        questdb_query = insert_query
        postgres_query = insert_query
    if "SELECT " in questdb_query:
        try:
            result = questdb_api.query(questdb_query)
            questdb_query_plan = extract_query_plan(result)
            if questdb_query_plan not in questdb_query_plans:
                questdb_query_plans.append(questdb_query_plan)
            result = postgres_api.query(postgres_query)
        except Exception as e:
            print(str(e))
            pass
    else:
        questdb_api.write_query(questdb_query)
        postgres_api.write_query(postgres_query)
    print(len(questdb_query_plans))
    # Code here
    # Calculate the end time and time taken
    end = time.time()
    length = end - start
    if length>next_logtime:
        os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco_{next_logtime}.exec")
        print(f"{next_logtime} logged")
        next_logtime += logtime
    if length>stoptime:
        break

os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_600.exec --html report-html-10 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_1200.exec --html report-html-20 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_1800.exec --html report-html-30 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_2400.exec --html report-html-40 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_3000.exec --html report-html-50 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_3600.exec --html report-html-60 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")