if __name__ == "__main__":
    s = open("azure/azure-help.txt").read()
    commands = []
    lines = s.split("Subgroups:")[1].strip().split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split("\t")[0]
        
        if ":" in lines[i]:
            temp = lines[i].split(":")[0]
            commands.append(temp.strip().split(" ")[0])
    #print(commands)

    for command in commands:
        if command not in ["To","Commands","Core"]:
            print(
                "az {command} --help > azure/{command}.txt".format(
                    command=command
                )
            )
