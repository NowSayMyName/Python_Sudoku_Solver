#-*-coding: utf8-*-

from grid import SudokuGrid
from solver import SudokuSolver

def start():
    chx = 4
    while chx not in (1,2):
        chx = int(input("Souhaiter vous entrer votre propre sudoku ou aller chercher cette grille dans un fichier ? (\"1\", \"2\") : "))
    if chx == 2:
        fichier = input("Veuillez saisir le nom du fichier (dans le meme dossier que les scripts) : ")
        ligne = input("Veullez saisir la ligne à lire dans le fichier : ")
        Sudoku = SudokuGrid.from_file(fichier, int(ligne))
    else:
        Sudoku = SudokuGrid.from_stdin()   
    return Sudoku

def play(Sudoku):
    new_instance = None
    while Sudoku.get_empty_pos():
        i = j = v = 11
        instance_act = Sudoku
        while i not in range(1,10):
            i = int(input("Veuillez entrer la ligne sur laquelle se situe la case à modifier (de haut en bas, de 1 à 9) : "))
        while j not in range(1,10):
            j = int(input("Veuillez entrer la colonne sur laquelle se situe la case à modifier (de gauche à droite, de 1 à 9) : "))
        while v not in range(1, 10):
            v = int(input("Veuillez entrer la valeur à mettre dans cette case (de 1 à 9) : "))
        instance_act.write(i - 1, j - 1, v)
        new_instance = instance_act.copy()
        print(new_instance)
    return new_instance

def solve(Sudoku):
    solver = SudokuSolver(Sudoku)
    return solver.solve()

if __name__ == "__main__":
    Sudoku = start()
    print(Sudoku)
    choix = input("Souhaitez vous jouer ou résoudre un sudoku ? : (\"1\", \"2\") : ")
    if int(choix) == 1:
        play(Sudoku)
    else:
        print(solve(Sudoku))