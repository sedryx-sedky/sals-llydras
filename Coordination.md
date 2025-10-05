# Llydras Project Coordination Document

## Introduction

This document serves as our central reference for technical setup, coding standards, and project coordination. The goal is to ensure we can work on each other's code seamlessly and avoid common integration issues. This is not a static document—please contribute your suggestions and expertise as we refine our workflow.

---

## Technical Setup

### Required Python Modules

1. __numpy__ - Numerical computing

2. __pandas__ - Data manipulation and analysis

3. __yfinance__ - Financial data retrieval

### Coding Conventions

To ensure interoperability and readability of each other's code, let us adopt the following conventions amongst ourselves.

1. __Indentation__

Use four spaces (not tabs) for Python indentation to prevent `IndentationError` which occurs when tabs and spaces are mixed within the same file.

2. __Type Annotations__

Please use Python's type hints where appropriate to improve code clarity and catch errors early.

3. __File Headers__

Include a docstring at the top of each file with a brief description of its purpose.

Example:
```python
"""
Data processing utilities for financial time series analysis.
"""
```

4. __Code Style__

Use __snake_case__ for functions and variables

Use __CamelCase__ for classes

Avoid excessive comments or overly long docstrings. Well-named functions with clear signatures often need minimal explanation.
---

## Testing

Please write unit tests for your code and save them in the *Tests* folder. Untested code should not be pushed to the repository—this helps us catch issues early and maintain code quality.

---

## Final Notes

Thank you for reading this. While these conventions help us collaborate effectively, the main objective is to have fun and enjoy building something together. Feel free to discuss or object to anything in this document in the WhatsApp group chat—nothing is set in stone.

Let's make this project something we're all proud of!
