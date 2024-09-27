import pytest

# Mock get_config_details function called at module level
def get_config_details():
    return {"password": "1234", "host": "testhost", "port": "testport"}

def test_process_data_from_source_high_priority(mocker):
    # Apply the patches
    mocker.patch("hashicorp_poc.get_config_details",
                 return_value={"password": "1234", "host": "testhost", "port": "testport"})
    mocker.patch("tasks.can_execute", return_value=True)
    mocker.patch("tasks.redis_client")
    mocker.patch("tasks.process_data", return_value=1)

    # Import the function to test after patching
    from tasks import process_data_from_source_high_priority

    # Call the function and assert the expected result
    result = process_data_from_source_high_priority("script_code", "function_name", 1, 2, 3)
    assert result == 1

def test_process_data_from_source_normal_priority(mocker):
    # Apply the patches
    mocker.patch("hashicorp_poc.get_config_details",
                 return_value={"password": "1234", "host": "testhost", "port": "testport"})
    mocker.patch("tasks.can_execute", return_value=True)
    mocker.patch("tasks.redis_client")
    mocker.patch("tasks.process_data", return_value=1)

    # Import the function to test after patching
    from tasks import process_data_from_source_normal

    # Call the function and assert the expected result
    result = process_data_from_source_normal("script_code", "function_name", 1, 2, 3)
    assert result == 1