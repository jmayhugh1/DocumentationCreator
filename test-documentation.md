# Title
Code Documentation

# Introduction
This document provides documentation for the code written in the given  file.

# Usage
This code is written to retrieve memory information from a specific EC2 instance and publish it as a CloudWatch metric.

# Dependencies
The code requires the following dependencies:
- [json](https://docs.python.org/3/library/json.html): The json module provides functionality for working with JSON data.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): Boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of Amazon services like Amazon S3, Amazon EC2, etc.
- [time](https://docs.python.org/3/library/time.html): The time module provides various time-related functions.
- [re](https://docs.python.org/3/library/re.html): The re module provides support for regular expressions.

# Functionality
The code consists of two main functions: `analyzeResult` and `lambda_handler`.

The `analyzeResult` function takes in a result string, instanceId, and instanceName as input. It uses regex to extract the memory usage from the result and returns it.

The `lambda_handler` function is the entry point of the code and is executed when the Lambda function is triggered. It initializes the AWS clients for CloudWatch, EC2, and SSM. It retrieves the instanceId and instanceName from the event payload. It then sends a command using SSM to retrieve memory usage information from the specified EC2 instance. It waits for the command to complete and retrieves the command output. If the output contains memory usage information, it calls the `analyzeResult` function to extract the memory usage and publishes it as a CloudWatch metric. If the output is empty, it indicates that the WebStoreWS.exe is not running.

# Input
The `lambda_handler` function expects an event payload containing the following attributes:
- instanceId: The ID of the EC2 instance from which memory usage information needs to be retrieved.
- instanceName: The name of the EC2 instance.

The event payload should be in the following format:
```python
{
    "instanceId": "i-1234567890abcdef0",
    "instanceName": "ExampleInstance"
}
```
Note: The actual values for instanceId and instanceName may vary depending on the specific EC2 instance you want to monitor.

# Output