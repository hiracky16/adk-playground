# GenAI Toolbox Agent

ホテル検索・予約システムのためのAIエージェントアプリケーション

## 概要

このプロジェクトは、Geminiモデルを利用したホテル検索・予約用のAIアシスタントを提供します。ユーザーは自然言語でホテルの検索、予約、キャンセルなどの操作を行うことができます。

## 主な機能

- ホテル名での検索
- 場所（ロケーション）での検索
- ホテルの予約
- 予約の更新（チェックイン・チェックアウト日の変更）
- 予約のキャンセル

## 技術スタック

- **AIモデル**: Gemini 2.0 Flash
- **フレームワーク**: Google ADK (Agent Development Kit)
- **データベース**: BigQuery
- **コンテナ環境**: Docker & Docker Compose

## プロジェクト構成

```
genai-toolbox-agent/
├── compose.yml              # Dockerコンテナ定義
├── README.md                # このファイル
├── hotel_agent/             # ホテル予約AIエージェント
│   ├── Dockerfile           # エージェントのコンテナ定義
│   ├── requirements.txt     # Pythonパッケージ依存関係
│   └── agent/               # エージェントコード
│       ├── __init__.py
│       └── agent.py         # AIエージェントの定義
└── toolbox/                 # ツールボックス設定
    └── sample_tools.yml     # 実際に使用するツール定義
```

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

## ツールの設定

`toolbox/tools.yml` ファイルでは、以下のツールが定義されています：

- `search-hotels-by-name`: ホテル名による検索
- `search-hotels-by-location`: ロケーションによる検索
- `search-hotels-by-everything`: 複合条件による検索

## 注意事項

- このプロジェクトはAsia Northeast 1リージョンのBigQueryを使用しています
- プロダクション環境での使用前に、セキュリティ設定を確認してください
