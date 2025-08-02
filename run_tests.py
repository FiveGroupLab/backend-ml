#!/usr/bin/env python3
"""
Test runner script for the hypertension prediction API.
"""

import subprocess
import sys
from pathlib import Path


def run_tests():
    """Run the test suite and display results."""
    print("🧪 Running Hypertension Prediction API Tests")
    print("=" * 50)
    
    # Change to project directory
    project_dir = Path(__file__).parent
    
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "-v", 
            "--tb=short",
            "tests/"
        ], cwd=project_dir, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print("\n✅ All tests passed!")
        else:
            print(f"\n❌ Tests failed with return code {result.returncode}")
            
        return result.returncode
        
    except FileNotFoundError:
        print("❌ pytest not found. Please install it with: pip install pytest pytest-asyncio")
        return 1
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)