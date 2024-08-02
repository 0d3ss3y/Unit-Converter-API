# Unit-Converter-API

## Overview

The Unit Conversion API allows you to convert between different units of measurement in various categories including length, temperature, area, volume, weight, and time. This API is built using Python and Flask.

## API Endpoints

### 1. Convert

**URL**: `/convert`

**Method**: `GET`

**Description**: Converts a value from one unit to another within a specified category.

**Parameters**:

- `category` (string): The category of conversion (e.g., `length`, `temperature`, `area`, `volume`, `weight`, `time`).
- `unit_from` (string): The unit you are converting from (e.g., `mts`, `celsius`, `sqmts`).
- `unit_to` (string): The unit you are converting to (e.g., `kilomts`, `fahrenheit`, `acre`).
- `value` (number): The numeric value to convert.

**Response**:

- `200 OK`: Returns the converted value.
- `400 Bad Request`: If the provided parameters are invalid.

**Example Request**:

```
GET http://127.0.0.1:5000/convert?category=length&unit_from=mts&unit_to=kilomts&value=100
```

**Example Response**:

```json
{
    "result": 0.1
}
```

## Categories and Units

### Length
- `mts`: Meters
- `kilomts`: Kilometers
- `cmts`: Centimeters
- `millimts`: Millimeters
- `micromts`: Micrometers
- `nanomts`: Nanometers
- `mile`: Miles
- `yard`: Yards
- `foot`: Foot
- `inch`: Inches
- `lightyear`: Light Year

### Temperature
- `celsius`: Celsius
- `kelvin`: Kelvin
- `fahrenheit`: Fahrenheit

### Area
- `sqmts`: Square Meters
- `sqkmts`: Square Kilometers
- `sqcmts`: Square Centimeters
- `sqmmts`: Square Millimeters
- `sqmicromts`: Square Micrometers
- `hectare`: Hectares
- `sqmile`: Square Mile
- `sqyard`: Square Yards
- `sqft`: Square Feet
- `sqinch`: Square Inches
- `acre`: Acres

### Volume
- `cumts`: Cubic Meter
- `cukmts`: Cubic Kilometer
- `cucmts`: Cubic Centimeter
- `cummts`: Cubic Millimeter
- `lts`: Liter
- `mlts`: Millimeter
- `usgallon`: US Gallon
- `usquart`: US Quart
- `uspint`: US Pint
- `uscup`: US Cup
- `usfluidounce`: US Fluid Ounce
- `ustablebspoon`: US Table Spoon
- `usteaspoon`: US Tea Spoon
- `impgallon`: Imperial Gallon
- `impquart`: Imperial Quart
- `imppint`: Imperial Pint
- `impfluidounce`: Imperial Fluid Ounce
- `imptablespoon`: Imperial Table Spoon
- `impteaspoon`: Imperial Tea Spoon
- `cumile`: Cubic Mile
- `cuyard`: Cubic Yard
- `cufoot`: Cubic Foot
- `cuinch`: Cubic Inch

### Weight
- `kgms`: Kilogram
- `gms`: Gram
- `mgms`: Milligram
- `metricton`: Metric Ton
- `longton`: Long Ton
- `shortton`: Short Ton
- `pound`: Pound
- `ounce`: Ounce
- `carrat`: Carrat
- `atomicmass`: Atomic Mass Unit

### Time
- `sec`: Second
- `milisec`: Millisecond
- `microsec`: Microsecond
- `nanosec`: Nanosecond
- `picosec`: Picosecond
- `min`: Minute
- `hour`: Hour
- `day`: Day
- `week`: Week
- `month`: Month
- `year`: Year

## Running the API

To run the API locally:

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install Flask
    ```

3. Run the Flask app:

    ```bash
    python your_api_file.py
    ```

The API will be available at `http://127.0.0.1:5000`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the sections or add more details based on your specific needs or additional features in your API.
