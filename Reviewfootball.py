import os
Fantacy_File = 'fantacy.txt'
My_Fantacy = 'my_fantacy.txt'
fantacy = []
teams = []

#Code to view all the english premier legue teams.
def English_premiea():
    with open('team.txt', 'r') as f:
        for line in f:
            print(line, end= ' ')
            pass

"""The below functions are for the main program of the fantacy. To add and remove teams in the 
... the user fantacy. Starting up with the 
"""

def load_team():
    if os.path.exists(Fantacy_File):
        with open(Fantacy_File, 'r') as f:
            for line in teams:
                teams.append(line, strip())

def save_team():
    with open(Fantacy_File, 'w') as f:
        for team in teams:
            f.write(team + '\n')


def main_menu():
    print('\n=== WELCOME TO FOOTBALL FANTACY ===')
    print('1.View all teams')
    print('2.Enter to soccer FANTACY')
    print('3.Exit')

def View_teams():
    print(English_premiea())

def my_fantcy():
    def load_fant():
        load_team()
    def save_fant():
        save_team()
    def fant_menu():
        print('\=== YOUR FANTACY ===')
        print('1.Add teams')
        print('2.View teams')
        print('3.Remove teams')
        print('4.Exit fantacy')

    def add_teams(*new_teams):
        for team in new_teams:
            teams.append(team)
            print(f'Your teams : {team}')
        save_fant()

    def view_teams():
        if not teams:
            print('No Teams added yet.')
        else:
            print('\n Your teams ')
            for index, teams in enumerate(teams, start = 1):
                 print(f'{index}, {team}')

    def remove_team():
        view_teams()
        try:
           team_num = int(input('Enter team number to remove'))
           if 1 <= team_num <= len(teams):
               removed = teams.pop(team_num - 1)
               print(f'You removed: {removed}')
               save_fant()
           else:
               print('Enter a number.')

        except(ValueError):
            print('Enter A VALID Number!!!!')

    def main_fantacy():
        load_fant()
        while True:
            fant_menu()
            choice = input('Choose an option:')
            if  choice == '1':
                team_input = input('Enter Your Teams separeted by commas')
                team_list = [t.strip() for t in team_input.split(",")
                             if t.strip()]
                add_teams(*team_list)

            elif choice == '2':
                view_teams()

            elif choice == '3':
                remove_team()

            elif choice == '4':
                print('Goodbye!')
                break
            else:
                print('Invalid option!!')

                
def exit_fantacy():
    print('Bye Soccer ANALIYST')
    

def Main():
    load_team()
    while True:
        main_menu()
        choice = input('Choose an option:')
        if choice == '1':
            View_teams()

        elif choice == '2':
             my_fantcy()
             main_fantacy()

        elif choice == '3':
            exit_fantacy()
            break

        else:
            print('Enter a valid option!!!!!')

if __name__ == "__main__":
    Main()
            
            
        

        

