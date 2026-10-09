
from flask import Flask, request, render_template
import joblib

# Load model
Obj = joblib.load('california.joblib')

model = Obj['Model']
columns = Obj['Columns']

app = Flask(__name__)


@app.route('/')
def Main():
    return render_template(
        'index.html',
        columns=columns
    )


@app.route('/predict', methods=['POST'])
def predict():

    Input = []

    try:

        for i in columns:

            val = request.form.get(i)

            if val is None or val.strip() == "":
                return render_template(
                    'index.html',
                    columns=columns,
                    error=f"Please enter a value for {i}"
                )

            Input.append(float(val))

        out = model.predict([Input])

        prediction = out[0]

        return render_template(
            'index.html',
            columns=columns,
            prediction=prediction
        )

    except ValueError:

        return render_template(
            'index.html',
            columns=columns,
            error="Please enter valid numeric values."
        )


if __name__ == "__main__":
    app.run(debug=True)
