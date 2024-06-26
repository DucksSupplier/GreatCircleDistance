# Great Circle Distance Visualizer
Welcome to the Great Circle Distance Visualizer, a web application that helps you visualize and calculate the shortest path between two points on the surface of a sphere, such as the Earth. This application uses Leaflet for 2D map visualization and Cesium for 3D globe visualization, allowing users to interact with both views.

## Features
* Interactive 2D and 3D Maps: Visualize points and paths on both a 2D map (Leaflet) and a 3D globe (Cesium).

* Drag-and-Drop Markers: Easily move markers on the map to dynamically update the path.

* Geodesic Path Calculation: Display the shortest path over the globe's surface (great circle distance).

* Distance Calculation: Calculate the great circle distance between two points and display the result.

## Installation
### Prerequisites
* Python 3.x
* Flask
* Geopy
* Flask-CORS
* A web browser (latest version of Chrome, Firefox, Safari, or Edge)

### Steps

1. Clone the Repository:

```
git clone https://github.com/DucksSupplier/GreatCircleDistance.git
cd path to repository
```

2. Install the Required Python Packages:

```
pip install flask geopy flask-cors
```

3. Run the Flask Application:

```
python app.py
```

4. Open Your Web Browser:
Go to http://127.0.0.1:5000 to view the application.

## Usage

1. Add Markers:
  Click on the 2D map or 3D globe to add a marker.
  Add at least two markers to calculate and visualize the path.

2. Move Markers:
  Drag markers on the 2D map to update their positions.

3. View Path:
  The path between the two markers will be displayed on both the 2D map and 3D globe.

4. Calculate Distance:
  The distance between the two markers will be calculated and displayed.
