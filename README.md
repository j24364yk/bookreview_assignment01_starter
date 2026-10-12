# 課題1 Book Review DB統合Webアプリ

## 学生情報

- 学籍番号：
- 氏名：

---

## 1. アプリ概要

<!-- 最終提出までに自分の言葉で記述する -->

---

## 2. 実行方法

### ライブラリのインストール

```bash
python -m pip install -r requirements.txt
```

### APIサーバの起動

```bash
cd src
python -m uvicorn main:app --reload
```

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### フロントエンド

```text
http://127.0.0.1:8000/frontend/index.html
```

---

## 3. ディレクトリ構成

```text
bookreview/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── data/
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── docs/
│   ├── data_design.md
│   └── api_design.md
├── requirements.txt
└── README.md
```

---

## 4. 実装済み機能

<!-- 第5回までに実装した機能を整理する -->

- [ ] Book登録
- [ ] Book一覧取得
- [ ] Book詳細取得
- [ ] Book削除
- [ ] Review登録
- [ ] Review取得
- [ ] Review削除
- [ ] Book削除時の関連Review削除
- [ ] ratingの1〜5制約
- [ ] Plain JavaScript画面との統合

---

## 5. 設計上のポイント

<!-- データ構造、API、保存方法、整合性について説明する -->

---

## 6. 未完成部分・既知の問題

<!-- 未完成や不具合がある場合は整理して書く -->
