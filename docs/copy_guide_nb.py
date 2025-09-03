import json

def copy_cells(input_path, output_path, start_pattern, end_pattern):
    with open(input_path, 'r') as f:
        source_nb = json.load(f)

    start_end_idx = []
    pattern = start_pattern
    for i, cell in enumerate(source_nb['cells']):
        if cell['cell_type'] == 'markdown':
            if any(pattern in line for line in cell['source']):
                start_end_idx.append(i)
                pattern = end_pattern

    dest_nb = {
        "cells": source_nb['cells'][start_end_idx[0]:start_end_idx[1]],
        "metadata": source_nb['metadata'],
        "nbformat": source_nb['nbformat'],
        "nbformat_minor": source_nb['nbformat_minor']
    }
    with open(output_path, 'w') as f:
        json.dump(dest_nb, f, indent=2)


def main():
    input_path = "../guide.ipynb"
    output_path = "./guide_example.ipynb"
    start_pattern = "### Package Installation"
    end_pattern = "### Bioinformatics"

    copy_cells(input_path, output_path, start_pattern, end_pattern)


if __name__ == "__main__":
    main()
