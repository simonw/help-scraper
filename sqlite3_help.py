import subprocess


if __name__ == "__main__":
    help = subprocess.run("sqlite3", capture_output=True, input=b".help").stdout.decode(
        "utf-8"
    )
    # Get the version
    version = (
        subprocess.run(["sqlite3", "--version"], capture_output=True)
        .stdout.decode("utf-8")
        .strip()
    )
    commands = [line.split()[0] for line in help.split("\n") if line.startswith(".")]
    details = []
    for command in commands:
        filename = command.lstrip(".") + ".txt"
        command_help = subprocess.run(
            "sqlite3",
            capture_output=True,
            input=".help {}".format(command).encode("utf-8"),
        ).stdout.decode("utf-8")
        details.append(command_help.strip())
    print("# sqlite3 .help\n\nVersion: `{}`\n\n```".format(version))
    print("\n\n".join(details))
    print("```")
