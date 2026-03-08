from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    tv = float(request.form['TV'])
    radio = float(request.form['Radio'])
    newspaper = float(request.form['Newspaper'])

    prediction = model.predict([[tv, radio, newspaper]])

    output = round(prediction[0], 2)
    import matplotlib.pyplot as plt

# Create dynamic graph
    plt.figure()
    plt.scatter(tv, prediction[0], color='red', label="Predicted Value")
    plt.scatter(tv, model.predict([[tv, radio, newspaper]]), color='blue')
    plt.xlabel("TV Budget")
    plt.ylabel("Sales")
    plt.legend()

    graph_path = "static/dynamic_graph.png"
    plt.savefig(graph_path)
    plt.close()  

    return render_template(
    "index.html",
    prediction_text="Predicted Sales: {}".format(output),
    show_graph=True,
    graph_image="dynamic_graph.png"
)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
