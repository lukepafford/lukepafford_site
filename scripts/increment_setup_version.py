import sys
import re
import argparse
import tempfile
import shutil

parser = argparse.ArgumentParser(
    description="Increments the major, minor, or patch number in a setup file",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("setup_file", type=str, help="path to setup.py file")
parser.add_argument(
    "--version-type", type=str, choices=["major", "minor", "patch"], default="patch"
)
args = parser.parse_args()

setup_file = args.setup_file
version_type = args.version_type

# Read the setup file
with open(setup_file) as f:
    try:
        data = f.read()
    except FileNotFoundError as f:
        print(f)
        sys.exit(1)

# Identify the version inside the setup.py, and replace the string with
# a value that is incremented
pattern = re.compile(
    "(?P<prefix>version\s*=\s*('|\"))(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?P<suffix>('|\"))"
)
match = re.search(pattern, data)
incremented_version = str(int(match.group(version_type)) + 1)

# This feels like a brute force solution, and it can be done betteer
if version_type == "major":
    new_version = (
        incremented_version + "." + match.group("minor") + "." + match.group("patch")
    )
    repl = match.group("prefix") + new_version + match.group("suffix")
elif version_type == "minor":
    new_version = (
        match.group("major") + "." + incremented_version + "." + match.group("patch")
    )
    repl = match.group("prefix") + new_version + match.group("suffix")

elif version_type == "patch":
    new_version = (
        match.group("major") + "." + match.group("minor") + "." + incremented_version
    )
    repl = match.group("prefix") + new_version + match.group("suffix")
incremented_data = re.sub(pattern, repl, data)


# Write the setup file to a temp file
with tempfile.NamedTemporaryFile(delete=False) as temp:
    temp.write(incremented_data.encode("utf8"))

# Replace the original setup.py file with the temp file
shutil.move(temp.name, setup_file)

# Print out the incremented version to be used by other commands
print(new_version)
