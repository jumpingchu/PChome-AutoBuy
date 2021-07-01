# PChome 24h 自動化搶購

## 功能

* 自動化快速搶購 PChome 24h 指定網頁之商品

## 使用工具

* Python
* Selenium
* requests
* Chrome browser

## 使用方法

1. 將 repo 複製到自己的資料夾，並安裝需要的套件
    ```bash
    $ git clone https://github.com/jumpingchu/PChome-AutoBuy.git
    $ cd PChome-AutoBuy
    $ pip install -r requirements.txt
    ```
2. 準備 chromedriver
   
   * **MacOS**：
      1. 安裝 chromedriver
        ```bash
        $ brew install chromedriver
        ```
        ![install_driver_mac](images/install_driver_mac.png)

      2. `settings.py` 的 `DRIVER_PATH` 填入上面顯示的路徑（如：/usr/local/bin/chromedriver）
   
   * **Windows**：
      1. 在 Chrome 網址列輸入 `chrome://settings/help` 確認自己的 Chrome 版本（本人是使用 v91.0）
      2. 下載對應 Chrome 版本的 `chromedriver.exe` 並放在同個資料夾內 ([前往下載](https://sites.google.com/chromium.org/driver/))
   
3. 在 `settings.py` 填入資料（請保管好個資）
   
4. 執行程式
    ```bash
    $ python pchome_autobuy.py
    ```

## 注意事項

1. 可以先拿其他的商品連結做測試，以防搶購時的突發狀況或錯誤（但請記得馬上取消訂單！）
   
2. `settings.py` 內的 `CHROME_PATH` 可讓 chrome 記住登入資訊，可提升搶購速度，建議使用
   
3. 部分程式碼依照每個人不同狀況，需要做一些調整，細節請參閱 [下一小節](#程式執行流程) 或是程式碼註解
     
4. 本專案 **尚未適用** 於數量多於１或必須選擇顏色或樣式的商品

5. 本程式碼單純是提供搶購足夠數量的商品為主，- 禁止用於大量收購並哄抬價格的黃牛行為！-

## 程式執行流程

1. 進入商品頁連結、取得商品 ID，判斷商品是否開賣（若未開賣則會 1 秒後重試，達 5 次即停止）
   
2. 將商品加入購物車
   
3. 前往購物車
   
4. 登入帳戶（若有使用 CHROME_PATH 記住登入資訊，要記得拿掉）
   
5. 點選一次付清 (或是使用 LINE Pay)
   
6. 提示訊息點擊「確定」（疫情期間的特別狀況，某些商品不會出現）
   
7. 填入身分證字號和生日等個資（若帳號有設定記住付款資訊，要記得拿掉）
   
8.  填入信用卡安全碼三碼
   
9.  勾選同意（若帳號有設定記住付款資訊，要記得拿掉）
    
10. 點擊送出訂單

## FAQ
  
### 程式沒有繼續進行下一個步驟？

* 通常是因為前一個步驟無法執行，請檢查程式碼是否有按照正確順序進行
  
* 例如：發現進入購物車頁面卻沒有點選「一次付清」，有可能是前面的登入步驟已被省略但程式沒有註解掉，導致找不到登入的位置

### 使用了 CHROME_PATH 卻還是要重新登入？

* 可能是 CHROME_PATH 設定有誤，導致登入 session 沒有成功被瀏覽器紀錄
  
* 可能的解決方法可參考 [#8](/jumpingchu/PChome-AutoBuy/issues/8)

## 貢獻

* 如果你有想要新增的功能，或是你有發現 bug，歡迎隨時發 Issue 或是發 PR 喔！
  
* 感謝 [sheway](https://github.com/sheway) 提供新的功能與想法
