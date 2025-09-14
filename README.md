# ACME

**ACME (Automated Clause Mapping Engine)** is a novel approach that **extends differential testing** for emerging database systems by introducing **SQL clause mappings** between traditional and new database engines.

Emerging systems such as time-series, streaming, and vector databases often extend relational models but introduce **syntactic and semantic differences**. These differences make conventional differential testing either ineffective (false alarms) or limited (reduced coverage). ACME addresses this challenge by **bridging syntax/semantics gaps via clause mappings**, enabling scalable and generalized bug detection.

This repository contains **demonstration code** for ACME, showcasing its functionality with **QuestDB** and **PostgreSQL**. (LLM component will be updated later)

---

### 🧠 Core Idea

The key to a generalized testing strategy is a robust **test oracle**. Traditional relational databases (e.g., PostgreSQL) are well-established and reliable, making them a natural reference for differential testing. However, emerging databases diverge in their query syntax and clause semantics, requiring **semantically equivalent queries** for fair comparison.

ACME solves this by:

* **Mapping new or altered clauses** from emerging systems into equivalent constructs in relational systems.
* **Automatically generating equivalent queries** that expand clause coverage while avoiding false alarms.

* (**Leveraging LLMs** as a knowledge bridge to interpret clause semantics, generate mappings, and validate them with minimal test queries.) (this is for reducing manual effort)

If two systems disagree **after mapping**, the discrepancy indicates a logic bug in the emerging system.

---

### 🐞 Example: Logic Bug in QuestDB

```sql
CREATE TABLE test (c0 INT);        -- Initialize Schema
INSERT INTO test VALUES (NULL);    -- Initialize Data

-- Original Query
Q: SELECT (c0 IN (0, NULL)) FROM test;
-- QuestDB: [(True)] 
-- Postgres: [(Null)] 
-- => Mismatch, but expected due to NULL semantics

-- Mapped Query
Q(mapped): SELECT (CASE WHEN c0 IS NULL THEN NULL ELSE c0 IN (0) END) FROM test;
-- QuestDB Result After Mapping: [(False)] 
-- => True Bug Discovered
```

Without mappings, this case would either be ignored (missing bugs) or flagged as a false alarm. With ACME, the semantic mapping exposes a genuine logic bug, later acknowledged and fixed by QuestDB.

```sql
-- Using SYMBOL type
CREATE TABLE test (c_0 SYMBOL);
INSERT INTO test VALUES ('A');
SELECT count_distinct(c_0) FROM test WHERE c_0 > 'Z';
-- QuestDB Result: [(1)]

-- Using VARCHAR type
CREATE TABLE test (c_0 VARCHAR(16));
INSERT INTO test VALUES ('A');
SELECT count(DISTINCT c_0) FROM test WHERE c_0 > 'Z';
-- PostgreSQL Result: [(0)]
```

Simple, necessary, and effective clause mapping from type `SYMBOL` to `VARCHAR`. 

---

## ⚙️ Setup

1. Install dependencies and initialize environment:

   ```bash
   bash setup.sh
   source pyenv/bin/activate
   ```

2. Start testing:

   ```bash
   python main.py
   ```

---

## 📊 Result Analysis

* **Logic bug reports:** `./bug.log`
* **Differential query pairs (QuestDB ↔ PostgreSQL):** `./diff_input.log`
* **Full query logs:** `./questdb_testing.log`, `./postgres_testing.log`
* **Exception logs (potential internal errors):** `./questdb_exception.log`

---

## 🐞 Reported Bugs

Bugs discovered by ACME have been reported and acknowledged by QuestDB:
👉 [QuestDB GitHub Issues](https://github.com/questdb/questdb/issues?q=author%3AYuanchengJiang)


