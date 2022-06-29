import random
import matplotlib.pyplot as plt
import numpy as np

import numpy.matlib
from numpy import matlib as mb
from scipy.stats import truncnorm


if __name__ == '__main__':
    # 上面就是生成了指定方差为sigma平方，均值为mu的随机数
    # 26.69是均值23.54是方差
    # sigma = np.sqrt(np.var(23.54))
    # print(sigma * mb.randn(5, 100))
    # a = sigma * numpy.matlib.randn(5, 100) + 26.69
    # print(a)
    import numpy as np
    import scipy.stats as st
    import matplotlib.pyplot as plt

    # s = np.random.normal(2, 3, 500)
    # print(s)
    # s_fit = np.linspace(s.min(), s.max())
    # plt.plot(s_fit, st.norm(2, 3).pdf(s_fit), lw=2, c='r')
    # plt.show()


    # xa, xb = 30, 250
    # loc, loc_guess = 50, 30
    # scale, scale_guess = 75, 90
    # a, b = (xa - loc) / scale, (xb - loc) / scale
    #
    # fig, ax = plt.subplots(1, 1)
    # x = np.linspace(xa, xb, 80)
    # print(x)
    # ax.plot(x, truncnorm.pdf(x, a, b, loc=loc, scale=scale),
    #         'r-', lw=5, alpha=0.6, label='truncnorm pdf')
    #
    a, b = 1, 3
    loc, scale = 2.62, 0.53
    r = truncnorm.rvs(a, b, loc=loc, scale=scale, size=80)
    print(r)
    # par = truncnorm.fit(r, scale=scale_guess, loc=loc_guess)
    # ax.plot(x, truncnorm.pdf(x, *par),
    #         'b-', lw=1, alpha=0.6, label='truncnorm fit')
    # ax.hist(r, density=True, histtype='stepfilled', alpha=0.3)
    # plt.legend()
    # plt.show()