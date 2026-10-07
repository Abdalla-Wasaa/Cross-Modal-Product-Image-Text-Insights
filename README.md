# Overview
Standalone SokoniHub retail catalog demo. Compares manual image annotations with title and description words and generates seller-facing insights. Includes three synthetic SVG image fixtures, not product photographs. An optional .txt audio transcript is attached to insights, without changing scores or titles. Requires Python 3.10+; no installation needed.

# Encoder Honesty
[encoder_pin.json](encoder_pin.json) pins lab-bow-v1 1.0.0. The fallback uses cosine similarity over a fixed vocabulary. Transformers did not run. Image pixels are not encoded: tags are manually authored. This is an image-tag/text proxy, not a pretrained multimodal model. No CLIP was used.

# Catalog Join
Run from this directory:
```sh
python3 mismatch.py
python3 check_mismatch.py
python3 insights.py
python3 analytics/build.py
python3 generation/hash_prompt.py
python3 -m unittest discover -s tests -v
```
Gold check output:
```text
KND-01 clear
NK-99 flagged
```
Score below 0.50 flags a row; exactly 0.50 passes. Unrounded scores determine flags. Threshold is chosen for teaching fixtures, not calibrated on real listings. Title and description are concatenated into a bag of words; missing vocabulary is ignored, zero vectors score zero. The Nike-titled bag has limited overlap with manually annotated woven-kiondo tags. [mismatch_report.json](mismatch_report.json) records results. Image files must exist under images/; duplicate SKUs are rejected.

# Insights
[insights.json](insights.json) is a stable array of sku, score, flag and seller_message objects, with transcript and transcript_source when present. Original catalog text is never rewritten. Transcript sidecars are read from audio/; no Whisper transcription runs.

# Tools
[hf_pipeline.yaml](hf_pipeline.yaml) records task, model, revision, CPU device and fallback backend; it is configuration evidence, not a claim of a Hugging Face run. [generation/](generation/) holds prompt, SHA-256 pin, deterministic SVG stub and provenance. [gen_twin.json](gen_twin.json) maps Stub Generator to a prospective Stable Diffusion path; Stable Diffusion was not executed. Generated concepts carry not_a_photo_of_the_sku and never enter images/ or gold scoring. [images/provenance.json](images/provenance.json) separately documents synthetic evaluation fixtures. No generation API is called.

# Analytics
[analytics/rates.json](analytics/rates.json) includes n=3, denominator=3 and flagged count. This is a fixture rate, not a market estimate. Run `python3 analytics/search.py "navy sisal kiondo" -k 2` for ranked SKUs. Search uses image tags, omits zero-score results and breaks ties by SKU. [analytics/vocab_gaps.json](analytics/vocab_gaps.json) records token coverage and missing words. See [analytics report](analytics/analytics_report.md) for recall limitations.

# Ethics
Read [ethics_note.md](ethics_note.md) for photo privacy, language coverage, generated content and review steps.

# Manager Summary
Read [manager_summary.md](manager_summary.md) for risks, mitigations and limits.

# Fallbacks
No GPU, transformers, Whisper or image generation API is used. Runtime is standard-library Python on CPU. Images are synthetic fixtures with manual tags; transcript is a synthetic .txt sidecar; generation is a deterministic SVG stub. No external model download, inference fee or seller-data upload occurs. Actual-photo accuracy is unmeasured.

# Week Reuse
Week 5: image/text and optional audio concepts. Week 7: cost awareness and reproducible checks. Week 8: pinning, evaluation and observability through explicit artifact metadata. Week 9: governance, provenance and privacy practices. Week 10 lab code was inspected as reference; this implementation is standalone and does not import or modify classwork. AfyaPlus clinical fixtures are excluded.

See [CONTRIBUTING.md](CONTRIBUTING.md) for branches, reviews and release practice. Remote synchronization depends on network access.
