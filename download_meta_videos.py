import urllib.request
import json
import os

with open(r'C:\Users\dedeu\.gemini\antigravity\brain\f4f213af-3982-4ea2-8a14-37b7991a4356\.system_generated\steps\211\output.txt', 'r', encoding='utf-8') as fp:
    lines = fp.readlines()

content = "".join(lines)
# find json
start = content.find('[')
end = content.rfind(']') + 1
videos = json.loads(content[start:end])

print(f"Total videos parsed: {len(videos)}")

# Download the first 3 videos to analyze
for i, v in enumerate(videos[:3]):
    src = v['src']
    out_name = f"meta_video_{i+1}.mp4"
    if not os.path.exists(out_name):
        print(f"Downloading video {i+1} ({v['duration']:.1f}s) to {out_name}...")
        try:
            req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp, open(out_name, 'wb') as out_f:
                out_f.write(resp.read())
            print(f"Downloaded {out_name}! Size: {os.path.getsize(out_name)} bytes")
        except Exception as e:
            print(f"Error downloading {i+1}: {e}")
    else:
        print(f"{out_name} already exists.")
