#!/usr/bin/env python3
"""
A simple CLI log analyzer that counts INFO, WARNING, and ERROR occurrences.

Usage:
    python log_analyzer.py --input /path/to/logfile.log --output /path/to/result.txt

If you omit --output, it will default to 'summary.txt' in the current directory.
"""

import argparse
import sys
import re

def parse_args():
    parser = argparse.ArgumentParser(
        description="Count how many INFO, WARNING, and ERROR lines are in a log file."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to the input log file to analyze."
    )
    parser.add_argument(
        "-o", "--output",
        default="summary.txt",
        help="Path to the output file where counts will be written. Defaults to 'summary.txt'."
    )
    return parser.parse_args()


def analyze_log_file(input_path):
    """
    Reads the log file at input_path and returns a dictionary with counts:
      {
        "INFO":    <int>,
        "WARNING": <int>,
        "ERROR":   <int>
      }
    This function is case‐insensitive (it will count "info", "Info", "INFO", etc.).
    """
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    # Compile regex patterns once (case‐insensitive)
    info_pattern = re.compile(r"\bINFO\b", re.IGNORECASE)
    warning_pattern = re.compile(r"\bWARNING\b", re.IGNORECASE)
    error_pattern = re.compile(r"\bERROR\b", re.IGNORECASE)

    try:
        with open(input_path, "r", encoding="utf‐8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                # Check each level; increment if found
                if error_pattern.search(line):
                    counts["ERROR"] += 1
                elif warning_pattern.search(line):
                    counts["WARNING"] += 1
                elif info_pattern.search(line):
                    counts["INFO"] += 1
                # If your logs embed multiple levels per line (e.g. "INFO ... ERROR ..."), 
                # you could remove elif and use three independent if‐blocks instead.
    except FileNotFoundError:
        print(f"Error: Could not open '{input_path}' (file not found).", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error while reading '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)

    return counts


def write_summary(counts, output_path):
    """
    Writes the counts dictionary to the file at output_path in a simple text format, for example:

        INFO:  123
        WARNING:  45
        ERROR:  7
    """
    try:
        with open(output_path, "w", encoding="utf‐8") as out_f:
            out_f.write("Log Analysis Summary\n")
            out_f.write("====================\n")
            out_f.write(f"INFO:    {counts['INFO']}\n")
            out_f.write(f"WARNING: {counts['WARNING']}\n")
            out_f.write(f"ERROR:   {counts['ERROR']}\n")
    except Exception as e:
        print(f"Error while writing to '{output_path}': {e}", file=sys.stderr)
        sys.exit(1)


def main():
    args = parse_args()
    input_path = args.input
    output_path = args.output

    counts = analyze_log_file(input_path)
    write_summary(counts, output_path)
    print(f"Analysis complete. Results written to: {output_path}")


if __name__ == "__main__":
    main()
