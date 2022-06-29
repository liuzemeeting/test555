import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab
from pylab import *
# 2.78 1.28
# 3.56 1.46
# 3.88 1.38
# 2.80 1.58
# 2.79 1.15
# 3.24 1.48

b = 1.48
from excel_test import data_write

if __name__ == '__main__':
    u_data_list = []
    flag = True
    while flag:
        mu, sigma = 3.24, 2.2
        # mu, sigma = sigma, mu
        lower, upper = mu - 1 * sigma, mu + 1 * sigma  # 截断在[μ-2σ, μ+2σ]
        # print(lower, upper)
        # X = stats.truncnorm((5 - mu) / sigma, (300 - mu) / sigma, loc=mu, scale=sigma)
        X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
        # N = stats.norm(loc=mu, scale=sigma)
        data_list = [round(i, 2) for i in X.rvs(80)]

        avg_data = np.mean(data_list)
        var_data = np.var(data_list, ddof=2)
        print("均值：%s" % avg_data, "方差：%s" % var_data)

        if 3.2 < avg_data < 3.3 and 1.4 < var_data < 1.6:
            print(data_list)
            print(np.var(data_list, ddof=2))
            print(np.mean(data_list))
            data_list.append("均值：%s" % avg_data)
            data_list.append("方差：%s" % var_data)
            u_data_list.append(data_list)
            f = open('a.txt', 'a+')
            f.writelines(','.join(str(i) for i in data_list))

            f.writelines("方差：" + str(var_data) + "均值：" + str(avg_data))
            f.writelines('\n')
            f.close()
            if len(u_data_list) == 100:
                data_write(f"均值{mu}方差{b}.xls", u_data_list)
            # if len(u_data_list) > 100:
                flag = False


    # figure(1)6b
    # subplot(2,1,1)
    # plt.hist(X.rvs(10000), normed=True, bins=30)   # 截断正态分布的直方图
    # subplot(2,1,2)
    # plt.hist(N.rvs(10000), normed=True, bins=30)   # 常规正态分布的直方图
    # plt.show()