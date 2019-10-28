import subprocess


def top_formatter(ext):
    """
    Given user inputted file extension, output mem usage sorted by
    user to an output file.
    :param ext: Desired extension for output file - Type: String
    :return: Success or error message - Type: String
    """
    extensions = ["txt", "json", "html"]

    if ext in extensions:
        with open("output." + ext, "w") as outfile:
            subprocess.call("top -b -n 1", shell=True, stdout=outfile)

        return "File successfully written to current directory."
    else:
        return "Invalid file extension!"
