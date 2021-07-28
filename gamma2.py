import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def relative_error(i):
    _k = np.sqrt(i)
    return _k

if __name__ == '__main__':
    df = pd.read_excel('/Users/yuitake/PycharmProjects/物理_ガンマ線/ガンマ線2.xlsx', sheet_name='Sheet4', usecols="A:F")
    print(df)
    x_Al=df['アルミ']
    x_Al=x_Al.values.tolist()

    y_Al=df['count(Al)']
    y_Al=y_Al.values.tolist()


    y_err=[]
    for n in y_Al:
        res = relative_error(n)
        y_err.append(res.tolist())

    x_Pb=df['鉛']
    x_Pb=x_Pb.values.tolist()
    y_Pb=df['count(Pb)']
    y_Pb=y_Pb.values.tolist()
    y_Pb_err = []
    for n in y_Pb:
        res = relative_error(n)
        y_Pb_err.append(res.tolist())


    plt.errorbar(x_Al, y_Al, yerr=y_err, capsize=4, fmt='.', ecolor='red', color='black')
    plt.errorbar(x_Pb, y_Pb, yerr=y_Pb_err, capsize=4, fmt='.', ecolor='blue', color='black')
    plt.yscale('log')
    plt.show()