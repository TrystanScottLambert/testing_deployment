import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rip_validator.validate import validate_maml_and_parquet

if __name__ == "__main__":
  test_cases = [
      "tests/test_data/test_rip_invalid_4/illegal_column_names", # Invalid 
      "tests/test_data/test_rip_invalid_ra_dec_max/invalid_max_ra_dec", # Invalid 
      "tests/test_data/test_rip_invalid_ra_dec_min/invalid_min_ra_dec", # Invalid 
      "tests/test_data/test_rip_invalid_max/invalid_column_max", # Invalid 
      "tests/test_data/test_rip_invalid_min/invalid_column_min", # Invalid 
  ]

  print("Test MAML-Parquet Validation Results:")
  print("-" * 80)
  for test in test_cases:
      print("-" * 80)
      print(f"Testing file {test}:")
      print("-" * 80)
      validate_maml_and_parquet(test, print_output=True, verbose=True)
