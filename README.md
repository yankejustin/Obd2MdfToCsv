# OBD2LogCSV

OBD2LogCSV is an application designed to transform OBD2 MDF file car logs into well-structured, beautiful CSV files. This tool is essential for professionals and enthusiasts in the automotive industry who deal with vehicle data logging and analysis.

## Features

- **Convert MDF to CSV**: Seamlessly convert OBD2 MDF files into easily readable CSV format.
- **Data Integrity**: Ensures that all data from the MDF file is accurately represented in the CSV output.
- **Filtering Options**: Offers options to filter and select specific data parameters for conversion.
- **Batch Processing**: Supports processing multiple files at once, saving time and effort.
- **Docker Integration**: Packaged with Docker, enabling easy setup and execution across different environments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Python (if you want to run the script outside of Docker)

### Installing

1. **Clone the Repository**

git clone https://github.com/yourusername/OBD2LogCSV.git
cd OBD2LogCSV

2. **Build the Docker Container**

docker build -t obd2logcsv .

3. **Run the Container**

docker run -v ${PWD}/data:/app/data obd2logcsv

Replace ${PWD}/data with the path to the directory containing your MDF files.

### Usage

To convert an MDF file to CSV, simply run:

docker run -v ${PWD}/data:/app/data obd2logcsv python convert.py yourfile.mdf

Replace yourfile.mdf with the name of your MDF file.

## Built With

- Docker - Used to containerize the application.
- Python - The core programming language used.

[https://pypi.org/project/asammdf/](ASAM MDF - Measurement Data File Parser)
