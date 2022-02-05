import pathlib
import subprocess


def extract_commands(s):
    if "Commands:" not in s:
        return []
    # Need everything between "Commands:" and "Options:"
    text = s.split("Commands:")[1].split("Options:")[0]
    # Every line with more than one token in represents a sub-command
    # - this excludes the Basic and Advanced headings on "vercel --help"
    commands = [
        l.strip().split()[0] for l in text.split("\n") if len(l.strip().split()) > 1
    ]
    # vercel login --help starts an interactive process, so skip it
    # Skip vercel deploy because it is alias of vercel
    return [c for c in commands if c not in ("help", "login", "deploy")]


def fetch_and_save(bits, previous_content=None):
    previous_content = previous_content or set()
    if bits == ("vercel",):
        filename = "index.txt"
        dir = pathlib.Path("vercel")
    else:
        filename = bits[-1] + ".txt"
        dir = pathlib.Path("/".join(bits[:-1]))
    args = list(bits) + ["--help"]
    print(args)
    proc = subprocess.run(args, capture_output=True)
    s = proc.stderr.decode("utf-8")
    if proc.stdout:
        # Use that instead, if provided
        s = proc.stdout.decode("utf-8")
    if s in previous_content:
        # Avoid storing duplicates
        return None
    dir.mkdir(parents=True, exist_ok=True)
    print(dir, filename)
    (dir / filename).write_text(s, "utf-8")
    return s


if __name__ == "__main__":
    to_do = [("vercel",)]
    done = set()
    previous_content = set()
    while to_do:
        next_bits = to_do.pop()
        print(next_bits)
        s = fetch_and_save(next_bits, previous_content)
        done.add(next_bits)
        if s is None:
            continue
        previous_content.add(s)
        # For index page, extract commands and add them to the list
        if next_bits == ("vercel",):
            for command in extract_commands(s):
                path = tuple(list(next_bits) + [command])
                print("  ", path)
                if path not in done:
                    to_do.append(path)
