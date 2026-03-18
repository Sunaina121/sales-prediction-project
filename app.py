 from flask import Flask, render_template, request
import pickle
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        tv = float(request.form['TV'])
        radio = float(request.form['Radio'])
        newspaper = float(request.form['Newspaper'])

        prediction = model.predict([[tv, radio, newspaper]])
        output = round(prediction[0], 2)

        # Graph
        import matplotlib.pyplot as plt
        plt.figure()
        plt.scatter(tv, output, color='red', label="Prediction")
        plt.xlabel("TV Budget")
        plt.ylabel("Sales")
        plt.title("Sales Prediction Graph")
        plt.legend()
 graph_path = os.path.join('static', 'dynamic_graph.png')
        plt.savefig(graph_path)
        plt.close()

        return render_template(
            "index.html",
            prediction_text=f"Predicted Sales: {output}",
            show_graph=True,
            graph_image="dynamic_graph.png"
        )

    except:
        return render_template(
            "index.html",
            prediction_text="Invalid input! Please enter numeric values only.",
            show_graph=False
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
