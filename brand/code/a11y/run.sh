#!/bin/bash
# usage: run.sh script.py name
cd "$(dirname "$1")" && A11YNAME="$2" python3 -c "import sys;sys.path.insert(0,'/home/claude/a11y');import a11y,runpy;runpy.run_path('$1',run_name='__main__')"
