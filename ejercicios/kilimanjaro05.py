from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')




preguntas = {
    "¿Cuántos dedos tienes?": "dedos",
    "¿Cuántas cabezas tienes?": "cabezas",
    "¿Cuántos pies tienes?": "pies",
    "¿Cuántos brazos tienes?": "brazos",
    "¿Cuántos ojos tienes?": "ojos"
}


respuestas = {}

def reclutador():
    resumen = ""
    for pregunta, respuesta in respuestas.items():
        if pregunta == "¿Cuántos dedos tienes?":
            resumen += "Le vamos a preparar unos guantes para sus {} dedos, ".format(respuesta * 2)
        elif pregunta == "¿Cuántas cabezas tienes?":
            if respuesta == 1:
                resumen += "un casco doble para sus 2 cabezas, "
            else:
                resumen += "un casco cuádruple para sus {} cabezas, ".format(respuesta * 2)
        elif pregunta == "¿Cuántos pies tienes?":
            resumen += "{} botas de nieve y {} botas de recambio, ".format(respuesta * 2, respuesta * 2)
        elif pregunta == "¿Cuántos brazos tienes?":
            resumen += "{} mangas para sus {} brazos, ".format(respuesta * 2, respuesta * 2)
        elif pregunta == "¿Cuántos ojos tienes?":
            resumen += "y unas gafas para sus {} ojos, ".format(respuesta * 2)

    return resumen.rstrip(", ")

@app.route("/", methods=["GET", "POST"])
def obtener_respuestas():
    if request.method == "POST":
        for pregunta, variable in preguntas.items():
            respuesta_usuario = request.form.get(variable)
            while not respuesta_usuario.isdigit():
                error = "Error: Debes ingresar un número entero."
                return render_template("index.html", preguntas=preguntas, error=error)
            respuestas[pregunta] = int(respuesta_usuario)
        resumen_reclutador = reclutador()
        return render_template("resumen.html", resumen=resumen_reclutador)
    else:
        return render_template("index.html", preguntas=preguntas)

if __name__ == "__main__":
    app.run(debug=True)
