from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def triangulo():
    area = None
    perimetro = None
    error = None

    if request.method == "POST":
        try:
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            lado1 = float(request.form['lado1'])
            lado2 = float(request.form['lado2'])
            lado3 = float(request.form['lado3'])

            if base <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                error = "Todos los valores deben ser mayores que cero."
            elif (lado1 + lado2 <= lado3 or 
                  lado1 + lado3 <= lado2 or 
                  lado2 + lado3 <= lado1):
                error = "Los tres lados no pueden formar un triángulo."
            else:
                area = (base * altura) / 2
                perimetro = lado1 + lado2 + lado3
        except ValueError:
            error = "Por favor, ingresa valores numéricos válidos."

    return render_template(
        "triangulo.html",
        area=area,
        perimetro=perimetro,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
