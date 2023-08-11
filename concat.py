import os

# get list of video files in current directory
video_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith('.mp4')]

# create filelist.txt file with list of video files to concatenate
with open('filelist.txt', 'w') as f:
    for video_file in video_files:
        f.write(f"file '{video_file}'\n")

# ask user for output filename
output_filename = input("Enter the output filename (including extension): ")

# run ffmpeg command to concatenate videos
os.system(f"ffmpeg -f concat -safe 0 -i filelist.txt -c copy {output_filename}")

# delete filelist.txt file
os.remove('filelist.txt')
