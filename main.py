import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function(x, _lambda: float):
    # Get the theoretical value
    _k = (2 * np.pi) / _lambda
    _res = np.sin(_k * x) ** 2
    return _res

def make_lambda(_lambda: float, _start: float, _end: float, _step: float, flag_method: int = 1):
    # Make a list of values ranging from -2.0 to 2.0 by step-size 0.1
    _base = np.arange(_start, _end, _step)
    _base += _lambda
    # List: sorted float values; +-0.1 ~ 2.0 at _lambda
    return sorted(_base)

if __name__ == '__main__':
    _lambda = 28.8
    # Make a list of values ranging from -2.0 to 2.0 by step-size 0.1
    lambda_list = make_lambda(_lambda=_lambda, _start=-2.0, _end=2.0, _step=0.1)
    print(lambda_list)

    # Init x
    x = np.arange(-11.0, 39.0, 1.0)
    _q = pd.ExcelFile('/Users/yuitake/Library/Containers/com.microsoft.Excel/Data/Desktop/物理学実験　回折　   実験課題1.xlsx')
    data_q = pd.read_excel(_q, '残差の表 (訂正後)', header = 0,  usecols=[2])
    print(data_q.values)
    obs_values = data_q.values.T

    # For each lambda, apply the function with all values in x
    result = list()

    # for _x in x:
    #     for __lambda in lambda_list:
    #         res = function(x=_x, _lambda=__lambda)
    #         result.append(res)

    # row: lambda, col: x
    for __lambda in lambda_list:
        res = function(x=x, _lambda=__lambda)
        result.append(res.tolist())
        # for _x in x:
        #     res = function(x=_x, _lambda=__lambda)
        #     result.append(res)

    # Convert the list into numpy array
    result = np.asarray(result)
    print(result.shape)

    # Mean Squared Error
    result = np.square(result - obs_values)
    print(result.shape)
    print(result.sum(axis=1).shape, result.sum(axis=0).shape)
    sum_lambda = result.sum(axis=1)
    plt.plot(lambda_list, sum_lambda)
    plt.show()

    # result = list()
    # for x in range(3):
    #     value_dict, if_equal = function(x, _lambda=_lambda, actual_value=None)
    #     print(f"x: {x} -> {value_dict}: {if_equal}")
    #     result.append(value_dict)
    # value_dict, if_equal = function(x, _lambda=_lambda, actual_value=actual_value)
    # print(f"x: {x} -> {value_dict}: {if_equal}")
    # df = pd.DataFrame(result)
    # df.columns = ["lambda={}".format(_lambda), "flag", "name", "age"]
    # print(df)
    # df.to_csv("a.csv", index=False)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
