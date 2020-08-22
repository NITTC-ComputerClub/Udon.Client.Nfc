## これは何
Udonのクライアントサイド  
NFC情報を読み取り、サーバーへ送信し認証する
## 開発時の環境
- PaSoRi(Sony RC-S380)
- Python 3.7.3
- pip 18.1
- Raspberry Pi model 3B(たぶん)
### モジュール
- nfcpy
## 初期設定
初期ではsudoしないと使えないが、推奨されないので設定を行う。  
ホントはrequirements.txtとか書くべきなのでそのうちやります]
```
pip3 install nfcpy
```
その後、
```
python3 -m nfcpy
```
すると、何すればいいか書いてある。具体的には
```
-- better assign the device to the 'plugdev' group  
   sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\",   
   ATTRS  {idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'  
   sudo udevadm control -R # then re-attach device  
```
みたいな部分、**表示された**コマンド(sudo -sh c 'echo ...と、sudo udevadm ...)を実行し、PaSoRiを抜き差しする  
(ここは調べたら再起動とか書いてあったので、ダメならそうしてください)  
[参考記事](https://qiita.com/irutack/items/61a783eb9d5c78d5a3f6)

```
lsusb
```
を実行して、
```
  Bus 001 Device 004: ID 054c:06c3 Sony Corp. RC-S380
  Bus 001 Device 005: ID 0424:7800 Standard Microsystems Corp.   
  Bus 001 Device 003: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub  
  Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub  
  Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
```
みたいに認識されてたらOKです  

## 手動システム起動
```
./main.sh
```

## 新規タグ登録
```
./registrar.sh
```

## 注意点
- python2系での動作は保証されません、必ずpython**3**コマンドで実行してください。
- 起動用のシェルスクリプトは初回だと権限で弾かれると思うので、
```
chmod 755 main.sh
chmod 755 registrar.sh
```
とかすると通ると思います
- 特に手動で止める機会はないと思いますが、  
Ctrl + cしても止まらないので
```
ps u
```
を叩いて
```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
pi         727  0.0  0.2   6992  2572 tty1     S+   13:33   0:00 -bash
pi        1785  0.0  0.3   7016  3232 pts/0    Ss   13:45   0:00 bash
pi        2229  3.7  1.7  41636 16236 pts/0    Sl   13:48   0:00 python3 ./scripts/main.py
pi        2404  0.0  0.2   8288  2532 pts/0    R+   13:48   0:00 ps u

```
で出たプロセスを
```
kill 2229
```
とかしてください 

