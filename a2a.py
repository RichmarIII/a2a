import os
import sys

# Check if ffmpeg is installed
if os.system('ffmpeg -version') != 0:
    print('ffmpeg is not installed')
    sys.exit(1)
    
# Print the usage of the script if the user did not provide the correct arguments
if len(sys.argv) < 2:
    print('Missing root directory argument')
    print('Usage: python a2a.py <root directory> <source format> <destination format>')
    print('Example: python a2a.py /home/user/Music flac wav')
    sys.exit(1)

if len(sys.argv) < 3:
    print('Missing source format argument')
    print('Usage: python a2a.py <root directory> <source format> <destination format>')
    print('Example: python a2a.py /home/user/Music flac wav')
    sys.exit(1)

if len(sys.argv) < 4:
    print('Missing destination format argument')
    print('Usage: python a2a.py <root directory> <source format> <destination format>')
    print('Example: python a2a.py /home/user/Music flac wav')
    sys.exit(1)

# Get the root directory from the command line arguments and convert it to an absolute path
root_dir = os.path.abspath(sys.argv[1])

# Check if the root directory exists
if not os.path.exists(root_dir):
    print(f'"{root_dir}" does not exist')
    sys.exit(1)

# Check if the root directory is a directory
if not os.path.isdir(root_dir):
    print(f'"{root_dir}" is not a directory')
    sys.exit(1)

# Get the source format from the command line arguments and add a period to the beginning
source_format = '.' + sys.argv[2]

# Get the destination format from the command line arguments and add a period to the beginning
destination_format = '.' + sys.argv[3]

# Get the specific ffmpeg codec for the destination format.
# If the destination format is m4a, use the alac codec.
# Otherwise, use the default codec for the destination format
output_codec = '-c:a alac' if destination_format == '.m4a' else ''

# Request user confirmation to continue and explain what the script will do
print(f'Convert all {source_format} files in "{root_dir}" to {destination_format} files recursively?')

# Get user input
user_input = input('Enter "y" to continue or "n" to cancel: ')

# Exit the script if the user did not enter "y"
if user_input != 'y':
    print('Exiting...')
    sys.exit(0)

# Ask the user if they want to delete the source files after conversion. Will not delete files if the conversion fails
print()
print(f'Delete {source_format} files after conversion?')
print('WARNING: This will permanently delete the source files')
print('WARNING: This will not delete files if the conversion fails')
print()

# Get user input
user_input = input('Enter "y" to continue or "n" to cancel: ')

# Set the delete_source_files variable to True if the user entered "y"
delete_source_files = user_input == 'y'

# Print a message to the user to let them know the script is running
print('Converting files...')
print()

# Create a list to store the paths of all files that failed to convert
unsuccessful_conversions = []

# Loop through all directories and files in the root directory
for root, dirs, files in os.walk(root_dir):
    # Loop through all files in the current directory
    for filename in files:
        # Check if the file is a flac file
        if filename.endswith(source_format):
            # Generate input and output file paths
            input_path = os.path.join(root, filename)
            output_path = os.path.join(root, os.path.splitext(filename)[0] + destination_format)
            # Run the ffmpeg command to convert the file
            result = os.system(f'ffmpeg -y -i "{input_path}" -vn {output_codec} "{output_path}"')
            
            # Check if the user wants to delete the source file
            if delete_source_files:
                # Check if the ffmpeg command was successful
                if result == 0:
                    # Delete the source file
                    os.remove(input_path)
                else:
                    # Print an error message if the ffmpeg command failed
                    print(f'Failed to convert "{input_path}"')
                    # Add the path of the file that failed to convert to the list
                    unsuccessful_conversions.append(input_path)

# Print a message to the user to let them know the script is finished
print()
print('Finished converting files')

# Check if any files failed to convert
if len(unsuccessful_conversions) > 0:
    # Print a message to the user to let them know which files failed to convert
    print()
    print('The following files failed to convert:')
    # Loop through all files that failed to convert
    for path in unsuccessful_conversions:
        # Print the path of the file that failed to convert
        print(path)