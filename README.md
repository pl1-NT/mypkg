# パッケージ説明
![test](https://github.com/pl1-NT/mypkg/actions/workflows/test.yml/badge.svg)
* ROS2のサービスの立ち上げと呼び出しができるパッケージです.サービスファイルは[person_msgs](https://github.com/pl1-NT/person_msgs "サービスファイル")内のQuery2.srvが使用されています.
# テスト済環境
* Ubuntu22.04
* ROS2 humble
* Python 3.7~3.10
* 上記のテストには、上田隆一氏作成のコンテナを使用しました。 
  * [dockerリンク](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2 "link")
# インストール
* 当パッケージはROS2環境が用意されていることを前提としています。
  ```
  $ cd ros2_ws/src
  $ git clone https://github.com/pl1-NT/mypkg.git
  $ (cd ~/ros2_ws && colcon build)
  ```
# ノード説明
* 当パッケージは"talker.py","listener.py","talk_listem.launch.py"によって構成されています。
## talker.py
* 誕生月を入力することで、対応する誕生石を教えてくれるサービス、"query2"を立ち上げるノードです。
### 使用例
* 端末１
  talkerの立ち上げ
  ```
  $ ros2 run mypkg talker
  ```
* 端末２
  サービスの呼び出し
  ```
  $ ros2 service call /query2 person_msgs/srv/Query2 "birthmonth: {任意の１～１２までの月}"
  ```
* 出力結果例
　端末２に出力されます。
  ```
  response:
  person_msgs.srv.Query2_Response(birthstone='{対応する誕生石}')
  ```
## listener.py
* サービスから誕生石のリストを呼ぶノードです。  
### 使用例
* 端末１
  ```
  $ ros2 run mypkg listener
  ```
* 端末２
  ```
  $ ros2 run mypkg talker
  ```
* 出力結果例
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
## talk_listen.launch.py
* サービスの立ち上げと呼び出しを同時に行うlaunchファイルです。
### 使用例
 ```
 $ ros2 launch mypkg talk_listen.launch.py
 ```
* 出力結果例
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
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
* このパッケージのコードは下記のスライド(CC-BY-SA 4.0 by RyuichiUeda)のものを本人の許諾のもと一部改変、自身の著作としたものです。
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/ "利用したスライド")
*  © 2023 Touki Nishi 
