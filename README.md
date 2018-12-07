# DiscomfortIndexSystem
TH02で不快指数を出すシステム

TH02仕様書：http://www.hoperf.com/upload/sensor/TH02_V1.1.pdf

TH02を使った先駆者のソースコード(Arduino)：https://github.com/Seeed-Studio/Grove_Temper_Humidity_TH02

- TH02クラス-> TH02モジュール(温湿度センサの動作)
    - コンストラクタ\-> バスのセットアップ
    - readTemp \-> 温度読み取り
    - readHum \-> 湿度読み取り
    - outputDI \-> 不快指数の出力

- main()関数
    - \#display() \-> GUIで表示したかったけど時間が無くて断念
    - 温度・湿度を表示してから、不快指数の計算を行い、表示する
    - 温度と湿度を連続して取得するとき、**一度値を棄却しないと正常に取得できない**。メモリの問題？？？

