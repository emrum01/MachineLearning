#加算ノードの逆伝搬　とは
'''
加算ノードは上流から伝わってきたノードに１をかけて下に流す

その下のノードで足したかずについて偏微分したものを伝わってきた
ノードにかけて流していく
'''

#乗算ノードの逆伝搬　とは
'''
乗算ノードでは入力信号と逆のほうをかけて下に流す

ある乗算ノードでx,yが乗算されていて、
z == xy
であるとする。このとき
dz/dx　== y, dz/dy == x
となっていて、偏微分に使ってない変数が残っていることがわかる。

だから入力信号をひっくり返したほうをかけて下に流す。
'''

class MulLayer:
    def __init__(self): #コンストラクタ
        self.x = None
        self.y = None

    def forward(self,x,y):#値のセットと計算とその結果を返す
        self.x = x 
        self.y = y 
        out = x*y
        
        return out

    def backward(self,dout):#逆伝搬の乗算ノード
        dx = dout*self.y    #doutは伝わってきた値   
        dy = dout*self.x

        return dx,dy

class Addlayer:
    def __init__(self):
        pass #何もしないということ

    def forward(self, x, y): #加算ノードの順伝搬
        out = x + y

        return out

    def backward(self,dout): #加算ノードの逆伝搬
        dx = dout * 1
        dy = dout * 1
        
        return dx, dy

#以下リンゴの実装

apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer() #コンストラクタ生成
mul_tax_layer = MulLayer()

#まず順伝搬を計算
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price,tax)

print(price)

#次に逆伝搬
dprice = 1
dapple_price,dtax = mul_tax_layer.backward(dprice)
print (mul_tax_layer.__dict__.values())

dapple,dapple_num = mul_apple_layer.backward(dapple_price)
print (mul_apple_layer.__dict__.values())
print(dapple,dapple_num,dtax)

#なぜbackwardは引数一つか？
'''
backwardクラスのなかで順伝搬の時にsetされたフィールド変数を呼び出しているから
'''

#backwardを複数回実行するときノードのフィールド変数はどこで更
# 新されている？
'''
そもそもmul_apple_layerとmul_tax_layerでことなる
インスタンスを作っているので更新もくそもない

これらのインスタンス変数はforwardで初期化されている。
'''

