import random
import string
import csv
import subprocess
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

from TBD.plot_graph import load_candidates_from_csv


class Candidate:
    name = ""
    skill = 0
    luck = 0
    net_score = 0

    def __init__(self, name, skill, luck, net_score):
        self.name = name
        self.skill = skill
        self.luck = luck
        self.net_score = net_score


def generate_name():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


def generate_candidates(n, x, y):
    candidates = []
    for _ in range(n):
        name = generate_name()
        skill = random.randint(0, 900)
        luck = random.randint(0, 100)
        net_score = ((x * skill) + (y * luck)) / (x + y)
        candidates.append(Candidate(name, skill, luck, net_score))
    return candidates


def find_top_candidates(candidates, percentage):
    num_top = max(1, int(len(candidates) * percentage / 100))
    candidates.sort(key=lambda x: x.net_score, reverse=True)
    return candidates[:num_top]


def calculate_average_scores(candidates):
    total_skill = sum(candidate.skill for candidate in candidates)
    total_luck = sum(candidate.luck for candidate in candidates)
    return total_skill / len(candidates), total_luck / len(candidates)


def save_to_csv(candidates, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Skill', 'Luck', 'Net_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for candidate in candidates:
            writer.writerow({
                'Name': candidate.name,
                'Skill': candidate.skill,
                'Luck': candidate.luck,
                'Net_score' : candidate.net_score
                })


# Example usage:
n = 15000
x = 5
y = 1.5
top_percentage = 0.67
output_filename = 'top_candidates.csv'

candidates = generate_candidates(n, x, y)
top_candidates = find_top_candidates(candidates, top_percentage)
avg_skill, avg_luck = calculate_average_scores(top_candidates)

print("Total candidates sampled: "+n.__str__())
print(f"Average skill of top {top_percentage}% candidates: {avg_skill}")
print(f"Average luck of top {top_percentage}% candidates: {avg_luck}")

save_to_csv(top_candidates, output_filename)
print(f"Top {top_percentage}% candidates saved to {output_filename}")






# Plotting function
def plot_top_candidates(candidates):
    names = [candidate.name for candidate in candidates]
    skills = [candidate.skill for candidate in candidates]
    lucks = [candidate.luck for candidate in candidates]
    net_scores = [candidate.net_score for candidate in candidates]

    # Normalize net scores to use as bar lengths
    max_net_score = max(net_scores)
    normalized_net_scores = [score / max_net_score for score in net_scores]

    # Create horizontal bar plot
    fig, ax = plt.subplots(figsize=(10, len(candidates) * 0.5))

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

print("graph plotted")
