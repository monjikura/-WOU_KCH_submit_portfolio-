import subprocess

def get_hg_rev(file_path):
    pipe = subprocess.Popen(
        ["hg", "log", "-l", "1", "--template", "{node}", file_path],
        stdout=subprocess.PIPE
        )
    return pipe.stdout.read()