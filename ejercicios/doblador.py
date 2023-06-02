

preguntas = {
    "¿Cuántos dedos tienes?": "dedos",
    "¿Cuántas cabezas tienes?": "cabezas",
    "¿Cuántos pies tienes?": "pies",
    "¿Cuántos brazos tienes?": "brazos",
    "¿Cuántos ojos tienes?": "ojos"
}

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