# Obd2MdfToCsv

Obd2MdfToCsv is an application designed to transform OBD2 MDF file car logs into well-structured, beautiful CSV files. This tool is essential for professionals and enthusiasts in the automotive industry who deal with vehicle data logging and analysis.

## Features

    Convert MDF to CSV: Seamlessly convert OBD2 MDF files into easily readable CSV format.
    Data Integrity: Ensures that all data from the MDF file is accurately represented in the CSV output.
    Filtering Options: Offers options to filter and select specific data parameters for conversion.
    Batch Processing: Supports processing multiple files at once, saving time and effort.
    Docker Integration: Packaged with Docker, enabling easy setup and execution across different environments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Docker (for Windows users: https://docs.docker.com/desktop/install/windows-install/)
- Python (if you want to run the script outside of Docker)

### Installing

1. **Clone the Repository**

git clone https://github.com/yankejustin/Obd2MdfToCsv.git
cd Obd2MdfToCsv

2. **Build the Docker Container**

docker build -t obd2mdftocsv .

3. **Run the Container**

docker run -v ${PWD}/data:/app/data obd2mdftocsv

Replace ${PWD}/data with the path to the directory containing your MDF files.

### Usage

To convert an MDF to CSV with column name changing and data modification:
docker run -v ${PWD}/data:/app/data obd2mdftocsv python app.py data/input.mdf data/output.csv

For example, if you place input.mdf inside the data directory, you can run the container like this:

docker run -v YourLocalDirectoryToWhereYouClonedIt\Obd2MdfToCsv\data:/app/data obd2mdftocsv python app.py /app/data/input.mdf

## Built With

    [Docker](https://www.docker.com/) - Used to containerize the application.
    [Python](https://www.python.org/) - The core programming language used.
    [ASAM MDF](https://www.asam.net/standards/detail/mdf) - Standard for MDF files.
    [ASAM MDF](https://pypi.org/project/asammdf/) - Measurement Data File Parser - Used for parsing MDF files.

## What to do after I update the code

pull latest code

cd YourLocalDirectoryToWhereYouClonedIt\Obd2MdfToCsv
git pull origin main

rebuild the docker image
docker build -t obd2mdftocsv .

run the docker container
docker run -v YourLocalDirectoryToWhereYouClonedIt\Obd2MdfToCsv\data:/usr/src/app/data obd2mdftocsv /usr/src/app/data/input.mdf
