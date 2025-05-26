import subprocess


def test_calculator_operations():
    # Simulate user input and check output
    process = subprocess.run(['python', 'calculator.py'], input="5\n3\n+\n", 
    text=True, capture_output=True)
    assert "5.0 + 3.0 = 8.0" in process.stdout

    process = subprocess.run(['python', 'calculator.py'], input="10\n2\n/\n", 
    text=True, capture_output=True)
    assert "10.0 / 2.0 = 5.0" in process.stdout

    process = subprocess.run(['python', 'calculator.py'], input="7\n0\n/\n", 
    text=True, capture_output=True)
    assert "Cannot divide by zero!" in process.stdout


if __name__ == "__main__":
    test_calculator_operations()
    print("Simple integration tests passed.")