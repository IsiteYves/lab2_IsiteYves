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

The application uses **Bubble Sort** to sort tweets by likes in descending order. The algorithm works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they're in the wrong order. This process continues until the list is sorted, with the highest values "bubbling up" to the front of the list. The implementation avoids using Python's built-in sorting functions as required.

## Requirements
- Python 3.x
- Bash shell
- twitter_dataset.csv file in the same directory
