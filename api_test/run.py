import pytest
import os
import argparse
import sys
import subprocess

# Ensure the root directory is in the python path to allow imports from other packages
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)

def run_command(command):
    """Helper function to run a shell command and print its output."""
    print(f"\nExecuting command: {' '.join(command)}")
    try:
        subprocess.run(command, check=True, shell=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error executing command: {e}")
        print("Please ensure 'allure' is installed and in your system's PATH.")

def main():
    """Main function to run pytest tests and generate/serve the Allure report."""
    parser = argparse.ArgumentParser(description="Run pytest tests with Allure reporting.")
    parser.add_argument(
        "path",
        nargs="?",
        default=os.path.join(PROJECT_ROOT, "api_test", "tests"),
        help="Path to the test file or directory. Defaults to the 'tests' directory."
    )
    parser.add_argument(
        "--no-serve",
        action="store_true",
        help="Only generate the report, do not open it in the browser."
    )
    cli_args = parser.parse_args()

    test_path = cli_args.path
    allure_results_dir = os.path.join(PROJECT_ROOT, "results", "allure-results")
    allure_report_dir = os.path.join(PROJECT_ROOT, "results", "allure-report")

    print(f"Target test path: {test_path}")
    print(f"Allure results will be saved to: {allure_results_dir}")

    os.makedirs(allure_results_dir, exist_ok=True)

    pytest_args = [
        test_path,
        "-v",
        "--alluredir", allure_results_dir,
        "--clean-alluredir",
    ]

    print(f"\nRunning pytest with arguments: {pytest_args}")
    exit_code = pytest.main(pytest_args)
    print(f"\nPytest finished with exit code: {exit_code}")

    # Generate and serve the Allure report regardless of test outcomes
    print("--- Generating Allure Report ---")
    generate_cmd = [
        "allure", "generate", allure_results_dir,
        "-o", allure_report_dir, "--clean"
    ]
    run_command(generate_cmd)

    if not cli_args.no_serve:
        print("--- Opening Allure Report ---")
        serve_cmd = ["allure", "open", allure_report_dir]
        run_command(serve_cmd)
    else:
        print("Report generated. To view it, run:")
        print(f"  allure open {allure_report_dir}")

if __name__ == "__main__":
    main()
