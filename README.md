# Audio Format Converter

This Python script can be used to convert audio files from one format to another using `ffmpeg`. It will convert all files of a given source format to a specified destination format in a given directory and its subdirectories.

## Requirements

- Python 3 (needs to be installed and added to PATH)
- ffmpeg (needs to be installed and added to PATH)

## Usage

`python a2a.py <root directory> <source format> <destination format>`

### Example

`python a2a.py /home/user/Music flac wav`

The above example converts all `.flac` files to `.wav` files that are located in the `/home/user/Music` directory recursively. All metadata is preserved (except artwork, which is removed)

## Notes

- This script only supports conversion of audio files.
- Make sure to backup your files before running the script.
