import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def relative_error(i):
    _k = np.sqrt(i)
    return _k

if __name__ == '__main__':
    df = pd.read_excel('/Users/yuitake/PycharmProjects/物理_ガンマ線/ガンマ線2.xlsx', sheet_name='Sheet7', usecols="A:C")
    print(df)

    x_Al=df['枚数']
    x_Al=x_Al.values.tolist()

    y=df['count']
    y=y.values.tolist()
    print(y)
    y_err=[]
    for n in y:
        res = relative_error(n)
        y_err.append(res.tolist())
    print(y_err)
    plt.yscale('log')
    plt.errorbar(x_Al, y, yerr=y_err, capsize=4, fmt='.', ecolor='red', color='black')
    plt.show()