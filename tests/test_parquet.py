import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rip_validator.validate import validate_parquet

if __name__ == "__main__":
  test_cases = [
      "tests/test_data/test_rip_valid_1/catalogue_1.parquet",  # Valid 
      "tests/test_data/test_rip_invalid_1/catalogue_1.parquet",  # Valid
      "tests/test_data/test_rip_invalid_1/catalogue_2.parquet",  # Valid
  ]

  print("Test Parquet Validation Results:")
  print("-" * 80)
  for test in test_cases:
      print(validate_parquet(test))
