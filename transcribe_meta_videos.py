from faster_whisper import WhisperModel
import json

print("Loading Whisper model (tiny or base)...")
model = WhisperModel("base", device="cpu", compute_type="int8")

files = ["meta_video_1.mp3", "meta_video_2.mp3", "meta_video_3.mp3"]

results = {}

for f in files:
    print(f"\n--- Transcribing {f} ---")
    segments, info = model.transcribe(f, language="pt", beam_size=1)
    transcription = []
    for s in segments:
        transcription.append({
            "start": round(s.start, 2),
            "end": round(s.end, 2),
            "text": s.text.strip()
        })
        print(f"[{s.start:.1f}s -> {s.end:.1f}s]: {s.text.strip()}")
    results[f] = transcription

with open("transcriptions_meta.json", "w", encoding="utf-8") as fp:
    json.dump(results, fp, ensure_ascii=False, indent=2)

print("\nDone! Saved to transcriptions_meta.json")
