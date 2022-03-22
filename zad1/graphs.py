from matplotlib import pyplot as plt


def graph(func, p, k, wynik, met):

    plt_precision = 0.0001
    pocz = p
    fx = [0.0] * int((abs(p) + k) / plt_precision)
    fy = [0.0] * int((abs(p) + k) / plt_precision)
    for i in range(len(fx)):
        fx[i] = pocz
        fy[i] = func(pocz)
        pocz += plt_precision

    min_ = min(abs(p), abs(k))

    min_height = min(fy) - 0.5
    if abs(min(fy)) < min_:
        min_height = -abs(min_)
    elif abs(min(fy)) < 3 * min_:
        min_height = 3 * min_

    max_height = max(fy) + 0.5
    if max(fy) < min_:
        max_height = min_
    elif max(fy) > 3 * min_:
        max_height = 3 * min_

    name = "Metoda "
    if met == 1:
        name += "bisekcji"
    else:
        name += "siecznych"

    fig = plt.figure(dpi=500)
    ax = fig.add_subplot(1, 1, 1)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(7, 0), textcoords='offset points',
                ha='left', va='center')

    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(0, 7), textcoords='offset points',
                ha='center', va='bottom',)

    ax.text(x=wynik + 0.3, y=0.3, s=f"{round(wynik, 3)}...", fontsize=6)

    if p > 0:
        plt.xlim(-1, k)
    if k < 0:
        plt.xlim(p, 10)
    plt.xlim(p, k)
    # max3 = 3 * max(p, k)
    # if min_height < -1 * max3:
    #     min_height = -1 * int(max3)
    # if max_height > max3:
    #     max_height = int(max3)
    plt.ylim(min_height, max_height)

    plt.axis('scaled')
    plt.scatter(wynik, func(wynik), color='red')
    plt.plot(fx, fy, color='blue')
    plt.savefig(name + ".jpg", dpi=500)
    plt.show()
