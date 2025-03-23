## base image
FROM jupyter/base-notebook:latest

USER root

# lhafile のインストールに必要なパッケージと、日本語ロケール設定に必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    locales \
    curl \
    gcc \
    python3-dev && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 環境変数の設定 (LegacyKeyValueFormat 警告を避ける形式に修正)
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

USER ${NB_USER}

RUN pip install --upgrade pip

# Jupyter関連パッケージをインストール
RUN pip install ipykernel notebook jupyterlab

# mysql-connector-python をインストール
#RUN pip install mysql-connector-python

# requirements.txt をコンテナにコピー
COPY requirements.txt /tmp/

# requirements.txt に基づいてパッケージをインストール
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# カーネルを明示的に設定
RUN python -m ipykernel install --user --name=python3

# jupyter labをデフォルトで起動するように設定
#ENV JUPYTER_ENABLE_LAB=yes