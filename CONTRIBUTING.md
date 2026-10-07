# Contributing
Create focused branches such as feat/catalog-join, feat/insights, feat/multimodal-artifacts, feat/analytics and docs/ethics-summary from main. Use semantic commits: feat(join), feat(insights), feat(multimodal), feat(analytics), docs(ethics), fix or test. Submit a pull request before merging into main; keep unrelated classwork outside this repository.

Use semantic versions: major for incompatible report schemas, minor for compatible capabilities, patch for fixes. Pin encoder and prompt changes and regenerate evidence in the same change. Reviewers check encoder honesty, provenance, privacy, original-title preservation and test results. Never commit credentials, .env files, .claude/, CLAUDE.md or AGENTS.md.

For release, run the README commands and test suite, inspect generated diffs, obtain review, merge and tag v1.0.0 (or the next appropriate version). Include limitations and validation in release notes. Remote PRs and tags require an available remote; local branches and commits can be prepared offline.
