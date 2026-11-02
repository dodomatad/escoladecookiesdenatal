import re

with open('gdrive_folder.html', 'r', encoding='utf-8', errors='ignore') as fp:
    c = fp.read()

# Find occurrences of CRIATIVO_02-OFICIAL.mp4
idx = 0
while True:
    pos = c.find('CRIATIVO_02-OFICIAL.mp4', idx)
    if pos == -1:
        break
    start = max(0, pos - 200)
    end = min(len(c), pos + 200)
    print("Match at", pos)
    print(c[start:end])
    print("="*40)
    idx = pos + 25
