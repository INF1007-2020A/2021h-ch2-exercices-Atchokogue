#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    mot_maj = ''
    for lettre in mot:
        mot_maj += chr((ord(lettre) - 32))

    return mot_maj
# difference entre '' et ""


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',  # this is lit
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

