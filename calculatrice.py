# Fonctions des opérations
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")
        return None

# Affichage message accueil
def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")

# Saisie des deux nombres
def input_two_numbers():
    while True:
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
            return num1, num2
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")

# Affichage menu et récupération du choix
def print_menu_and_get_choice():
    print("\n=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    user_choice = input("Entrez votre choix (1-5) : ")
    while user_choice not in ["1", "2", "3", "4", "5"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-5) : ")
    return user_choice

# Exécution du calcul selon le choix
def run_calculation(user_choice):
    num1, num2 = input_two_numbers()
    result = None
    match user_choice:
        case '1':
            result = addition(num1, num2)
        case '2':
            result = subtraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = division(num1, num2)
    return result

# Programme principal
if __name__ == '__main__':
    print_welcome_message()
    
    while True:
        user_choice = print_menu_and_get_choice()
        if user_choice == '5':  # Quitter
            print("Au revoir !")
            break
        result = run_calculation(user_choice)
        if result is not None:
            print(f"Résultat : {result}")