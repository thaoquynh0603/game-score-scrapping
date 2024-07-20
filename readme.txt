
# Game Score Scrapping

## Introduction
Game Score Scrapping is a Python-based project designed to extract and compile game scores from various gaming websites. The primary goal is to convert a dataset of game titles from a PDF file into a comprehensive dataset containing game scores and source links.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/thaoquynh0603/game-score-scrapping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd game-score-scrapping
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the input PDF (containing game titles) in the project directory.
2. Run the `convert_pdf.ipynb` notebook to convert the PDF into a dataset.
3. Execute the scraping scripts (`gamespot.py`, `ign.py`, `metacritic.py`) to fetch game scores.
4. Combine the results using `combine.py`.

## Features
- Convert PDF of game titles to a pandas DataFrame.
- Scrape game scores from GameSpot, IGN, and Metacritic.
- Generate a final dataset with game titles, scores, and source links.

## Dependencies
- Python 3.x
- Pandas
- BeautifulSoup4
- Requests

## Configuration
- Ensure the PDF file is named correctly as per the script requirements.
- Update the scraping scripts if necessary to match any changes in the website structures.

## Documentation
- `convert_pdf.ipynb`: Notebook for converting PDF to dataset.
- `gamespot.py`, `ign.py`, `metacritic.py`: Scripts for scraping game scores.
- `combine.py`: Script to merge the scraped data into a single dataset.

## Examples
- Input PDF: `Creative-Arcades-6296.pdf`
- Output CSV: `finalgamespot.csv`, `finalign.csv`, `finalmetacritic.csv`, `data.csv`

## Troubleshooting
- Ensure all dependencies are installed.
- Check for updates in the website structure if scraping fails.
- Verify the format of the input PDF.

## Contributors
- [thaoquynh0603](https://github.com/thaoquynh0603)

## License
This project is licensed under the MIT License.

---

Feel free to adjust or expand upon this template as needed!
