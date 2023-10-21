# SCD-30 Carbon Dioxide (CO2) Sensor

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Provide a brief introduction to the SCD-30 and SHT31 Carbon Dioxide (CO2) Sensor. Explain what this sensor is used for and its significance.

## Features

- **Power Supply Voltage:** Operates on 3.3V - 5.5V.
- **NDIR CO2 Sensor Technology:** Utilizes Non-Dispersive Infrared (NDIR) technology for accurate CO2 measurements.
- **Integrated Temperature and Humidity Sensor:** Includes a built-in sensor for temperature and humidity readings.
- **Dual-Channel Detection:** Provides dual-channel CO2 detection for superior stability and precision.
- **Compact Form Factor:** Compact dimensions measuring 35 mm x 23 mm x 7 mm.
- **Measurement Range:** Capable of measuring CO2 levels within the range of 400 ppm to 10,000 ppm.
- **Accuracy:** Offers a high level of accuracy with a specification of ±(30 ppm + 3%).
- **Low Current Consumption:** Operates with a low current consumption of 19 mA at a measurement rate of 1 per 2 seconds.
- **Energy Efficiency:** Designed for energy efficiency, consuming only 120 mJ per measurement.
- **Fully Calibrated and Linearized:** Sensor data is fully calibrated and linearized for precise readings.
- **Digital Interface:** Provides the option of digital communication through UART or I2C.



## Getting Started

Explain how to get started with the SCD-30 and SHT31 sensor. This section should cover any prerequisites and installation instructions.

### Prerequisites

List any prerequisites or dependencies that users need before they can use the sensor. For example, if they need specific hardware, libraries, or software.

### Installation

Provide step-by-step installation instructions, including how to physically connect the sensor and how to set it up with any required software.

## Usage

Show examples of how to use the sensor. You can include code snippets, diagrams, and explanations to help users understand how to work with the sensor.

```python
# Example code to read data from the sensor
import sensor_library

sensor = sensor_library.SCD30()
data = sensor.read_data()
print(data)

```

![CO2 Data](co2_data.jpeg)
