#-*-coding: utf8-*-

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """

    @classmethod
    def from_file(cls, filename, line):
        """
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne contenue dans un fichier.
        Pour retourner une nouvelle instance de la classe, utilisez le premier argument ``cls`` ainsi::
            return cls(arguments du constructeur)

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """
        with open(filename, "r") as fichier:
            grid_info = fichier.readlines()
            grid_info = grid_info[line-1].strip("\n")
            return cls(grid_info)

    @classmethod
    def from_stdin(cls):
        """
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne lu depuis l'entrée standard (saisi utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """
        in_str = input("Veuillez entrez une chaine de caracteres contenant exactement 81 chiffres compris entre 0 et 9 : ")
        return cls(in_str)

    def __init__(self, initial_values_str):
        """
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        if initial_values_str.isdigit() and len(initial_values_str) == 81:
            self.grid = dict()
            for i in range(9):
                for j in range(9):
                    self.grid[i, j] = int(initial_values_str[i*9+j])
        else:
            raise ValueError("La chaine doit contenir exactement 81 chiffres de 0 à 9")

    def __str__(self):
        """
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """
        
        #l'affichage n'est pas très beau mais suffisant
        string = ""
        for i in range(9):
            if i%3 == 0:
                string += "+++++++++++++\n"
            for j in range(9):
                if j%3 == 0:
                    string += "+"
                string += str(self.grid[i, j])
            string += "+\n"
        string += "+++++++++++++\n"
        return string

    def get_row(self, i):
        """
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """
        row = list()
        for j in range(9):
            row.append(self.grid[i, j])
        return row

    def get_col(self, j):
        """
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        col = list()
        for i in range(9):
            col.append(self.grid[i, j])
        return col

    def get_region(self, reg_row, reg_col):
        """
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """

        if 0 <= reg_row <= 2 and 0 <= reg_col <= 2:
            reg_content = list()
            for i in range(3):
                for j in range(3):
                   reg_content.append(self.grid[reg_row*3+i, reg_col*3+j])
            return reg_content
        else:
            raise ValueError("entrez des valeurs entre 0** et 2**")

    def get_empty_pos(self):
        """
        Cette méthode renvoit la position des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of tuple of int
        """
        empty_pos_list = list()
        for i in range(9):
            for j in range(9):
                if self.grid[i, j] == 0:
                    coord = (i, j)
                    empty_pos_list.append(coord)
        return empty_pos_list

    def write(self, i, j, v):
        """
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        if 0 <= i <= 8 and 0 <= j <= 8 and 0 <= v <= 9:
            if self.grid[i, j] != 0:
                print("\nLa case n'est pas vide !!")
            else:
                self.grid[i, j]=v
        else:
            raise ValueError("i et j doivent être compris entre 0** et 8**, v entre 0** et 10**")

    def copy(self):
        """
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        copie **indépendante** de la grille de Sudoku.
        Vous pouvez utiliser ``self.__class__(argument du constructeur)``.
        *Variante avancée: vous pouvez aussi utiliser ``self.__new__(self.__class__)``
        et manuellement initialiser les attributs de la copie.*
        """

        string = str(self)
        string = string.replace('\n', '')
        string = string.replace('+', '')
        return self.__class__(string)

