import pdb
from services import compute_lcm, sort_numbers

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/lcm", methods=["GET", "POST"])
def get_lcm():
    if request.method == "GET":
        return render_template("lcm.html")
    data = request.form  # ! data = {"x": 5, "y": 10}
    x = data["x"]  # * x=5
    y = data["y"]  # * y=10

    lcm = compute_lcm(x, y)
    context = {"lcm": lcm, "x": x, "y": y}
    return render_template("lcm.html", **context)


@app.route("/sort", methods=["GET", "POST"])
def sort():
    print(request.remote_addr)
    if request.method == "GET":
        return render_template("sort.html")
    data = request.form
    numbers = data["numbers"].split("\n")
    sorted_numbers = sort_numbers(numbers)
    # * kwargs & args
    context = {"sorted_numbers": sorted_numbers}
    return render_template("sort.html", **context)


if __name__ == "__main__":
    app.run(debug=True)

