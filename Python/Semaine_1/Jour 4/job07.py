def lang(language):
    match language:
        case "JavaScript":
           print("Tu es un developpeur web")
        case "Python":
            print("Tu es un developpeur IA")
        case "Java":
            print("Tu es un developpeur logiciel")
        case "reactjs":
            print("Tu es un developpeur mobile")
        case _:
             print("Uun jour, je serai le meilleur développeur... ")


lang("JavaScript")