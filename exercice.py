#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici

    motmaj = ''
    for j in range(len(mot)):
        motmaj = motmaj + chr((ord(mot[j]) - 32))

    return motmaj


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

