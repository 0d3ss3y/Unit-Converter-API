from flask import Flask, request,jsonify

app = Flask(__name__)

def convert_length(value, from_unit, to_unit):
    length_units = {
        'mts': 1,
        'kilomts': 1000,
        'cmts': 0.01,
        'millimts': 0.001,
        'micromts': 1e-6,
        'nanomts': 1e-9,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'lightyear': 9.461e15
    }
    return value*(length_units[from_unit]/length_units[to_unit])


def convert_temperature(value, from_unit, to_unit):
    match from_unit:
        case 'celsius':
            if to_unit == 'fahrenheit':
                return value * 9/5 + 32
            elif to_unit == 'kelvin':
                return value + 273.15
        
        case 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * 5/9
            elif to_unit == 'kelvin':
                return (value - 32) * 5/9 + 273.15
            
        case 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            elif to_unit == 'fahrenheit':
                return (value - 273.15) * 9/5 + 32
            

def convert_area(value, from_unit, to_unit):
    area_units = {
       'sqmts': 1, 
       'hectare': 1e4,
       'sqmile': 2.58999e6,
       'sqft' : 0.092903,
       'acre' : 4046.86
    }
    return (value * (area_units[from_unit] / area_units[to_unit]))


def convert_volume(value, from_unit, to_unit):
    volume_units ={
        'lts': 0.001,
        'mlts': 1e-6,
        'usgallon': 3.78541,
        'uscup': 0.236588
    }

    return value * (volume_units[from_unit] / volume_units[to_unit])


def convert_weight(value, from_unit, to_unit):
    weight_unit = {
        'kgms': 1,
        'gms': 1e-3,
        'mgms': 1e-6,
        'pound': 0.453592,
        'ounce': 0.0283495,
        'carrat': 2e-4
    }


def convert_time(value, from_unit, to_unit):
    time_units = {
        'sec': 1,
        'milisec': 1e-3,
        'microsec': 1e-6,
        'nanosec': 1e-9,
        'picosec': 1e-12,
        'min': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2592000, 
        'year': 31536000
    }
    return value * (time_units[from_unit] / time_units[to_unit])


@app.route('/convert',methods = ['GET'])
def convert():
    category = request.args.get('category')
    unit_from = request.args.get('unit_from')
    unit_to = request.args.get('unit_to')
    value = float(request.args.get('value'))

    match category:
        case 'length':
            result = convert_length(value,unit_from,unit_to)
        case 'temperate':
            result = convert_temperature(value,unit_from,unit_to)
        case 'area':
            result = convert_area(value,unit_from,unit_to)
        case 'volume':
            result = convert_volume(value,unit_from,unit_to)
        case 'weight':
            result = convert_weight(value,unit_from,unit_to)
        case 'time':
            result = convert_time(value,unit_from,unit_to)
        case _:
            return jsonify({'error': 'Invalid category requested'}), 400
    
    return jsonify({"result":result})


if __name__ == '__main__':
    app.run(debug=True)