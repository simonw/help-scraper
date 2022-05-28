import subprocess
import sys

run = subprocess.check_output

def extract_commands(output):
    try:
        lines = output.split("Commands:")[1].split("\n\nFlags:")[0].strip().split("\n")
    except IndexError:
        return []
    return [l.strip().split()[0] for l in lines if l.strip()]


if __name__ == "__main__":
    fly_bin = sys.argv[-1]
    assert fly_bin.endswith("flyctl")

    def run(*args):
        return subprocess.check_output([fly_bin] + list(args))

    open("flyctl/flyctl-flyctl-version.txt", "w").write(run("version"))
    help = run("--help")
    open("flyctl/flyctl-help.txt", "w").write(help)

    commands = extract_commands(help)
    for command in commands:
        command_help = run(command, "--help")
        open("flyctl/{}.txt".format(command), "w").write(command_help)
        # Only one nested recursion, I don't think Fly has deeper than that
        subcommands = extract_commands(command_help)
        for subcommand in subcommands:
            subcommand_help = run(command, subcommand, "--help")
            open("flyctl/{}-{}.txt".format(command, subcommand), "w").write(subcommand_help)
