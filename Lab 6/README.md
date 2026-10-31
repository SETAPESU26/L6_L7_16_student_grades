# L6_L7_16_student_grades — Student Grades

Lab 6: Code and Branch Coverage

## About

A small Python module that converts marks to letter grades, works out final marks with a project bonus and checks exam eligibility.

## Files

| File | Description |
|------|-------------|
| `student_grades.py` | The module under test |
| `test_student_grades.py` | Starter test file |

Refer to the lab handout for instructions.

## Run Coverage Analysis

Install the test and coverage tools:

```bash
python3 -m pip install pytest coverage
```

From the repository root, run the line-coverage suite:

```bash
cd "Lab 6"
python3 -m coverage erase
python3 -m coverage run -m pytest -q CodeCoverageTest_student_grades.py
python3 -m coverage report -m --include=student_grades.py
```

The line-coverage suite passes 14 tests and covers 100% of application statements. Its report is in [code-coverage.png](screenshots/code-coverage.png).

Run the branch-coverage suite separately:

```bash
python3 -m coverage erase
python3 -m coverage run --branch -m pytest -q BranchCoverageTest_student_grades.py
python3 -m coverage report -m --include=student_grades.py
```

The branch-coverage suite passes 26 tests and covers all 26 measured branches, with 100% total coverage. Its report is in [branch-coverage.png](screenshots/branch-coverage.png).

Line coverage confirms that every application statement ran. Branch coverage additionally confirms that both outcomes of each measured decision were exercised.
