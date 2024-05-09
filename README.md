# Streamlit Chatbot Ollama

Streamlitを使用して構築されたチャットボットアプリケーションです。モデルとしてOllamaを使用し、ユーザーとの対話を通じてリアルタイムで応答を生成します。

## ollamaでローカルモデルを使ってみる。
[ryota39-Phi-3-mini-4k-instruct-dpo](https://huggingface.co/mmnga/ryota39-Phi-3-mini-4k-instruct-dpo-gguf)を遊んでみたくて、langchainからollamaの呼び出しを試して見ました。

## Ollamaとモデルの準備
1. 予めモデルをダウンロードして保存する。
2. モデルファイル作成する。パスは絶対パスでないといけないかも。[sample](https://github.com/chottokun/learn_ollama_stremlit/blob/main/modelfieforphiinstdop.exsample)の「FROM /home/foobar/ryota39-Phi-3-mini-4k-instruct-dpo-gguf」のパスを設定する。
3. ollama上でモデルを作成する。
```
ollama create ryota39-Phi-3-mini-4k-instruct-dpo-Q4_0.gguf -f modelfile
```
4. ollama
```
ollama serve
ollama run ryota39-Phi-3-mini-4k-instruct-dpo-Q4_0.gguf
```

## streamlit
```
streamlit run streamlit_chatbot_ollama.py
```
※あらかじめ必要なライブラリはpipenvのpipfileでインストールしておくこと。

## 機能メモ

- **ストリーミング**: ユーザーからの入力に対して、リアルタイムで応答を生成します。
- **履歴管理**: 過去のメッセージ履歴を保持し、対話の文脈を維持します。


## 利用ライブラリ

- **Streamlit**: ウェブアプリケーションのフロントエンド
- **LangChain**: LLMの超定番
- **ollama**:　ローカルでLLMのモデル管理と実行

## 参考
- https://github.com/shashankdeshpande/langchain-chatbot
- https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history/
- https://note.com/lucas_san/n/n388aa16c6766
