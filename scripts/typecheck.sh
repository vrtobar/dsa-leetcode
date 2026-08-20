#!/usr/bin/env bash
# Type-check the repository with mypy.
#
# mypy is invoked once per top-level tree rather than once over the whole repo, because
# solution files are named after their LeetCode id: the same basename can legitimately
# appear in more than one tree, and a single whole-repo run aborts with
# "Duplicate module named ...". Trees with no solutions yet are skipped, since mypy treats
# an empty directory as an error.
set -euo pipefail

TREES=(scripts docs neetcode-150 random-problems)
status=0

for tree in "${TREES[@]}"; do
    if [[ ! -d "$tree" ]]; then
        continue
    fi
    if [[ -z "$(find "$tree" -name '*.py' -print -quit)" ]]; then
        echo "skipping $tree (no Python files yet)"
        continue
    fi
    echo "mypy $tree"
    mypy "$tree" || status=1
done

exit "$status"
