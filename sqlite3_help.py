import subprocess


if __name__ == "__main__":
    proc = subprocess.run("sqlite3", capture_output=True, input=b".help")
    help = proc.stdout.decode("utf-8")
    commands = [line.split()[0] for line in help.split("\n") if line.startswith(".")]
    details = []
    for command in commands:
        filename = command.lstrip(".") + ".txt"
        proc2 = subprocess.run("sqlite3", capture_output=True, input=".help {}".format(command).encode("utf-8"))
        command_help = proc2.stdout.decode("utf-8")
        details.append(command_help.strip())
    print("# sqlite3 .help\n```")
    print("\n\n".join(details))
    print("```")
