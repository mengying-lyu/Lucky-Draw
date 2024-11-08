# Lucky Draw App (Dorothy Draw 🎉)

Dorothy Draw is a Python-based lottery application that allows users to manage participant information, import data from Excel files, and conduct random draws to select winners. The application is built using `Tkinter` for its graphical user interface and `pandas` for handling Excel file imports.

## Features
1. *Add Participants Manually*: Users can add participants' names and student IDs through the app interface.
2. *Bulk Import Participants*: Load participant data from Excel files with predefined columns (`Name` and `ID`).
3. *Display Participant List*: View the list of all participants in the system.
4. *Random Winner Selection*: Select a random winner from the participant list and display their details.
5. *Simple and User-Friendly Interface*: Designed with an intuitive layout for easy interaction.

## Installation
1. Clone this repository or download the code files

2.	Install the required Python packages:

```pip install pandas```

```pip install tkinter```


3.	Ensure you have Python 3 installed on your system.

## Usage

1.	Run the main code in PyCharm


2.	Use the application interface:
- Insert New One: Add participant details manually.
- Insert Excel File: Import participants in bulk by selecting an Excel file with columns Name and ID.
- Draw: Randomly select a winner and display their details.

## File Structure

`main.py`: Main Python script for running the application.
Excel file must include two columns:
- Name: Participant’s name.
- ID: Participant’s student ID.


## Dependencies

- Python 3
- Tkinter (included with Python)
- pandas (pip install pandas)
