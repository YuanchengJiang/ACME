# SQLxDiff

The key idea of SQLxDiff is to expand the working scope of differential testing on database management systems by adopting SQL query mappings between old and new database instances. We observe that small efforts into query mappings pay off with greater testing coverage. 

See more details at https://arxiv.org/abs/2501.01236

**This is the demonstration code for SQLxDiff, showcasing its functionality with QuestDB and Postgres.**

## Setup

### Prerequisites

- Ensure you have set up the related databases (QuestDB and Postgres). Please refer to `driver.py` for the connection details.
- Python (version 3.8 or later) installed.
- Install necessary Python libraries using `pip install -r requirements.txt`.

### Usage

- Run the main script to start the comparison: `python main.py`

### Bugs

- See https://github.com/questdb/questdb/issues?q=is%3Aissue+author%3AYuanchengJiang+
