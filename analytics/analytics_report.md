# Fixture analytics
The denominator is all three synthetic catalog rows, with one flag. Run build.py to regenerate rates and title-plus-description token coverage. Vocabulary gaps include ordinary words and local context; token coverage is not semantic understanding.

A single hand-chosen retrieval query ranks KND-01 first for "navy sisal kiondo". This is a smoke check, not a recall benchmark. Measuring recall@k requires independently labeled relevant SKU sets and held-out English/Swahili queries, including synonyms and misspellings. Unknown-only queries return no results. Manual tags, ASCII tokens and three fixtures limit generalization; brand legitimacy and image accuracy are unmeasured. The threshold was selected on fixtures and must be calibrated separately for deployment.
