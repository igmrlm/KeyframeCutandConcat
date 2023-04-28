import os
import subprocess
import shutil, sys                                                                                                                                                    


# Create 'concat' directory if it does not exist
if not os.path.exists('concat'):
    os.makedirs('concat')

# Get a list of all video files in current directory
videos = [f for f in os.listdir('.') if f.endswith('.mp4')]

# Iterate through each video file
for video in videos:
    # Ask user for start and stop times
    start_time = input(f"Enter start time for {video} (mm:ss): ")
    stop_time = input(f"Enter stop time for {video} (mm:ss): ")
    
    # Split start and stop times into mm and ss components
    start_time_mm, start_time_ss = start_time.split(':')
    stop_time_mm, stop_time_ss = stop_time.split(':')
    
    # Convert mm and ss components to integers and calculate total start and stop times in seconds
    start_time_seconds = int(start_time_mm) * 60 + int(start_time_ss)
    stop_time_seconds = int(stop_time_mm) * 60 + int(stop_time_ss)
    
    # Use ffprobe to find the closest iframe to the chosen start time
    ffprobe_command = f"ffprobe -i {video} -skip_frame nokey -show_entries frame=pkt_dts_time -select_streams v -of compact=p=0:nk=1 -v 0"
    output = subprocess.check_output(ffprobe_command, shell=True)
    iframe_times = [float(t) for t in output.decode().split() if t != 'N/A']
    start_frame = min(range(len(iframe_times)), key=lambda i: abs(iframe_times[i] - start_time_seconds))
    
    # Use ffprobe to find the closest iframe to the chosen stop time
    stop_frame = min(range(len(iframe_times)), key=lambda i: abs(iframe_times[i] - stop_time_seconds))
    
    # Use ffmpeg to trim the video to the chosen start and stop times
    output_filename = f"concat/{os.path.splitext(video)[0]}_trimmed.mp4"
    ffmpeg_command = f"ffmpeg -i {video} -ss {iframe_times[start_frame]} -to {iframe_times[stop_frame]} -c copy {output_filename}"
    subprocess.call(ffmpeg_command, shell=True)


# Copy concat.py file to concat folder
shutil.copyfile("concat.py", os.path.join("concat", "concat.py"))

# Change directory to concat folder and execute concat.py
os.chdir("concat")
subprocess.run(["python", "concat.py"])

print("Done!")
