# パッケージ説明
![test](https://github.com/pl1-NT/mypkg/actions/workflows/test.yml/badge.svg)
* ros2パッケージです
# 動作環境
* ubuntu20.04
* ROS2 foxy
# テスト環境
* ubuntu22.04
* ROS2 humble 
# インストール
* 当パッケージはROS2環境が用意されていることを前提としています。
  ```
  $ cd ros2_ws/src
  $ git clone {https}
  $ (cd ~/ros2_ws && colcon build)
  ```
# ノード説明
* 当パッケージは"talker","listener"によって構成されています。
## talker.py
* 誕生月を入力することで、対応する誕生石を教えてくれるサービスです。
### 使用法
* 端末１
  ```
  $ ros2 run mypkg talker
  ```
* 端末２
  ```
  $ ros2 service call /query2 person_msgs/srv/Query2 "birthmonth: {任意の１～１２までの月}"
  ```
* 出力結果
　端末２に出力されます。
  ```
  response:
  person_msgs.srv.Query2_Response(birthstone='{対応する誕生石}')
  ```
## listener.py
* 月の誕生石をリスト化して表示するサービスです。  
### 使用法
* 端末１
  ```
  $ ros2 run listener
  ```
* 端末２
  ```
  $ ros2 run talker
  ```
* 出力結果
  ```
  [INFO] [1704091524.926019416] [listener]: 待機中
  [INFO] [1704091525.929169176] [listener]: 待機中
  [INFO] [1704091526.932590980] [listener]: 待機中
  [INFO] [1704091527.437147346] [listener]: 1月の誕生石: garnett
  [INFO] [1704091527.439808260] [listener]: 2月の誕生石: amethyst
  [INFO] [1704091527.442079308] [listener]: 3月の誕生石: aquamarine
  [INFO] [1704091527.444232334] [listener]: 4月の誕生石: diamond
  [INFO] [1704091527.446420997] [listener]: 5月の誕生石: emerald
  [INFO] [1704091527.448482805] [listener]: 6月の誕生石: moonstone
  [INFO] [1704091527.450940213] [listener]: 7月の誕生石: ruby
  [INFO] [1704091527.453460898] [listener]: 8月の誕生石: peridot
  [INFO] [1704091527.455671132] [listener]: 9月の誕生石: sapphire
  [INFO] [1704091527.458224729] [listener]: 10月の誕生石: tourmaline
  [INFO] [1704091527.460483176] [listener]: 11月の誕生石: topaz
  [INFO] [1704091527.462470388] [listener]: 12月の誕生石: tanzanite 
  ```
# ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
