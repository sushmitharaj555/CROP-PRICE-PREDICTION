from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained machine learning model
model = joblib.load('model.pkl')  # Replace 'model.pkl' with the path to your model file

@app.route('/')
def home():
    return render_template('ml_project.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    try:
        year = int(request.form['year'])
        area = float(request.form['area'])
        cropType = request.form['cropType']
        season_rabi = bool(request.form.get('season_rabi'))
        season_kharif = bool(request.form.get('season_kharif'))
        season_summer = bool(request.form.get('season_summer'))
        season_whole_year = bool(request.form.get('season_whole_year'))

        # Convert season checkboxes to integers
        season_rabi = int(season_rabi)
        season_kharif = int(season_kharif)
        season_summer = int(season_summer)
        season_whole_year = int(season_whole_year)

        # Perform prediction using your model
        prediction = model.predict([[year, area, season_rabi, season_kharif, season_summer, season_whole_year]])

        # Render the ml_project.html template with the prediction
        return render_template('ml_project.html', prediction=prediction)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('ml_project.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)


