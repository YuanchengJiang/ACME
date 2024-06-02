import re

def extract_query_plan(results):
    query_plan = []
    for eachline in results:
        query_plan_step = eachline[0].replace(' ','')
        if ':' in query_plan_step:
            query_plan_step = query_plan_step.split(':')[0]
        query_plan.append(query_plan_step)
    return query_plan