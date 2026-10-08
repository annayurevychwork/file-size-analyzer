Markdown
# 📊 File Size Distribution Analyzer

> A Python-based analytical tool developed to evaluate the frequency distribution of file sizes across a local file system. Created as Lab 1 for the "Operating Systems" course at Taras Shevchenko National University of Kyiv.

---

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** `matplotlib`, `collections`, `re`
- **Data Extraction:** Windows PowerShell

---

## ⚙️ How It Works
This project analyzes the dependency between the number of files and their respective sizes on a local drive to identify storage patterns.

1. **Data Collection:** A PowerShell script recursively scans the target drive (e.g., `D:\`) and extracts the exact size of every file in bytes, saving the raw data to `files.txt`.
   Get-ChildItem -Path D:\ -Recurse -File | ForEach-Object { $_.Length } > files.txt

2. **Analysis & Categorization:** The Python script reads the raw data, sanitizes it using Regular Expressions, and sorts the file sizes into specific buckets (ranging from 0-10KB up to 1GB+).

3. **Visualization:** Using matplotlib, the script calculates the percentage makeup of each category and generates a detailed bar chart to visualize the frequency distribution.

## 📸 Results & Visualization
1. **Terminal Output & Statistics**
Statistical breakdown showing the exact count and percentage for each size category. The analysis reveals that the vast majority of files (65.75%) fall into the 0-10 KB range.
<img src="./screenshots/src1.png" width="500" />

2. **Frequency Distribution Chart**
Visual representation of the file count across all size ranges.
<img src="./screenshots/src2.png" width="500" />