import subprocess
import sys

if __name__ == "__main__":
    # Usage: python3 sqlite3_help.py /path/to/sqlite3
    bin = sys.argv[-1]
    help = subprocess.run(bin, capture_output=True, input=b".help").stdout.decode(
        "utf-8"
    )
    # Get the version
    version = (
        subprocess.run([bin, "--version"], capture_output=True)
        .stdout.decode("utf-8")
        .strip()
    )
    commands = [line.split()[0] for line in help.split("\n") if line.startswith(".")]
    details = []
    for command in commands:
        filename = command.lstrip(".") + ".txt"
        command_help = subprocess.run(
            bin,
            capture_output=True,
            input=".help {}".format(command).encode("utf-8"),
        ).stdout.decode("utf-8")
        details.append(command_help.strip())
    print("# sqlite3 .help\n\nVersion: `{}`\n\n```".format(version))
    print("\n\n".join(details))
    print("```")
