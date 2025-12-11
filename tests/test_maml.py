import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rip_validator.validate import validate_maml

if __name__ == "__main__":
  test_cases = [
      "tests/test_data/test_rip_valid_1/catalogue_1.maml",  # Valid 
      "tests/test_data/test_rip_invalid_1/catalogue_1.maml",  # Invalid
      "tests/test_data/test_rip_invalid_1/catalogue_3.maml",  # Invalid
      "tests/test_data/test_rip_invalid_2/catalogue_4.maml",  # Invalid
      "tests/test_data/test_rip_invalid_2/catalogue_5.maml",  # Invalid
      "tests/test_data/test_rip_invalid_2/catalogue_6.maml",  # Invalid
      "tests/test_data/test_rip_invalid_2/catalogue_7.maml",  # Valid
      "tests/test_data/test_rip_invalid_2/catalogue_8.maml",  # Invalid
  ]

  print("Test MAML Validation Results:")
  print("-" * 80)
  for test in test_cases:
      validate_maml(test)
