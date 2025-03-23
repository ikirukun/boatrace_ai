競艇予想AIを作るチュートリアルです。機械学習で１着になる選手の予測を出します。

## 環境構築

Docker+Cursor/VSCode+Jupyter notebook

事前にDocker Desktop、Cursor/VSCodeをインストール、VSCodeの拡張機能Dev Containersをインストール

※参考　[DockerとCursorでJupyter Notebook環境を構築する方法（Mac版）](https://note.com/frypan1996/n/nd6f6c5202560)

## コンテナ起動まで

*git clone*

```
git clone https://github.com/ikirukun/boatrace_ai.git

```

デスクトップ上に作成すること前提でdocker-composeを作っていますが、ご自身の環境に応じて変えてください。

dockerの起動

```
cd ~/Desktop/boatrace_ai/devcontainer

docker-compose up -d --build

```

コンテナが立ち上がったら、VSCodeのリモートウィンドウを開いて「実行中のコンテナーにアタッチ」

コンテナ内にPythonとJupyterの拡張機能がインストールされます。

インストールされない場合は手動でインストールすればとりあえず動きます。

## 1.スクレイピング

work/Data_scrapingの1.と2.の.ipynbファイルを実行します。

1.のSTART_DATEとEND_DATEを検証したい期間に設定してください。

## 2.trainデータ作成

work/train_dataの3.と4.の.ipynbファイルを実行します。

4.だけ処理の高速化のため、polarsでデータフレームを処理しています。（結果的に特徴量として使わないので意味ないですが）他のファイルは全てpandasです。

## 3.モデル学習

work/Learning_modelの5.の.ipynbを実行します。

date_split_test = 2405010000　は初期では2024/05/01以降をテストデータとし、それより前を訓練データとしています。

取得する期間などによって、変更してください。YYMMDD+0000形式

## 4.当日分レースの予測

work/daily_predictionsの6.の.ipynbをを実行します。

3.モデル学習で保存した学習済みモデルを使って、その日のレース（未知データ）を予測します。

予測結果は、csvでも保存されますが、webアプリでも見れるようにデータベースにも保存します。

## 5.webアプリケーションの実行（オプション）

予測は前回の4.当日分レースの予測までで終了ですが、予測結果を実際に競艇場に持ち込んで使用する需要があったため、

データを見やすくするためFlaskによる簡単なWebアプリケーションを作りました。

docker-composeファイルにDB（MySQL　ユーザー名などは適宜変更）とFlask appを定義済みですので

コンテナが立ち上がっていれば、
http://localhost:5001
でアクセスできます。
