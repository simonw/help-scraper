import pathlib
import re
import subprocess


backspace_re = re.compile(r'(.)\x08')

def apply_backspaces(s):
    return backspace_re.sub('', s)


def extract_commands(s):
    if "AVAILABLE " not in s:
        return []
    lines = s.split("AVAILABLE ")[1].split("SEE ALSO")[0].strip().split('\n')
    commands = [c.split(' o ')[1].strip() for c in lines if ' o ' in c]
    return [c for c in commands if c != "help"]


def fetch_and_save(bits):
    # ("aws",) - saves to aws/index.txt (special case)
    # ("aws", "codestar", "update-user-profile") saves to
    #   aws/codestar/update-user-profile.txt
    if bits == ("aws",):
        filename = "index.txt"
        dir = pathlib.Path("aws")
    else:
        filename = bits[-1] + ".txt"
        dir = pathlib.Path("/".join(bits[:-1]))
    dir.mkdir(parents=True, exist_ok=True)
    s = subprocess.run(list(bits) + ["help"], capture_output=True).stdout.decode("utf-8")
    s = apply_backspaces(s)
    (dir / filename).write_text(s, "utf-8")
    return s


if __name__ == "__main__":
    # Start with aws help
    to_do = [("aws",)]
    done = set()
    while to_do:
        next_bits = to_do.pop()
        print(next_bits)
        s = fetch_and_save(next_bits)
        done.add(next_bits)
        # Extract commands and add them to the list
        for command in extract_commands(s):
            path = tuple(list(next_bits) + [command])
            if path not in done:
                to_do.append(path)
