#copyメソッド(a = b.copy)は普通の代入(a=b)と何が違う？

'''
普通の代入が参照渡しなのにたいして、copyを使うと値渡し
'''

import numpy as np

#Reluクラス
class Relu:
    def __init__(self):
        self.mask = None
        

    def forward(self, x):
        self.mask = (x <= 0) #ここは何をしている？
        out = x.copy() # 値渡し //xの値まで変わる？
        out[self.mask] = 0 #ここどういうこと？
        
        b = x.copy() #値渡しのテスト

        '''
        l,17 trueの値を0にする
        '''

        # なぜcopyじゃないといけないのか
        return out,b


    def backward(self,dout):
        dout[self.mask] = 0
        dx = dout

        return dx

#Reluクラスがやっていることはnp配列の要素のうち負のものの値をすべて0にすることである

a = Relu()
list = np.array([[1.0,-1.5],[-2.0, 3.0]])
print(a.forward(list))


#sigmoidクラス
class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self,x):
        out = 1/(1+np.exp(-x))
        self.out = out
        
        return out

    def backward(self, dout):
        dx = dout*(1.0 - self.out)*self.out

        return dx

#affineってなんぞ
'''
アフィン変換
y = wx + b
を出力する層
ひとまず置いておくことにする
'''

