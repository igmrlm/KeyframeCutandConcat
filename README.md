# KeyframeCutandConcat

This program is perfect for editing HDR Video without an expensive Graphics card that supports HDR editing, a software licence for Davinci Resolve Studio / Adobe Premiere pro & a HDR screen

This Python program is designed to trim video files to specific start and stop times using the `ffprobe` and `ffmpeg` command line tools. It sequentially goes through each video in the folder it's been executed from, asks the user to specify the start and stop times in the format `mm:ss`, finds the closest iframe to the chosen time using `ffprobe`, and trims the video to that time using `ffmpeg`. The trimmed video is saved in a subfolder titled `concat` as `original_filename_trimmed.mp4`.

## Dependencies

This program requires the following command line tools to be installed:

- `ffprobe`
- `ffmpeg`

These tools can typically be installed using your operating system's package manager. 

## Usage

1. Download the `trim.py` and `concat.py` files and save them in the directory containing the video files you wish to trim.
2. Open a terminal window and navigate to the directory containing the `trim.py` file.
3. Run the program by typing `python trim.py` in the terminal and pressing enter.
4. For each video file, enter the start and stop times in the format `mm:ss` when prompted.
5. The trimmed videos will be saved in the `concat` subfolder.

## How it works

The program first checks if a subfolder titled `concat` exists in the current directory. If it does not, the program creates it using the `os` module.

The program then uses the `os` module to get a list of all video files in the current directory. It iterates through each video file and prompts the user to enter the start and stop times in the format `mm:ss`.

The program then uses the `subprocess` module to execute the `ffprobe` command on the video file to find the closest iframe to the chosen start and stop times. The output of the `ffprobe` command is parsed to extract the iframe times, which are converted to floats.

The program then uses the `min()` function to find the index of the iframe closest to the chosen start and stop times. The chosen start and stop times are converted from `mm:ss` format to seconds, and the closest iframe times are used to calculate the start and stop frames.

Finally, the program uses the `subprocess` module to execute the `ffmpeg` command on the video file to trim it to the chosen start and stop times. The trimmed video is saved in the `concat` subfolder with the filename `original_filename_trimmed.mp4`.

Lastly, it changes directory to the concat folder and executes the `concat.py` script to concat all the video files.
