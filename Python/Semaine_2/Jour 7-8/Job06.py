def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:

        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiples = ((note // 5) + 1) * 5

            difference = prochain_multiples - note

            if difference < 3:
                notes_arrondies.append(prochain_multiples)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

notes = [84, 29, 57, 83, 38, 73, 67, 82, 40]
notes_finales = arrondir_notes(notes)

print("Notes originales :", notes)
print("Notes arrondies :", notes_finales) 