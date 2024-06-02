import os
import time

# reset coverage
os.system("java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco001.exec --reset")
os.system("rm /tmp/jacoco001.exec")

start = time.time()

# every 20 mins
logtime = 1200
next_logtime = 1200
stoptime = 3600 + 60

approach = 'sqlancer'

time.sleep(2)

os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco_{approach}_000.exec")
os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_{approach}_000.exec --html ./coverage_reports/report-html-{approach}-000 --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")

print("inited")

while True:
    time.sleep(2)
    end = time.time()
    length = end - start
    if length>next_logtime:
        os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar dump --address 127.0.0.1 --port 36320 --destfile /tmp/jacoco_{approach}_{next_logtime}.exec")
        print(f"{next_logtime} logged")
        os.system(f"java -jar /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/lib/jacococli.jar report /tmp/jacoco_sqlancer_{next_logtime}.exec --html ./coverage_reports/report-html-{approach}-{next_logtime} --classfiles /home/jyc/Desktop/DatabaseTesting/questdb-7.4.2-no-jre-bin/questdb.jar")
        next_logtime += logtime
        print("report generated")
    if length>stoptime:
        break
