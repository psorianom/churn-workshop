# Tasks

Each task is written the way a stakeholder would describe it.
For the agent tasks, copy the text of your task and paste it into the agent as your starting prompt.

The loop for every agent task:

> Plan -> Grill (the agent asks you questions) -> Execute -> Read the diff -> Grill (the agent reviews itself) -> Commit -> Push

Before you start: create a branch (`git switch -c <name>`) and make sure `git status` is clean.
Before you finish: read the diff yourself, run `pytest` and `python run.py`, then commit and push the branch.

---

## Task 1 (by hand, no agent)

Task text:

> One of the model's inputs, the average monthly charge of each customer's region, looks wrong for some
> customers. Find out why and fix it.

Start here: `pytest` shows that `test_region_feature_for_missing_region` fails. Set a breakpoint in
`add_region_features`, debug the test, and look at the customers that have no region.

How to check: `pytest tests/test_features.py::test_region_feature_for_missing_region` should pass.

---

## Task 2 (guided session, with the agent)

Task text:

> The pipeline output shows more rows after the features step than after cleaning. Each customer should
> appear exactly once. Find out why and fix it.

How to check: `pytest tests/test_features.py::test_merge_preserves_row_count` should pass, and the `rows:`
line printed by `python run.py` should show the same number for `clean` and `features`.

---

## Task 3 (challenge, with the agent)

Task text:

> Our AUC changes every time we run the pipeline, so we cannot compare any changes. Make the results
> reproducible.

How to check: `pytest tests/test_pipeline.py::test_training_is_deterministic` should pass, and running
`python run.py` several times should print the same AUC every time.

---

## Task 4 (challenge, with the agent)

Task text:

> The stakeholder wants an AUC of at least 0.85, but we get about 0.82. Improve the pipeline.

How to check: run `pytest` and `python run.py`.

If your AUC is not about 0.82 on a clean run, ask for the checkpoint branch for this task.
