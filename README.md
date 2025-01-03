# SQLxDiff

In recent years, a plethora of database management systems have surfaced to meet the demands of various scenarios. Emerging database systems, such as time-series and streaming database systems, are tailored to specific use cases requiring enhanced functionality and performance. However, as they are typically less mature, there can be bugs that either cause incorrect results or errors impacting reliability. To tackle this, we propose enhanced differential testing to uncover various bugs in emerging SQL-like database systems. The challenge is how to deal with differences of these emerging databases. Our insight is that many emerging database systems are conceptually extensions of relational database systems, making it possible to reveal logic bugs leveraging existing relational, known-reliable database systems. However, due to inevitable syntax or semantics gaps, it remains challenging to scale differential testing to various emerging database systems. We enhance differential testing for emerging database systems with three steps: (i) identifying shared clauses; (ii) extending shared clauses via mapping new features back to existing clauses of relational database systems; and (iii) generating differential inputs using extended shared clauses. We implemented our approach in a tool called SQLxDiff and applied it to four popular emerging database systems. In total, we found 57 unknown bugs, of which 17 were logic bugs and 40 were internal errors. Overall, vendors fixed 50 bugs and confirmed 5. Our results demonstrate the practicality and effectiveness of SQLxDiff in detecting bugs in emerging database systems, which has the potential to improve the reliability of their applications.

**This is the demonstration code for SQLxDiff, showcasing its functionality with QuestDB and Postgres.**

## Setup

### Prerequisites

- Ensure you have set up the related databases (QuestDB and Postgres). Please refer to `driver.py` for the connection details.
- Python (version 3.8 or later) installed.
- Install necessary Python libraries using `pip install -r requirements.txt`.

### Usage

- Run the main script to start the comparison: `python main.py` 
