**JSON Schema Generation Technical Report** 

This technical report provides an overview and detailed explanation of the JSON Schema Generation program **(main.py)**. The program, implemented in Python, reads a JSON file, sniffs the schema of the JSON data, and generates an output schema in a specific location. The program follows specific instructions and best practices to ensure accurate schema generation.

**Program Overview**
The program **(main.py)** consists of two main functions: sniff_json_schema and generate_schema. The sniff_json_schema function constructs the schema dictionary by assigning attributes for each key in the JSON data. The generate_schema function is responsible for generating the schema for each attribute based on specific instructions for handling data types, arrays, and enums.

**Detailed Explanation**

**1. Reading the JSON File:** The program reads a JSON file located in the ./data/ directory. The file contains the JSON data for which the schema needs to be generated.

**2. Sniffing the JSON Schema:** The sniff_json_schema function processes the JSON data and generates the schema. It iterates over each key in the JSON data and constructs the schema dictionary.

**3. Attribute Generation:** For each attribute in the JSON data, the program determines the attribute's type based on the Python type of its corresponding value. It uses the following mapping:

    - If the value is a string, the attribute type is set as **"string".**
    - If the value is an integer, the attribute type is set as **"integer".**
    - If the value is an array and the elements are strings, the attribute type is set as **"enum".**
    - If the value is an array and the elements are JSON objects, the attribute type is set as **"array".**
    
**4. Schema Attributes:** Each attribute in the schema dictionary includes the following fields:

    - **type:** Represents the data type of the attribute.
    - **tag:** A placeholder for additional information or tags related to the attribute.
    - **description:** A placeholder for a description or explanation of the attribute.
    - **required:** A boolean flag indicating whether the attribute is required or not.
   
**5. Handling Nested Objects:** The program handles nested objects within the JSON data by recursively calling the generate_schema function for each nested attribute.

**6. Excluding "attributes" Key:** The program ensures that only attributes within the "message" key of the input JSON data are considered for schema generation. Attributes within the "attributes" key are excluded.

**7. Output Generation:** The generated schema is dumped into a JSON file located in the ./schema/ directory. The output file follows the specified format with the addition of the tag and description keys for each attribute.


**Software Best Practices**

The program **(main.py)** adheres to software best practices and Python coding standards to ensure readability, maintainability, and robustness. The following practices are followed:

    - Clear and descriptive variable and function names are used to enhance code understanding.
    - Proper indentation and formatting are applied for improved code readability.
    - The code is modularized into separate functions to promote code reusability and maintainability.
    - Appropriate comments are provided to explain the purpose and functionality of key code sections.
    - Error handling mechanisms, such as exception handling, can be implemented to handle potential errors or invalid input cases.


**Unit Testing**

The program **(test_json_schema)** is a separate script, which contains unit tests for validating the functionality of the sniff_json_schema function. The unit tests cover different scenarios, including simple and complex JSON inputs, to ensure the generated schema matches the expected schema.

**Conclusion**

The JSON Schema Generation program **(main.py)** provides a solution for reading a JSON file, sniffing the schema, and generating an output schema file. The program follows specific instructions for handling data types, arrays, and enums. It adheres to software best practices and includes unit tests for robustness. By using this program, users can easily generate accurate JSON schemas based on their input data, facilitating data validation and interoperability.
