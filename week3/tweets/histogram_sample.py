'''
sample code for plotting a histogram

original code:
https://github.com/GirlsFirst/SIP-2018-starter/blob/master/U2-Applications/U2.1-Data/histogram_sample.py
'''
import matplotlib.pyplot as plt

def plot_histogram(data, data_bins, axis_list):
    plt.hist(data, bins=data_bins)
    plt.xlabel('Values')
    plt.ylabel('Number of Items')
    plt.title('Histogram of Numbers')
    plt.axis(axis_list)
    plt.grid(True)
    plt.show()

def main():
    someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
    bins = [-1, -0.5, 0.0, 0.5, 1]
    axes = [-1.1, 1.1, 0, 6]
    plot_histogram(someList, bins, axes)

if __name__ == '__main__':
    main()
