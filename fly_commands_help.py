if __name__ == "__main__":
    s = open("flyctl/flyctl-help.txt").read()
    lines = s.split("Commands:")[1].split("\n\nFlags:")[0].strip().split("\n")
    commands = [l.strip().split()[0] for l in lines]
    for command in commands:
        print(
            "~/.fly/bin/flyctl {command} --help > flyctl/{command}.txt".format(
                command=command
            )
        )
