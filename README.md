# Report-Generation-Sensor
Automated Sensor Reporting System

A Python automation project built to practice and reinforce concepts related to task scheduling, report generation, logging, command-line interfaces, and data processing.

Rather than being a production application, this project serves as a hands-on learning exercise that combines multiple Python libraries into a complete automated reporting pipeline.

Project Overview

The application periodically reads sensor data from a CSV file, validates and processes the data, generates an HTML report using a Jinja2 template, converts the report into a PDF document, and repeats the entire process automatically using a scheduler.

The primary objective of this project was to understand how multiple independent Python libraries can work together to build an automated workflow similar to those found in industrial software.

Features
Automated report generation using scheduled tasks
Command-line interface using argparse
Structured logging with Python's logging module
CSV data processing with pandas
HTML report generation using Jinja2
PDF generation from HTML
Input validation and error handling
Automatic report creation at user-defined intervals
Organized project structure for maintainability

Concepts Practiced

This project was created to strengthen understanding of the following Python topics:

Task Scheduling (schedule)
Command-Line Arguments (argparse)
Logging and Debugging
File Handling
Path Management (pathlib)
CSV Processing (pandas)
HTML Templating (Jinja2)
HTML to PDF Conversion
Validation and Error Handling
Modular Program Design

Technologies Used
Python 3.13.1
pandas
schedule
Jinja2
pdfkit
pathlib
logging
argparse

Project Workflow
Sensor CSV
      │
      ▼
Input Validation
      │
      ▼
Data Cleaning
      │
      ▼
HTML Report (Jinja2)
      │
      ▼
PDF Generation
      │
      ▼
Saved Report
      │
      ▼
Scheduler waits until next interval

Running the Project

Install the required packages:

pip install pandas schedule jinja2 pdfkit

Run the application:

python automation.py --input sensors.csv --output reports --interval 60

Example:

python automation.py --input sensor_data.csv --output reports --interval 30

This generates a report every 30 minutes.

Example Output

The generated report contains:

Report title
Report timestamp
Sensor statistics
Tabulated sensor readings
Summary section

For the generated output to be generated without any error create a report folder with 3 subfolders excels, htmls, and pdfs. And each report will be generated in their respective folders.

Purpose

This project was developed as part of my Python learning roadmap to reinforce newly learned concepts through practical implementation.

Instead of learning each library independently, the goal was to integrate them into a realistic engineering automation workflow.
