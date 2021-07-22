import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#相対誤差を求める式
def relative_error(i):
    _k = 1 / np.sqrt(i)
    return _k

if __name__ == '__main__':
    df = pd.read_excel('/Users/yuitake/PycharmProjects/物理_ガンマ線/ガンマ線2.xlsx', sheet_name='Sheet2', usecols="A:C",
                       skiprows=2, skipfooter=7)

    print('df.columnsを調べる')
    print(df.columns)#列名を調べるために利用した。

    Dx = df[0]#dataframeの電圧を記録した列をDxとした。
    Dx1_list = Dx.values.tolist()#Dxをリストにする。
    print('Dx1_listのdataframe')
    print(Dx1_list)
    print('indexの名称')
    print(df.index)

    Dx2 = df.drop([10,12,14,16,18,20,21,22,23,24,25,26,27,28,29,30,31])#カウント数がNaNになる時の電圧を消去
    Dx2_2 = Dx2[0]#dataframeの電圧を記録した列を取り出す。
    Dx2_list = Dx2_2.values.tolist()#Dx2をリストにする。
    print('Dx2_listのdataframe')
    print(Dx2_list)

    Dy1 = df["0.1"]  # Dxは線源ありの時のカウント数のdataframeの列 relative_errorの分母が0になるのを防ぐために、0を抜いた。
    print('Dy1のdataframe')
    print(Dy1)
    Dy2 = df['0.2']  # Dyは線源なしの時のカウント数のdataframeの列 relative_errorの分母が0になるのを防ぐために、0を抜いた。
    print('Dy2のdataframe')
    print(Dy2)

    Dy1_list = Dy1.values.tolist()#dataframeをリストとして使えるようにした。
    print('Dy1_listのリスト')
    print(Dy1_list)
    '''Dy2_list=Dy2.values.tolist()
    print(Dy2_list)'''#間違えた記述だが後学のため残した。
    Dy2_list = Dy2.dropna()#NaNの部分を消した。
    print('Dy2_listのリスト')
    print(Dy2_list.dropna().tolist())


    #まず、線源ありの時の相対誤差
    result1 = []
    for n in Dy1_list:
        res = relative_error(n)
        result1.append(res.tolist())
    print('線源ありの時のカウント数')
    print(result1)

    #次に、線源なしの時の相対誤差
    result2 = []
    for n in Dy2_list:
        res = relative_error(n)
        result2.append(res.tolist())
    print('線源なしの時のカウント数')
    print(result2)

    ax1 = plt.subplot(3, 1, 1)
    plt.scatter(Dx1_list, Dy1_list)
    ax2 = plt.subplot(3, 1, 2)
    plt.scatter(Dx2_list, Dy2_list)
    ax3 = plt.subplot(3, 1, 3)
    plt.scatter(Dx1_list, Dy1_list, color = 'red', marker = 'o')
    plt.scatter(Dx2_list, Dy2_list, color = 'blue', marker = 'v')
    plt.show()





