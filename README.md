# Immunology 101

Interactive terminal-based immunology course for bioinformaticians and CS-background learners.

Learn immunology concepts through an interactive CLI with exercises, progress tracking, and optional AI-powered explanations — similar to how regex tutorials teach regex.

## Install

```bash
pip install -e ".[dev]"

# With AI explanations (optional)
pip install -e ".[dev,ai]"
export ANTHROPIC_API_KEY="your-key"
```

## Usage

```bash
imm101 start                  # Launch interactive course
imm101 start 01_cells_of...   # Jump to specific module
imm101 list                   # List modules + status
imm101 progress               # Progress dashboard
imm101 reset                  # Reset progress
imm101 validate               # Validate content files
```

## Exercise Types

- **Multiple choice** — pick A/B/C/D
- **Matching** — match left items to right items
- **Fill-in-the-blank** — fuzzy-matched text answers
- **Ordering** — arrange steps in correct sequence
- **Case study** — clinical scenario with keyword-matched answers

## Content License

Course content is curated from CC BY 4.0 sources (OpenStax, Frontiers, IEDB).
Software is MIT licensed.
