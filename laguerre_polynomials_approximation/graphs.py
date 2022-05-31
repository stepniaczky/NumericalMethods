from matplotlib import pyplot as plt


def graph(calculated_x, calculated_y, real_x, real_y):

    plt.plot(calculated_x, calculated_y, 'red')
    plt.plot(real_x, real_y, 'lime')

    plt.legend(['calculated', 'real'])
    plt.savefig("graph.jpg", dpi=500)
    plt.show()
