import pandas as pd
import random

# Read the datafile
data = pd.read_csv('data.csv', sep=',')

class decaycalculations:
    def alpha_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 2)

        # Find the new isotope
        new_isotope = isotope_number_input - 4

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("He-4")
            return

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def beta_minus_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] + 1)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + e-")
        decaydetermination.continue_decay(new_element, new_isotope)

    def two_beta_minus_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] + 2)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + 2e-")
        decaydetermination.continue_decay(new_element, new_isotope)

    def beta_plus_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 1)

        # Find the new isotope
        new_isotope = isotope_number_input
        
        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("e-")
            return


        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + e+")
        decaydetermination.continue_decay(new_element, new_isotope)

    def two_beta_plus_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 2)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("e-")
            return

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + 2e+")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def alphabeta_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 1)

        # Find the new isotope
        new_isotope = isotope_number_input - 4
        
        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("e-")
            return

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("He-4 + e-")
            return

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def betaneutron_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] + 1)

        # Find the new isotope
        new_isotope = isotope_number_input - 1

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def betatwoneutron_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] + 1)

        # Find the new isotope
        new_isotope = isotope_number_input - 2

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def betaproton_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] + 1)

        # Find the new isotope
        new_isotope = isotope_number_input - 1

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def neutron_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0])

        # Find the new isotope
        new_isotope = isotope_number_input - 1

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def twoneutron_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0])

        # Find the new isotope
        new_isotope = isotope_number_input - 2

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def electroncapture_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 1)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def twoelectroncapture_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 2)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def electroncapturebeta_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0] - 2)

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def proton_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0])

        # Find the new isotope
        new_isotope = isotope_number_input-1

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)
        
    def twoproton_decay(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[row_number, 'z']
        new_atomnumber = int(atomnumber.iloc[0])

        # Find the new isotope
        new_isotope = isotope_number_input-2

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Retrieve the decay result
        print(f"Decay result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + alpha")
        decaydetermination.continue_decay(new_element, new_isotope)

    def spontaneous_fission(row_number, element_input, isotope_number_input):
        # Find the new element
        atomnumber = data.loc[data['symbol'] == element_input, 'z'].values[0]
        new_atomnumber = atomnumber

        # Find the new isotope
        new_isotope = isotope_number_input

        # Construct the new element and isotope labels
        new_element = data.loc[data['z'] == new_atomnumber, 'symbol'].values[0]

        # Check if the new isotope is within the range of isotopes
        if new_isotope == 0:
            print("Decay result: No spontaneous fission observed.")
            return

        # Retrieve the decay result
        print(f"Spontaneous fission result for '{element_input}' with isotope number '{isotope_number_input}' is:")
        print(f"{element_input}-{isotope_number_input} -> {new_element}-{new_isotope} + fission products")
        decaydetermination.continue_decay(new_element, new_isotope)

class decaydetermination:
    
    def decay_chance(row_number, element_input, isotope_number_input):
        decay1_chance = data.loc[row_number, 'decay_1_%'].iloc[0]
        decay2_chance = data.loc[row_number, 'decay_2_%'].iloc[0]
                
        # Generate a random number between 0 and 100
        random_number = random.uniform(0, 100)

        # Choose the decay based on the random number and decay chances
        if random_number <= decay1_chance:
            decay = data.loc[row_number, 'decay_1'].iloc[0]
            decaydetermination.decay_list(row_number, element_input, isotope_number_input, decay)
        elif random_number <= decay1_chance + decay2_chance:
            decay = data.loc[row_number, 'decay_2'].iloc[0]
            decaydetermination.decay_list(row_number, element_input, isotope_number_input, decay)
        else:
            decay = data.loc[row_number, 'decay_3'].iloc[0]  
            decaydetermination.decay_list(row_number, element_input, isotope_number_input, decay)
             
    def decay_list(row_number, element_input, isotope_number_input, decay):
        match decay:
            case 'A':
                decaycalculations.alpha_decay(row_number, element_input, isotope_number_input)
            case 'B-':
                decaycalculations.beta_minus_decay(row_number, element_input, isotope_number_input)
            case '2B-':
                decaycalculations.two_beta_minus_decay(row_number, element_input, isotope_number_input)
            case 'B+':
                decaycalculations.beta_plus_decay(row_number, element_input, isotope_number_input)
            case '2B+':
                decaycalculations.two_beta_plus_decay(row_number, element_input, isotope_number_input)
            case 'B-A':
                decaycalculations.alphabeta_decay(row_number, element_input, isotope_number_input)
            case 'B-N':
                decaycalculations.betaneutron_decay(row_number, element_input, isotope_number_input)
            case 'B-2N':
                decaycalculations.betatwoneutron_decay(row_number, element_input, isotope_number_input)
            case 'B+P':
                decaycalculations.betaproton_decay(row_number, element_input, isotope_number_input)
            case 'N':
                decaycalculations.neutron_decay(row_number, element_input, isotope_number_input)
            case '2N':
                decaycalculations.twoneutron_decay(row_number, element_input, isotope_number_input)
            case 'EC':
                decaycalculations.electroncapture_decay(row_number, element_input, isotope_number_input)
            case '2EC':
                decaycalculations.twoelectroncapture_decay(row_number, element_input, isotope_number_input)
            case 'EC+B+':
                decaycalculations.electroncapturebeta_decay(row_number, element_input, isotope_number_input)
            case 'SF':
                decaycalculations.spontaneous_fission(row_number, element_input, isotope_number_input)
            case 'P':
                decaycalculations.proton_decay(row_number, element_input, isotope_number_input)
            case '2P':
                decaycalculations.twoproton_decay(row_number, element_input, isotope_number_input)
            case _:
                print('Stable')
        
    def decay_checker(row_number, element_input, isotope_number_input):
        # Check if the element is stable
        half_life_value = data.loc[row_number, 'half_life']
        if half_life_value.str.contains("STABLE").any():
            print('stable')
        else:
            decaydetermination.decay_chance(row_number, element_input, isotope_number_input)
            
    def continue_decay(new_element, new_isotope):
        # Check if the element with the given isotope number is in the data
        isotope_exists = (data['symbol'] == new_element) & (data['n'] + data['z'] == new_isotope)
        if isotope_exists.any():
            print('Would you like to continue the decay? (Yes or No)')
            user_input = input()
            if user_input.lower() == 'yes':
                row_number = isotope_exists.index[isotope_exists]
                element_input = new_element
                isotope_number_input = new_isotope
                decaydetermination.decay_checker(row_number, element_input, isotope_number_input)
            else:
                print('')
        else:
            print('')

class elementinfo:
    def halflife(row_number):
        half_life_sec = data.loc[row_number, 'half_life_sec'].values[0]

        if isinstance(half_life_sec, (int, float)) and half_life_sec >= 0.001:
            # If it's a numerical value greater than or equal to 0.001 seconds
            return half_life_sec, 'seconds'
        elif half_life_sec == "STABLE":
            # If it's the string "STABLE"
            half_life_years = data.loc[row_number, 'half_life'].values[0]
            return half_life_years, 'years'
        else:
            # If it's not a numerical value or "STABLE"
            return 'stable'

    def basicinfo(element_input, row_number):
        print('name:', element_input)
        atomnumber = data.loc[row_number, 'z'].values[0]
        print('atomnumber:', atomnumber)

        # Call the halflife function and store the result in livingspan
        livespan = elementinfo.halflife(row_number)
        print('half-life:', livespan)
        
        atomic_mass = data.loc[row_number, 'atomic_mass'].values[0]
        print('atomic mass:', atomic_mass,'AMU' )
        
        discovery = data.loc[row_number, 'discovery'].values[0]
        print('discovery:', discovery)
        
        authors = data.loc[row_number, 'ENSDFauthors'].values[0]
        print('authors:', authors)
      
class menu_options:    
    def decaycalculator():
        # Terminal input
            print('What element would you like the decay of?')
            element_input = input()

            print('What isotope number would you like to search for?')
            isotope_number_input = int(input())

            # Check if the element with the given isotope number is in the data
            isotope_exists = (data['symbol'] == element_input) & (data['n'] + data['z'] == isotope_number_input)

            if isotope_exists.any():
                row_number = isotope_exists.index[isotope_exists]
                decaydetermination.decay_checker(row_number, element_input, isotope_number_input)
            else:
                print(f"{element_input} with isotope number {isotope_number_input} is not in the data.")

    def element_info():
        print('What element would you like information about?')
        element_input = input()
        
        # Check if the element exists
        element_exists = data['symbol'] == element_input
        
        if element_exists.any():
            row_number = element_exists.index[element_exists]
            elementinfo.basicinfo(element_input, row_number)
        else:
            print(f"{element_input} is not in the data.")
        
def main_menu():
    # Start the decay simulation loop
    while True:
        print('What would you like to do?')
        print('Input \'1\' for the decay calculator')
        print('Input \'2\' for element information')
        
        user_input = input()
        match user_input:
            case '1':
                menu_options.decaycalculator()
            case '2':
                menu_options.element_info()
            case _:
                break

if __name__ == "__main__":
    main_menu()
