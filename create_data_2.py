import numpy as np
# import matplotlib.pyplot as plt
from math import sqrt

# # bi = np.random.binomial(n=100, p=0.5, size=200)
# n = np.random.normal(100*0.5, sqrt(100*0.5*0.5), size=500)
# #
# # plt.hist(bi, bins=20, normed=True);
# plt.hist(n, alpha=0.5, bins=20, normed=True);
# plt.show();
# print()

from scipy.stats import truncnorm


def get_truncated_normal(mean=0.00, sd=1.00, low=20.00, upp=30.00):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


if __name__ == '__main__':
    import numpy as np

    # arr = np.array([1, 2, 3, 4, 5, 6, 7])
    #
    # print(arr[1:5:3])
    # 0.0854±0.03
    X1 = get_truncated_normal(mean=0.0854, sd=0.03, low=0.02, upp=0.10)
    print(X1)
    print(X1.rvs(100))
    data_list = [i for i in X1.rvs(100)]
    print(np.mean(data_list))
    print(np.var(data_list))
    # X2 = get_truncated_normal(mean=5.5, sd=1, low=1, upp=10)
    # X3 = get_truncated_normal(mean=25.13, sd=36.00, low=20.13, upp=30.00)
    #
    # # import matplotlib.pyplot as plt
    # # fig, ax = plt.subplots(3, ncols=1, sharex=True)
    # # ax[0].hist(X1.rvs(10000))
    # # ax[1].hist(X2.rvs(10000))
    # print(X3)
    #
    # _ = X3.rvs(100)
    # # ax[2].hist(_)
    # # plt.show()
    # data_list = [int(j) for j in _]
    # print(len(data_list))
    # print(data_list)
    #
    # np.savetxt("result.txt", [int(j) for j in _], fmt='%d');