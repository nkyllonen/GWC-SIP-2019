'''
sample code for plotting a histogram

original code:
https://github.com/GirlsFirst/SIP-2018-starter/blob/master/U2-Applications/U2.1-Data/histogram_sample.py
'''
import matplotlib.pyplot as plt

'''
plot_histogram:
    data(list)      :   list of data values
    data_bins(list) :   list of bin values (x-axis)
    axis_list(list) :   list of min & max axis values
'''
def plot_histogram(data, data_bins, axis_list, title, xlabel, ylabel):
    plt.hist(data, bins=data_bins)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.axis(axis_list)
    plt.grid(True)
    plt.show()

def main():
    someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
    bins = [-1, -0.5, 0.0, 0.5, 1]      # [x-axis values]
    axes = [-1.1, 1.1, 0, 6]            # [min_x, max_x, min_y, max_y]
    plot_histogram(someList, bins, axes, "Histogram of Numbers", "Values", "Numer of Items")

if __name__ == '__main__':
    main()
