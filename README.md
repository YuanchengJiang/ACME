# ACME

**ACME (Automated Clause Mapping Engine)** expands the scope of differential testing for database management systems by introducing **SQL clause mappings** between traditional and emerging database engines. Even a small number of mappings can greatly improve testing coverage. Nowe we find, with the help of LLMs, these mappings can now be automatically generated (LLM component will be updated in the future).

This repository contains the **demonstration code for ACME**, showcasing its functionality with **QuestDB** and **PostgreSQL**.

---

## ⚙️ Setup

1. Run setup:

   ```bash
   bash setup.sh
   ```
2. Activate environment:

   ```bash
   source pyenv/bin/activate
   ```

3. Start testing:

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

See issues reported via ACME:
[QuestDB GitHub Issues](https://github.com/questdb/questdb/issues?q=author%3AYuanchengJiang)