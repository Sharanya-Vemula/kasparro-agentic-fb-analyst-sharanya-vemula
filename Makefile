.PHONY: install run test lint

install:
\tpip install -r requirements.txt

run:
\tpython src/run.py "Analyze ROAS drop in last 7 days"

test:
\tpytest -q

lint:
\tpython -m compileall src
