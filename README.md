# Satisfactory Loot Maps
This python program generates Satisfactory Loot Maps using CSV data on crash sites and loot around the crash sites

## Example Satisfactory Maps

### Unique Items

### Each Item Stack

## How To Download And Run
### Cloning Repo
```sh
git clone https://github.com/klforthwind/SatisfactoryLootMaps.git
```

### Install Instructions
```sh
cd SatisfactoryLootMaps

sudo pip3 install -r requirements.txt
```

### Running The Code
```sh
python3 main.py
```

## Code Structure
### SatisfactoryLootMaps
```
.
├── data                    # CSV files containing crash site data
├── final                   # Final images of generated loot maps
├── img                     # Image files for README.md
├── imgs                    # Image files for SatisfactoryLootMaps program
├── data.py                 # Data File - handles data transformation and reading from CSV files
├── graphics.py             # Graphics File - handles Matplotlib drawing / drawing functions
├── main.py                 # Main file that handles the interaction between other python files
└── README.md
```

## Software Design
![](img/SatisfactoryLootMaps_FileStructure.png)
