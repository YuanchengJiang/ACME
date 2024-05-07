
# map structure: {syntax_in_questdb: syntax_in_postgres}

# for some complex mappings, it requires query mutations
# pattern: "_MUTATION_XXX"

def _clause_mapping_between_symmetric():
    return {"BETWEEN": "BETWEEN SYMMETRIC"}

def _clause_mapping_count_distinct():
    # Note: the syntax here is not complete for easier match
    return {"COUNT_DISTINCT(": "COUNT(DISTINCT"}

def _clause_mapping_string_type():
    return {"SYMBOL", "VARCHAR(64)"}

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
    extended_shared_clauses = []
    return extended_shared_clauses
