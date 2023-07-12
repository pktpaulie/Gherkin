from behave import __main__ as behave_executable
from behave_html_formatter import HTMLFormatter

def generate_html_report():
    # Set the output directory for the report
    output_dir = 'reports'

    # Set the formatter to HTMLFormatter
    formatter = HTMLFormatter(directory=output_dir)

    # Run Behave with the formatter
    behave_executable.main(['-f', formatter])

generate_html_report()