import csv

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.get_backend()

class Candidate:
    def __init__(self, name, skill, luck, net_score):
        self.name = name
        self.skill = skill
        self.luck = luck
        self.net_score = net_score


# Load data from CSV file (top_candidates.csv)
def load_candidates_from_csv(filename):
    candidates = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            skill = int(row['Skill'])
            luck = int(row['Luck'])
            net_score = float(row['Net_score'])
            candidates.append(Candidate(name, skill, luck, net_score))
    return candidates

# Plotting function
def plot_top_candidates(candidates):
    # Sort candidates based on net score (descending order)
    sorted_candidates = sorted(candidates, key=lambda x: x.net_score, reverse=True)

    names = [candidate.name for candidate in sorted_candidates]
    skills = [candidate.skill for candidate in sorted_candidates]
    lucks = [candidate.luck for candidate in sorted_candidates]
    net_scores = [candidate.net_score for candidate in sorted_candidates]

    # Normalize net scores to use as bar lengths
    max_net_score = max(net_scores)
    normalized_net_scores = [score / max_net_score for score in net_scores]

    # Create horizontal bar plot
    fig, ax = plt.subplots(figsize=(10, len(sorted_candidates) * 0.5))

    # Plot bars for skill (blue) and luck (green)
    ax.barh(names, skills, color='blue', label='Skill', alpha=0.5)
    ax.barh(names, lucks, left=skills, color='green', label='Luck', alpha=0.5)

    # Set y-axis labels
    ax.set_yticks(np.arange(len(names)))
    ax.set_yticklabels(names)

    # Set x-axis label
    ax.set_xlabel('Score')

    # Set legend
    ax.legend()

    plt.title('Candidate Skills and Luck')
    plt.tight_layout()
    plt.show()


# Example usage:
output_filename = 'top_candidates.csv'
top_candidates = load_candidates_from_csv(output_filename)
plot_top_candidates(top_candidates)

