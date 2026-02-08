def start_button_on_click(event):
    """スタートボタンがクリックされたときの処理を行う関数"""
    # スタートボタンを無効化
    document.getElementById("start_button").disabled=True
    # ゲームの初期化
    game["turns"]=GAME_TURNS  # 残りのゲームターン数の初期化
    game["score"]=0  # スコアの初期化
    # ゲームの開始
    next_turn()

def canvas_on_click(event):
    """キャンバスがクリックされたときの処理を行う関数"""
    # クリック位置の取得
    rect=canvas.getBoundingClientRect()
    click_x=event.clientX - rect.left
    click_y=event.clientY - rect.top
    # モグラの位置内がクリックされたか確認
    if (game["mx"] <= click_x <= game["mx"] + WIDTH and
        game["my"] <= click_y <= game["my"] + WIDTH):
        # スコアを加算
        game["score"]+=1
        # モグラを隠す
        game["hide"]=True
