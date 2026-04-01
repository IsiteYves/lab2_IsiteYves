#!/bin/bash

# feed-analyzer.sh
# Analyzes twitter_dataset.csv to find the Top 5 Most Active Users

if [ ! -f "twitter_dataset.csv" ]; then
    echo "Error: twitter_dataset.csv not found!"
    exit 1
fi

echo "=== TOP 5 MOST ACTIVE USERS ==="
echo "Format: [Count] [Username]"
echo ""

# Extract username column, sort, count occurrences, sort by count, show top 5
cut -d',' -f2 twitter_dataset.csv | tail -n +2 | sort | uniq -c | sort -nr | head -5
