# Snap-hook Calculator App

This repository contains a Python application for calculating various parameters related to snap-hooks. Snap-hooks are commonly used in various industries for fastening purposes. This application provides a user-friendly interface to input snap-hook parameters and obtain calculated results.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Snap-hook Types](#snap-hook-types)
- [Formulas](#formulas)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Snap-hook Calculator App is a desktop application developed using Python's tkinter library. It allows users to select different types of snap-hooks from a dropdown menu, input specific parameters related to the selected snap-hook type, and calculate various properties such as allowable snap deflection and deflection force.

## Features
- User-friendly GUI.
- Dropdown menu for selecting snap-hook type.
- Display of snap-hook images and section images.
- Input fields for entering parameters.
- Calculation of snap-hook properties based on selected type and entered parameters.
- Help tables for detailed information on certain snap-hook types.
- Error handling for invalid input values.

## Installation
To run the Snap-hook Calculator App, follow these steps:
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/cristib01/snap-hook_calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd snap-hook-calculator
    ```
3. Run the application:
    ```bash
    python snap_hook_calculator.py
    ```

## Usage
Upon launching the application, you'll be presented with a graphical user interface. Follow these steps to use the application effectively:
1. Select a snap-hook type from the dropdown menu.
2. Optionally, click on the "Display information" button to view details about the selected snap-hook type.
3. Input values for the parameters displayed based on the selected snap-hook type.
4. Click on the "Calculate" button to obtain calculated results.
5. View the calculated properties displayed in the result label.

## Snap-hook Types
The Snap-hook Calculator App supports various types of snap-hooks, including:
- Improved - Rectangular Types
- L Beam
- U Beam Case 1 & 2
- Classic - Ring segment
- Classic - Trapezoid
- Classic - Irregular
Each snap-hook type has specific parameters and formulas associated with it.

## Formulas
The application utilizes specific formulas to calculate snap-hook properties based on the selected type and entered parameters. These formulas are defined in the codebase and are specific to each snap-hook type.

## Contributing
Contributions to the Snap-hook Calculator App are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

