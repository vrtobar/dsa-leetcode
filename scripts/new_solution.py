"""Scaffold the next unsolved NeetCode 150 problem.

Walks the categories in scripts/neetcode150.json in order and creates a solution
file for the first problem that doesn't have one yet, pre-filled with the same
docstring header used by every other file in the repo.

Usage:
    python scripts/new_solution.py
    python scripts/new_solution.py --difficulty Medium
"""

from __future__ import annotations

import argparse
import sys

from update_progress import NEETCODE_DIR, REPO_ROOT, Category, Problem, load_categories, solved_ids

TEMPLATE = '''"""{id}. {title} ({difficulty})
https://leetcode.com/problems/{slug}/

One sentence on the key insight, if it's not obvious from the code. Skip it for
problems where the approach speaks for itself.

Time:  O(?)
Space: O(?)
"""


class Solution:
    def methodName(self, arg: list[int]) -> int:
        raise NotImplementedError
'''


def find_next(categories: list[Category]) -> tuple[Category, Problem] | None:
    for category in categories:
        found = solved_ids(NEETCODE_DIR / category.dir)
        for problem in category.problems:
            if problem.id not in found:
                return category, problem
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--difficulty",
        choices=("Easy", "Medium", "Hard"),
        default="<Easy|Medium|Hard>",
        help="fill in the difficulty instead of leaving a placeholder",
    )
    args = parser.parse_args()

    next_problem = find_next(load_categories())
    if next_problem is None:
        print("All NeetCode 150 problems already have a solution file.")
        return 0

    category, problem = next_problem
    path = NEETCODE_DIR / category.dir / f"{problem.id}_{problem.slug}.py"

    if path.exists():
        print(f"{path} already exists.", file=sys.stderr)
        return 1

    path.write_text(
        TEMPLATE.format(
            id=problem.id, title=problem.title, difficulty=args.difficulty, slug=problem.slug
        ),
        encoding="utf-8",
    )
    print(f"Created {path.relative_to(REPO_ROOT)} for {problem.id}. {problem.title}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
