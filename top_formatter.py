import subprocess
import os


def top_formatter(ext):
    """
    Given desired file extension, stores top output to file in current directory.
    Supported file extensions:
    - "txt"
    - "csv"
    - "json" (wip)
    :param ext: Desired extension for output file - Type: String
    :return: Success or error message - Type: String
    """
    extensions = ["txt", "csv", "json"]

    if ext in extensions:
        # Global file path
        file_path = "top." + ext

        if ext == "txt":
            with open(file_path, "w") as outfile:
                # Store top output in txt file.
                subprocess.call("top -b -n 1", shell=True, stdout=outfile)

                return ".txt file successfully written to current directory."
        elif ext == "csv":
            with open(file_path, "w") as outfile:
                # Store top output in csv file.
                subprocess.call("top -b -n 1", shell=True, stdout=outfile)

                # Remove unwanted values at the top of the output and store in new temporary file.
                # Effectively prints from line 7 to end of output file.
                subprocess.call("sed -n '7, $p' " + file_path + " > new." + ext, shell=True)

                # Removes trailing/leading whitespace and replaces everything else with a comma.
                subprocess.call("sed -n '{s/^ *//;s/ *$//;s/  */,/gp;}' new." + ext + " > " + file_path, shell=True)

                # Remove temp file
                os.remove("new." + ext)

                return ".csv file successfully written to current directory."
    else:
        return "Invalid file extension!"
