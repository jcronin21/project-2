import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode(), process.returncode

def check_code_quality():
    # Run Black
    black_output, black_error, black_returncode = run_command("black --check .")
    if black_returncode != 0:
        print("Black failed with the following error:")
        print(black_error)
        return False

    # Run isort
    isort_output, isort_error, isort_returncode = run_command("isort . --check-only")
    if isort_returncode != 0:
        print("isort failed with the following error:")
        print(isort_error)
        return False

    # Run Flake8
    flake8_output, flake8_error, flake8_returncode = run_command("flake8")
    if flake8_returncode != 0:
        print("Flake8 failed with the following error:")
        print(flake8_error)
        return False

    print("All checks passed successfully!")
    return True

if __name__ == "__main__":
    if not check_code_quality():
        exit(1)



##chat gpt made this whole test because I wasnt sure where to start