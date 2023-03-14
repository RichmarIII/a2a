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

## Script Explanation

1. The script first checks if `ffmpeg` is installed. If not, it will exit.
2. It then checks if the correct number of arguments are provided. If not, it will print a usage message and exit.
3. The script verifies the existence and validity of the provided root directory.
4. The script prompts the user for confirmation before proceeding with the conversion.
5. The user can choose whether to delete the source files after conversion. If the conversion fails, the source files will not be deleted.
6. The script converts the files and keeps track of any unsuccessful conversions.
7. Once the conversion is complete, the script prints a summary of the results.

## Notes

- This script only supports conversion of audio files.
- Make sure to backup your files before running the script.
