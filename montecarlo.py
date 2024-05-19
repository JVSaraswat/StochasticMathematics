import random
import matplotlib.pyplot as plt


# generate a random int list of length y
def random_list(y):
    return [random.randint(10, 99) for _ in range(y)]


# simulate mean results with x=10 and plot histogram
def simulate_and_plot():
    means = []
    sample_size = 100000
    x = random.randint(1, 9)

    for _ in range(sample_size):
        x_list = random_list(x)
        mean_result = sum(x_list) / x
        means.append(mean_result)

    plt.hist(means, bins=20, color='skyblue', edgecolor='black', linewidth=1.2)
    plt.xlabel('Mean Result')
    plt.ylabel('Frequency')
    plt.title('Histogram of Mean Results (x: 1-9)')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulate_and_plot()

# min max 3 metrcis sample simze of human po;ulkuation
