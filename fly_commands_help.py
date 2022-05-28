import subprocess
import sys

run = subprocess.check_output


def extract_commands(output):
    try:
        lines = output.split("Commands:")[1].split("\n\nFlags:")[0].split("\n")
    except IndexError:
        return []
    commands = [l.strip().split()[0] for l in lines if l.strip() and l[:2] == "  "]
    print(commands)
    return commands


def save_help_for_command_and_subcommands(run, path):
    print(path)
    command_help = run(path + ["--help"])
    open("flyctl/{}.txt".format("-".join(path)), "w").write(command_help)
    subcommands = extract_commands(command_help)
    for subcommand in subcommands:
        save_help_for_command_and_subcommands(run, path + [subcommand])


if __name__ == "__main__":
    fly_bin = sys.argv[-1]
    assert fly_bin.endswith("flyctl")

    def run(args):
        return subprocess.check_output([fly_bin] + args).decode("latin-1")

    open("flyctl/flyctl-flyctl-version.txt", "w").write(run(["version"]))
    help = run(["--help"])
    open("flyctl/flyctl-help.txt", "w").write(help)

    commands = extract_commands(help)
    for command in commands:
        save_help_for_command_and_subcommands(run, [command])
