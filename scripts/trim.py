
import subprocess
import os

INPUT_VIDEO = "videos/input.mp4"
OUTPUT_VIDEO = "videos/trimmed.mp4"

def trim_video():
    if not os.path.exists(INPUT_VIDEO):
        print("❌ لم يتم العثور على input.mp4")
        return

    command = [
        "ffmpeg",
        "-y",
        "-i", INPUT_VIDEO,
        "-t", "5",
        OUTPUT_VIDEO
    ]

    subprocess.run(command)
    print("✅ تم قص الفيديو بنجاح")

if __name__ == "__main__":
    trim_video()
