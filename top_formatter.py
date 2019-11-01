import subprocess
import os


def top_formatter(ext):
    """
    Given desired file extension, stores top output to file in current directory.
    Supported file extensions:
    - "txt"
    - "csv"
    - "json" (WIP)
    :param ext: Desired extension for output file - Type: String
    :return: Success or error message - Type: String
    """
    extensions = ["txt", "csv", "json"]

    if ext in extensions:
        txt_path = "top.txt"
        csv_path = "top.csv"
        json_path = "top.json"

        if ext == "txt":
            with open(txt_path, "w") as outfile:
                # Store top output in txt file.
                subprocess.call("top -b -n 1", shell=True, stdout=outfile)

            return ".txt file successfully written to current directory."
        elif ext == "csv" or ext == "json":
            with open(csv_path, "w") as outfile:
                # Store top output in csv file.
                subprocess.call("top -b -n 1 | sed -n '7, $p' | sed -n '{s/^ *//;s/ *$//;s/  */,/gp;}'", shell=True, stdout=outfile)

                # Convert to json
                if ext == "json":
                    subprocess.call("jq -R -s -f scripts/csv2json.jq " + csv_path + " > " + json_path, shell=True)

                    # Remove donor csv file
                    os.remove(csv_path)

                    return ".json file successfully written to current directory."

            return ".csv file successfully written to current directory."
    else:
        return "Invalid file extension!"
