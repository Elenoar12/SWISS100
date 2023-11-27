import shutil
import os
import re

def move_actigraph(source_folder, destination_folder):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Iterate over all files in the source folder
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)

            # Split the file name into parts
            file_parts = filename.split("_")

            # Check if the file name has the expected number of parts
            if len(file_parts) == 4:
                # Extract the relevant parts
                project = file_parts[0]
                canton = file_parts[1]
                suffix = file_parts[2]
                idnr = re.sub(r'\(.*\)', '', file_parts[3]).split(".")[0].lstrip("0").rstrip(" ").rstrip("1sec").rstrip(" ")

                # Create the destination subfolder name
                destination_subfolder = canton + idnr

                # Create the destination subfolder if it doesn't exist
                destination_path = os.path.join(destination_folder, destination_subfolder)
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                # Move the file to the destination subfolder
                shutil.move(source_file, destination_path)
        print("Files moved successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

## Usage Actigraph
## Define the source folder (Actigraph) and the destination folder (Cases)
# source_folder = r"path\Actigraph"
# destination_folder = r"path\Cases"
# move_actigraph(source_folder, destination_folder)


def move_EAR(source_folder, destination_folder):
    # List of subfolders in the source folder
    folders = os.listdir(source_folder)

    # Regular expression to match filenames with delimiters (., _, -)
    delimiter_pattern = re.compile(r'[._-]')

    try:
        for subfolder in folders:
            # Check if the subfolder name contains any delimiter character and only include those without
            if not delimiter_pattern.search(subfolder):
                EAR_case = os.path.join(source_folder, subfolder)
                destination_subfolder = os.path.join(destination_folder, subfolder)
                # If path exists move folder to path
                if os.path.exists(destination_subfolder):
                    shutil.move(EAR_case, destination_subfolder)
                # If path does not exist create folder and move folder to created path
                else:
                    # Create a new subfolder with the case name from the source folder
                    os.makedirs(destination_subfolder)
                    shutil.move(EAR_case, destination_subfolder)
        print("Files moved successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

## Usage EAR:
## Define the source folder (EAR) and the destination folder (Cases)
# source_folder = r"path\EAR data"
# destination_folder = r"path\Cases"
# move_EAR(source_folder, destination_folder)


