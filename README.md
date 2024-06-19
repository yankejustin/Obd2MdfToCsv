# Obd2MdfToCsv

Obd2MdfToCsv is an application designed to transform OBD2 MDF file car logs into well-structured, beautiful CSV files. This tool is essential for professionals and enthusiasts in the automotive industry who deal with vehicle data logging and analysis.

## Features

- **Convert MDF to CSV**: Seamlessly convert OBD2 MDF files into an easily readable CSV format.
- **Data Integrity**: Ensures that all data from the MDF file is accurately represented in the CSV output.
- **Filtering Options**: Offers options to filter and select specific data parameters for conversion.
- **Batch Processing**: Supports processing multiple files at once, saving time and effort.
- **Docker Integration**: Packaged with Docker, enabling easy setup and execution across different environments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- [Docker](https://docs.docker.com/desktop/install/windows-install/) (for Windows users)
- [Python](https://www.python.org/) (if you want to run the script outside of Docker)

### Installing

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yankejustin/Obd2MdfToCsv.git
    cd Obd2MdfToCsv
    ```

2. **Build the Docker Container**

    ```bash
    docker build -t obd2mdftocsv .
    ```

### Usage

To convert an MDF to CSV with column name changing and data modification:

    ```bash
    docker run -v ${PWD}/data:/app/data obd2mdftocsv python app.py data/input.mdf data/output.csv
    ```

For example, if you place `input.mdf` inside the `data` directory, you can run the container like this:

    ```bash
    docker run -v /path/to/Obd2MdfToCsv/data:/app/data obd2mdftocsv python app.py /app/data/input.mdf
    ```

> **Note:** Replace `/path/to/Obd2MdfToCsv` with the actual path to where you cloned the repository.

## Built With

- [Docker](https://www.docker.com/) - Used to containerize the application.
- [Python](https://www.python.org/) - The core programming language used.
- [MDF Standard Reference](https://www.asam.net/standards/detail/mdf) - Standard for MDF files.
- [ASAM MDF](https://pypi.org/project/asammdf/) - Measurement Data File Parser - Used for parsing MDF files.

## Updating the Code

To bring the latest changes from GitHub to your machine:

1. **Pull the latest code**:

    ```bash
    cd /path/to/Obd2MdfToCsv
    git pull origin main
    ```

2. **Rebuild the Docker image**:

    ```bash
    docker build -t obd2mdftocsv .
    ```

3. **Run the Docker container**:

    ```bash
    docker run -v /path/to/Obd2MdfToCsv/data:/usr/src/app/data obd2mdftocsv /usr/src/app/data/input.mdf
    ```

> **Note:** The `OptionalFilePathForInput` parameter can be excluded entirely, and it will default to the local path and file: `/Obd2MdfToCsv/data/input.mdf`
