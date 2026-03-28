# Social Media Data Detective - Lab 2

## Overview
A Python application that analyzes social media data from Twitter with custom sorting algorithms and Bash scripting for command-line data processing.

## Files
- `data-detective.py` - Main Python application
- `feed-analyzer.sh` - Bash script for user activity analysis
- `twitter_dataset.csv` - Dataset file (download from Kaggle)

## Usage Instructions

### Python Application
```bash
python data-detective.py
```

The application will:
1. Load and clean the Twitter dataset
2. Find the viral tweet with most likes
3. Display top 10 most liked tweets using custom Bubble Sort
4. Allow keyword search through tweets

### Bash Script Analyzer
```bash
bash feed-analyzer.sh
```

### Windows PowerShell Alternative
```powershell
powershell -ExecutionPolicy Bypass -File feed-analyzer.ps1
```

Displays the top 5 most active users by tweet count.

## Custom Sorting Algorithm

The application uses **Selection Sort** to sort tweets by likes in descending order. The algorithm works by repeatedly finding the maximum element from the unsorted portion and placing it at the beginning. For each position, it scans through the remaining unsorted elements to find the highest value, then swaps it into place. This process continues until the entire list is sorted with the highest values at the front. The implementation avoids using Python's built-in sorting functions as required.

## Requirements
- Python 3.x
- Bash shell
- twitter_dataset.csv file in the same directory
