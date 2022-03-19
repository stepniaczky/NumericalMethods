from matplotlib import pyplot as plt


def graph(func, p, k, wynik, met, fn_str):
    plt_precision = 0.01
    pocz = p
    fx = [0.0] * int((abs(p) + k) / plt_precision)
    fy = [0.0] * int((abs(p) + k) / plt_precision)
    for i in range(len(fx)):
        fx[i] = pocz
        fy[i] = func(pocz)
        pocz += plt_precision

    min_height = min(fy) - 0.5
    max_height = max(fy) + 0.5

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

    # ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    # ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
                xytext=(20, 0), textcoords='offset points',
                ha='left', va='center',
                arrowprops=dict(arrowstyle='<-', fc='black'))

    # Y-axis arrow
    ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
                xytext=(0, 20), textcoords='offset points',
                ha='center', va='bottom',
                arrowprops=dict(arrowstyle='<-', fc='black'))

    plt.title(name, loc='left')

    # plt.text(k - 0.08, 0.25, 'x', fontsize=8)
    # plt.text(0.25 * k, max_height - 0.08 * max_height, 'y', fontsize=8)

    # plt.text(k - 0.1, -0.06, '\u25B6', fontsize=6)
    # plt.text(0 - 0.07, max_height - 0.12, '\u25B2', fontsize=6)

    # plt.grid(True)
    plt.xlim(p, k)
    plt.ylim(min_height, max_height)

    result = plt.scatter(wynik, func(wynik), color='red')
    line, = plt.plot(fx, fy, color='blue')
    plt.legend([line, result], [f'{fn_str}', f'{wynik}'], loc="upper left", fontsize=7)
    plt.savefig(name + ".jpg", dpi=500)
    plt.show()
