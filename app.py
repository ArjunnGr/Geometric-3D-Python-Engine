import json
from flask import Flask, jsonify, request, render_template, redirect
from modules.bounding_box import calculate_smallest_bounding_box
from modules.mesh_rotate import rotate_mesh
from modules.mesh_move import move_mesh
from modules.convexity_check import is_convex
from modules.mesh_scale import scale_mesh

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bounding-box', methods=['POST'])
def bounding_box():
    try:
        points_string = request.form.get('points')
        #points = json.loads(points_string)
        if not points_string:
            raise ValueError('No points data provided')

        try:
            points = json.loads(points_string)
        except json.JSONDecodeError:
            raise ValueError('Add Extra Braces, Bad Input Error')

        if not all(len(point) == 3 for point in points):
            raise ValueError('All points must have three coordinates')
        bbox = calculate_smallest_bounding_box(points)
        return render_template('results.html', result={'bbox': bbox})
    except Exception as e:
        return render_template('results.html', result={}, error=str(e))

@app.route('/rotate-mesh', methods=['POST'])
def rotate_mesh_endpoint():
    try:
        mesh_string = request.form.get('mesh')
        if not mesh_string:
            raise ValueError('No mesh data provided')
        try:
            mesh = json.loads(mesh_string)
        except json.JSONDecodeError:
            raise ValueError('Invalid input for mesh, add extra brackets []')
        if not all(isinstance(point, list) and len(point) == 3 for point in mesh):
            raise ValueError('Each mesh point must be a list of three coordinates')
        angle_string = request.form.get('angle')
        if angle_string is None:
            raise ValueError('No angle provided')
        try:
            angle = float(angle_string)
        except ValueError:
            raise ValueError('Angle must be a valid number')
        axis = request.form.get('axis')
        if axis not in {'X', 'Y', 'Z'}:
            raise ValueError('Axis must be one of "X", "Y", or "Z"')
        rotated_mesh = rotate_mesh(mesh, angle, axis)
        return render_template('results.html',result={'rotated_mesh': rotated_mesh})
    except Exception as e:
        return render_template('results.html',result={}, error=str(e))
    

@app.route('/move-mesh', methods=['POST'])
def move_mesh_endpoint():
    try:
        mesh_string = request.form.get('mesh')
        if not mesh_string:
            raise ValueError('No mesh data provided')
        translation_vector_string = request.form.get('translation')
        if not translation_vector_string:
            raise ValueError('No translation vector provided')
        try:
            mesh = json.loads(mesh_string)
        except json.JSONDecodeError:
            raise ValueError('Invalid input for mesh, add extra brackets []')

        if not all(isinstance(point, list) and len(point) == 3 for point in mesh):
            raise ValueError('Each mesh point must be a list of three coordinates')
        try:
            translation_vector = json.loads(translation_vector_string)
        except json.JSONDecodeError:
            raise ValueError('Invalid input for mesh, add extra brackets []')
        if not (isinstance(translation_vector, list) and len(translation_vector) == 3):
            raise ValueError('Translation vector must be a list of three values')

        moved_mesh = move_mesh(mesh, translation_vector)  # Ensure this function is defined correctly
        # Render the results with moved mesh
        return render_template('results.html', result={'moved_mesh': moved_mesh})
    except Exception as e:
        # Handle exceptions
        return render_template('results.html', result = {}, error=str(e))
    

@app.route('/check-convexity', methods=['POST'])
def check_convexity_endpoint():
    try:
        data = request.form.get('polygon')
        if not data:
            raise ValueError("No polygon provided")

        # Attempt to parse the JSON data
        try:
            polygon = json.loads(data)
        except json.JSONDecodeError as json_err:
            raise ValueError(f"Invalid Input Error, Add Brackets []")

        # Validate the polygon format
        if not all(isinstance(point, list) and len(point) == 3 for point in polygon):
            raise ValueError("Each input point must be a list of three coordinates")
        is_convex_flag = is_convex(polygon)
        return render_template('results.html', result={'is_convex': is_convex_flag})
    except ValueError as e:
        return render_template('results.html', result={}, error=str(e))
    except Exception as e:
        return render_template('results.html', result={}, error=str(e))

@app.route('/scale-mesh', methods=['POST'])
def scale_mesh_endpoint():
    try:
        mesh_string = request.form.get('mesh')
        if not mesh_string:
            raise ValueError("No mesh data provided")

        # Attempt to parse the JSON data for mesh
        try:
            mesh = json.loads(mesh_string)
        except json.JSONDecodeError:
            raise ValueError("Invalid format for mesh, add brackets []")

        # Validate the mesh format
        if not all(isinstance(point, list) and len(point) == 3 for point in mesh):
            raise ValueError("Each mesh point must be a list of three coordinates")

        # Attempt to get and convert the scale factor
        scale_factor = request.form.get('scale_factor')
        if not scale_factor:
            raise ValueError("No scale factor provided")

        try:
            scale_factor = float(scale_factor)
        except ValueError:
            raise ValueError("Scale factor must be a number")

        # Get the precision, default to 2 if not provided
        precision = request.form.get('precision', 2)
        if not precision:
            raise ValueError("No precision value provided")
        try:
            precision = int(precision)
        except ValueError:
            raise ValueError("Precision must be an integer")
        scaled_mesh = scale_mesh(mesh, scale_factor, precision)
        
        # Render the results with scaled mesh
        return render_template('results.html', result={'scaled_mesh': scaled_mesh})

    except ValueError as e:
        # Catch and handle the custom ValueError exceptions
        return render_template('results.html', result={},error=str(e))

    except Exception as e:
        # Catch all other exceptions
        return render_template('results.html', result={},error=str(e))

if __name__ == '__main__':
    app.run(debug=True)