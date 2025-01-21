# Climb Compe Result
クライミングジムコンペのリザルト入力と集計用のWEBアプリ開発
<br>
# URL
[streamlit climb compe result](https://appclimbcompeapp-8qmglktavkwftccrnafe4r.streamlit.app/)<br>
管理ページログイン<br>
テスト用ユーザー名：abc<br>
テスト用パスワード：123<br>
<br>
# 概要
2024年3月からPythonを学び始め、5月にPython3エンジニア認定基礎試験の合格を得たとき、学んだことを形にする上で何かWEBアプリを作れないかと模索しました。<br>
そのときに思いついたのが、行きつけのクライミングジムでのコンペのリザルト入力と集計を簡素化するためのアプリでした。<br>
マルチセレクトで登った課題を選択し、得点の自動計算とエクセルでのダウンロードを必須機能として色々と調べた結果、デプロイまでのハードルが低いStreamlitとSQLiteを用いて作成しました。<br>
sessionstateでの入力内容の保持、multiselectの挙動の正常化、エクセルへの変換に苦戦しましたが、何とか最低限の機能を有するものができました。<br>
初めて作成したアプリなので足りない機能が多々ありますが、理解を深めていく中で実装できればと思っています。
<br>
# デモ
![GIF_20240717_143450_264](https://github.com/user-attachments/assets/d58e302f-52be-479f-901f-3f70027f7cf0)
<br>
# 環境
Python==3.12.3<br>
streamlit==1.35.0<br>
pandas==2.2.2<br>
openpyxl==3.1.3

