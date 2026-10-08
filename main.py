import collections
import matplotlib.pyplot as plt
import re

def file_read(file_path):
    with open(file_path, 'r', encoding='utf-16') as file:
        files = []
        for line in file:
            cleaned_line = re.sub(r'[^\d\s]', '', line.strip()) 
            if cleaned_line:
                numbers = map(int, cleaned_line.split())
                files.extend(numbers)
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return files

def categorize_size(size):
    size_intervals = [
        (10 * 1024, '0KB-10KB'), 
        (100 * 1024, '10KB-100KB'), 
        (1024 * 1024, '100KB-1MB'),  
        (10 * 1024 * 1024, '1MB-10MB'),
        (100 * 1024 * 1024, '10MB-100MB'), 
        (1024 * 1024 * 1024, '100MB-1GB'), 
        (float('inf'), '1GB+'),
    ]

    for threshold, label in size_intervals:
        if size < threshold:
            return label
    return 'Unknown'

def analyze_files(files):
    total_files = len(files)
    size_ranges = collections.defaultdict(int)

    for size in files:
        category = categorize_size(size)
        size_ranges[category] += 1

    sorted_ranges = dict(sorted(size_ranges.items(), key=lambda item: item[1], reverse=True))

    print(f"Total files: {total_files}")
    print("Distribution of file sizes:")
    for range_label, count in sorted_ranges.items():
        print(f" {range_label}: {count} - {count / total_files * 100:.2f}%")

    return sorted_ranges

def draw_graph(file_counts):
    labels = list(file_counts.keys())
    counts = list(file_counts.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color='red')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:,}', ha='center', va='bottom')

    plt.title('File Size Distribution')
    plt.xlabel('Size Range')
    plt.ylabel('File Count')
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    plt.tight_layout()

    plt.show()

def main(file_path):
    files = file_read(file_path)
    size_ranges = analyze_files(files)
    draw_graph(size_ranges)

if __name__ == '__main__':
    main('files.txt')
