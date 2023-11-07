from collections import Counter
from typing import List, Union
import numpy as np
np.random.seed(1998)
from reaction_generation import get_unique_intermediates, create_reactions
from parameter_estimation import evaluate
from plot_optimal_solution import plot

def bob_the_mechanism_builder(
        reactant:Union[str,List], 
        products:Counter
    ):

    # Find the number of the most repeated product
    most_repeated = products.most_common(1)[0][1]

    # Start with no intermediates and increase the count on each iteration
    iteration_counter = 0
    reaction_chains = []

    # Initialize flag variables
    last_AIC = 100
    AIC = 100
    opt_solution = {}

    # do this loop until current AIC is greater than last iteration's AIC
    while AIC <= last_AIC:
        # Keep track of AIC values and last optimal solution for breaking the loop 
        last_AIC = AIC
        
        # Log important info from the last iteration after first iteration
        if iteration_counter > 0:
            opt_solution["unique_letters"] = unique_letters
            opt_solution["model_predictions"] = model_predictions
            opt_solution["reaction_chain"] = reaction_chain
            opt_solution["nll"] = nll
            opt_solution["AIC"] = AIC

        # Generate intermediates for this iteration
        intermediates = get_unique_intermediates(most_repeated + iteration_counter, products, reactant)

        # Create reactions with the current set of intermediates
        reaction_chain = create_reactions(reactant, products, intermediates)
        reaction_chains.append(reaction_chain)
        print(reaction_chain)

        unique_letters, model_predictions, nll, AIC = evaluate(reaction_chain)

        # Increase the iteration counter
        iteration_counter += 1

    # Print important information of the chosen solution
    print("#"*50, "\n")
    print("Solution found!")
    print(f"Optimal reaction chain: {opt_solution['reaction_chain']}")
    print(f"Optimal NLL: {opt_solution['nll']}")
    print(f"Optimal AIC: {opt_solution['AIC']}")

    # Plot the result
    plot(unique_letters=opt_solution['unique_letters'], model_predictions=opt_solution['model_predictions'])

if __name__ == "__main__":

    # Define the reactant and products
    reactant = 'A'
    products = Counter(['B', 'B', 'B', 'C'])  # 'B' appears three times and 'C' once
    
    # Magic is happening here :)
    print("Mechanism builder is working ...")
    print("#"*50)
    bob_the_mechanism_builder(reactant=reactant, products=products)