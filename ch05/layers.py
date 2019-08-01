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
        '''   
        ndarrayはmutableなのでリスト自体のidを渡している。よって渡した先で変更があれば、リスト自体にも変更があり、
        '''
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

points

1. 流れるノードは数値から行列になる
2. 乗算ノードではnp.dot計算を行うので掛ける行列の次元の要
素数を一致させないといけない
3. 一致させるためには順序変えたり、転置したりしても良い
'''

#バッチ版のaffineレイヤーはなぜバイアスの計算をいじる？
'''
微分したものの要素数がバイアスの要素数と一緒にならなければならないため

'''

# class Affine

class Affine:
    def __init__(self,w,b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self.db = None

    def forward(self,x):
        self.x = x
        out = np.dot(x,self.w) + self.b

        return out

    def backward(self,dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T,dout)
        self.db = np.num(dout,axis = 0)

        returndx

