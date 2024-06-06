import os
import time
from tqdm import tqdm
from driver import *
from random import *
from eval_query_plan import extract_query_plan

# reset coverage
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco001.exec --reset")
os.system("rm /tmp/jacoco001.exec")

logpath = "/home/jyc/Desktop/DatabaseTesting/sqlancer/target/logs/postgres/database27-cur.log"

if not os.path.exists(logpath):
    print("no log available")
    exit(-1)

questdb_api = QuestDBConnector()
postgres_api = PostgresConnector()

f = open(logpath,"r")
lines = f.readlines()
f.close()

def sqlancer_query_adapter(query):
    my_tables = ["vuuierda","zlffztga","jqllaanm"]
    my_columns = ["c0","c1","c2"]#
    predicate = "" if "WHERE" not in query else " WHERE "+query.split("WHERE")[1]
    query = query.split("FROM")[0]+" FROM "+choice(my_tables)+" AS T1 "+predicate
    query = query.replace('t7.','')
    query = query.replace('t7','')
    query = query.replace('t6.','')
    query = query.replace('t6','')
    query = query.replace('t5.','')
    query = query.replace('t5','')
    query = query.replace('t4.','')
    query = query.replace('t4','')
    query = query.replace('t3.','')
    query = query.replace('t3','')
    query = query.replace('t2.','')
    query = query.replace('t2','')
    query = query.replace('t1.','')
    query = query.replace('t1','')
    query = query.replace('t0.','')
    query = query.replace('t0','')
    query = query.replace('c0','T1.c0')
    query = query.replace('c1','T1.c1')
    query = query.replace('c2','T1.c2')
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace('AS T1.',f'AS T1_{randint(1,100)}',1)
    query = query.replace("IS FALSE","IS NULL").replace("IS TRUE","IS NULL").replace("SELECT ALL","SELECT").replace("BETWEEN SYMMETRIC","BETWEEN").replace("::int4range","::int").replace(" ONLY "," ").replace("ISNULL", "IS NULL").replace("BOOL_AND(","count(").replace(" COLLATE ", " AND ").replace("IS NOT UNKNOWN", "IS NOT NULL").replace("::inrange","::int").replace("AS MONEY","AS INT")
    return query

questdb_query_plans = []

for i in tqdm(range(len(lines))):
    each_query = lines[i]
    if "SELECT" in each_query and each_query[0]=="S":
        try:
            query = sqlancer_query_adapter(each_query.strip('\n'))
            result = questdb_api.query("EXPLAIN "+query)
            questdb_query_plan = extract_query_plan(result)
            if questdb_query_plan not in questdb_query_plans:
                questdb_query_plans.append(questdb_query_plan)
        except Exception as e:
            pass

        if i%100==0:
            print(len(questdb_query_plans))
        # 25
        # input()

# collect coverage
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco_sqlancer_001.exec")
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_sqlancer_001.exec --html report-sqlancer-html --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")