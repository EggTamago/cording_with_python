from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import numpy as np
import os
import time

# 参考：https://hituji-ws.com/code/python/face_reco/

# 類似度の関数
def cos_similarity(p1, p2): 
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

def facenet():
    # 顔検出のAI
    # image_size: 顔を検出して切り取るサイズ
    # margin: 顔まわりの余白
    mtcnn = MTCNN(image_size=160, margin=10)
    
    # 切り取った顔を512個の数字にするAI
    # 1回目の実行では学習済みのモデルをダウンロードしますので、少し時間かかります。
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    pwd = os.getcwd()
    image_path1 = "/root/enjoy_cording_with_python/Twins-detection/ai/images/0.jpg"
    image_path2 = "/root/enjoy_cording_with_python/Twins-detection/ai/images/1.jpg"

    while(not os.path.exists(image_path1)):
        time.sleep(0.5)
        print("checking path 1")
    
    while(not os.path.exists(image_path2)):
        time.sleep(0.5)
        print("checkint path 2")

    # 画像データ1
    img1 = Image.open(image_path1) 
    img_cropped1 = mtcnn(img1)
    img_embedding1 = resnet(img_cropped1.unsqueeze(0))
    
    # 画像データ2
    img2 = Image.open(image_path2)
    img_cropped2 = mtcnn(img2)
    img_embedding2 = resnet(img_cropped2.unsqueeze(0))
    
    # 配列へ変換
    p1 = img_embedding1.squeeze().to('cpu').detach().numpy().copy()
    p2 = img_embedding2.squeeze().to('cpu').detach().numpy().copy()
    
    # 類似度を計算して顔認証
    img1vs2 = cos_similarity(p1, p2)
    
    return round(img1vs2, 2)

if __name__ == '__main__':
    facenet()
