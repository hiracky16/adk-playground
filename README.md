# ADK Playground


## travel_agent
ホテル検索や旅行支援 AI エージェントアプリケーション

## 概要

このプロジェクトは、Geminiモデルを利用した旅行のプランニングやホテル検索のAIアシスタントを提供します。ユーザーは自然言語でプランの検討やホテルの検索などの操作を行うことができます。

## 主な機能

- 旅行プランの検討
- ホテル名での検索
- 場所（ロケーション）での検索

## 技術スタック

- **AIモデル**: Gemini 2.0 Flash
- **フレームワーク**: Google ADK (Agent Development Kit)
- **データベース**: BigQuery
- **コンテナ環境**: Docker & Docker Compose

## セットアップと実行方法

### 前提条件

- Docker および Docker Compose がインストールされていること
- Google Cloud Platform のアカウントと認証情報
- BigQuery プロジェクトへのアクセス権限

### 環境変数の設定

`.env` ファイルを作成し、以下の環境変数を設定します：

```
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="あなたのGoogleAPIキー"
```

### 実行方法

1. Docker Composeでサービスを起動します：

```bash
docker compose up
```

2. ブラウザで http://localhost:8000 にアクセスしてAIアシスタントを利用できます。
