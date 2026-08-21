# DSA & LeetCode — Python

[![CI](https://github.com/vrtobar/dsa-leetcode/actions/workflows/ci.yml/badge.svg)](https://github.com/vrtobar/dsa-leetcode/actions/workflows/ci.yml)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Daily algorithm practice in Python, working through the **NeetCode 150** plus supplemental
LeetCode problems. Every solution is type-annotated, linted, and documents the approach and
its time/space complexity in the file itself.

This repo is as much about engineering habits as it is about algorithms: solutions follow a
consistent template, `ruff` and `mypy --strict` run in CI on every push, and the progress
table below is regenerated from the filesystem rather than maintained by hand.

## How each solution is written

Every file carries the problem link, a short note on the key insight when it isn't
obvious from the code, and the time/space complexity:

```python
"""1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

One pass with a hash map of value -> index; complement lookups are O(1), beats the
O(n^2) brute force.

Time:  O(n)
Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

Start a new problem from [`docs/solution_template.py`](docs/solution_template.py).

## Progress

<!-- progress:start -->
| Track | Solved | Total | Progress |
| :---- | :----: | :---: | :------- |
| Arrays & Hashing | 1 | 9 | `█░░░░░░░░░` 11% |
| Two Pointers | 0 | 5 | `░░░░░░░░░░` 0% |
| Sliding Window | 0 | 6 | `░░░░░░░░░░` 0% |
| Stack | 0 | 6 | `░░░░░░░░░░` 0% |
| Binary Search | 0 | 7 | `░░░░░░░░░░` 0% |
| Linked List | 0 | 11 | `░░░░░░░░░░` 0% |
| Trees | 0 | 15 | `░░░░░░░░░░` 0% |
| Heap / Priority Queue | 0 | 7 | `░░░░░░░░░░` 0% |
| Backtracking | 0 | 10 | `░░░░░░░░░░` 0% |
| Tries | 0 | 3 | `░░░░░░░░░░` 0% |
| Graphs | 0 | 13 | `░░░░░░░░░░` 0% |
| Advanced Graphs | 0 | 6 | `░░░░░░░░░░` 0% |
| 1-D Dynamic Programming | 0 | 12 | `░░░░░░░░░░` 0% |
| 2-D Dynamic Programming | 0 | 11 | `░░░░░░░░░░` 0% |
| Greedy | 0 | 8 | `░░░░░░░░░░` 0% |
| Intervals | 0 | 6 | `░░░░░░░░░░` 0% |
| Math & Geometry | 0 | 8 | `░░░░░░░░░░` 0% |
| Bit Manipulation | 0 | 7 | `░░░░░░░░░░` 0% |
| **NeetCode 150 total** | **1** | **150** | `░░░░░░░░░░` 1% |
| Supplemental LeetCode | 0 | — | easy: 0 · medium: 0 · hard: 0 |
<!-- progress:end -->

Full problem-by-problem checklist: [PROGRESS.md](PROGRESS.md).

## Repository structure

Files are named `<problem-id>_<slug>.py`, which keeps directories sorted by problem number
and lets the progress script detect what has been solved.

```text
├── neetcode-150/                # NeetCode 150, grouped by pattern
│   ├── 01-arrays-hashing/
│   │   └── 0001_two_sum.py
│   ├── 02-two-pointers/
│   └── ...                      # 18 pattern directories
├── random-problems/             # Supplemental LeetCode, grouped by difficulty
│   ├── easy/
│   ├── medium/
│   └── hard/
├── docs/solution_template.py    # Starting point for a new problem
└── scripts/update_progress.py   # Regenerates the table above and PROGRESS.md
```

## Running the checks locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt

make check       # ruff format, ruff check, mypy --strict, progress table freshness
make format      # apply formatting
make progress    # refresh the progress table after adding a solution
```

CI runs the same lint and type checks on every push and pull request, and regenerates the
progress table automatically when solutions land on `main`.

## License

[MIT](LICENSE)
