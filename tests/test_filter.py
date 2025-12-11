import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rip_validator.filter_check import check_filter
from rip_validator.status import State, Status

if __name__ == "__main__":
  test_cases = [
      "FUV_GALEX",  # Valid - exact match
      "fuvGALEX",  # Invalid - wrong case, missing underscore
      "filterFUVgalex",  # Invalid - prefix + wrong case
      "FuvGalex",  # Invalid - camelCase
      "GALEXfuv",  # Invalid - reordered
      "galex_fuv",  # Invalid - wrong case, reordered
      "fuv_galex",  # Invalid - wrong case
      "filtW1WISE",  # Invalid - prefix + wrong format
      "bandW1Wise",  # Invalid - prefix + camelCase
      "FUV_GALEX_test",  # Valid - doesn't match any filter
      "my_custom_filter",  # Valid - doesn't match any filter
      "u_SDSS",  # Valid - exact match
      "uSDSS",  # Invalid - missing underscore
      "SDSS_u",  # Invalid - reordered
      "Band7ALMA",  # Invalid - missing underscore
      "filterBand7Alma",  # Invalid - prefix + wrong case
      "mag_err_VISTA_Z",  # Invalid - should be Z_VISTA
      "VISTA_Z",  # Invalid - reordered
      "flux_Z_VISTA",  # Valid - correct filter in compound name
  ]

  print("Filter Validation Results:")
  print("-" * 80)
  for test in test_cases:
      filter_status = check_filter(test)
      status = "✓ VALID" if filter_status.state == State.PASS else "✗ VIOLATION"
      correction = f" → Use: {filter_status.message}" if filter_status.message else ""
      print(f"{status:12} | '{test:25}'{correction}")

  # Test snake_case validation
  print("\n" + "=" * 80)
  print("Snake Case Validation Results:")
  print("-" * 80)

  snake_case_tests = [
      "my_variable_name",  # Valid snake_case
      "filter_data_v2",  # Valid snake_case
      "myVariableName",  # Invalid - camelCase
      "MyVariableName",  # Invalid - PascalCase
      "my-variable-name",  # Invalid - kebab-case
      "_leading_underscore",  # Invalid - leading underscore
      "trailing_underscore_",  # Invalid - trailing underscore
      "double__underscore",  # Invalid - consecutive underscores
      "UPPERCASE_NAME",  # Invalid - uppercase
      "mix_Case_name",  # Invalid - mixed case
      "number123_test",  # Valid - contains numbers
      "123number",  # Valid - starts with number
      "just_underscores_",  # Invalid - trailing underscore
      "simple",  # Valid - single word lowercase
  ]
