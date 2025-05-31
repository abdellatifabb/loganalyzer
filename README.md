# CLI Log Analyzer

**Author:** abdellatif er-razzouqi

---

## Description

This project is a simple command-line log analyzer written in Python. It reads a plain‐text log file, counts how many lines contain the keywords `INFO`, `WARNING`, and `ERROR`, and writes those counts to an output summary file.

---

## Files

- `log_analyzer.py`  
  The main Python script. It accepts an input log file and (optionally) an output filename, then produces a summary of INFO/WARNING/ERROR counts.

- `README.md`  
  This file, containing project details and usage instructions.

---

## Requirements

- Python 3.6 or higher  
- No external dependencies (uses only the Python standard library: `argparse`, `re`, `sys`).

---

## Installation

1. **Clone or download** this repository to your local machine.
2. Ensure you have Python 3 installed. You can check by running:
   ```bash
   python3 --version
