==============================
サンプルプログラムの作成と実行
==============================
:確認用サンプルプログラム: STM32CubeIDEによるFreeRTOS環境
:統合環境: STM32CubeIDE
:デバッガ: Arm GNU Toolchainよりarm-none-eabiデバッガ(windows用)

.. _STM32CubeIDE: https://www.st.com/ja/development-tools/stm32cubeide.html
.. _Arm GNU Toolchain: https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads

サンプルプログラムの作成
========================

STM32CubeIDE(統合環境)のインストール
------------------------------------
`STM32CubeIDE`_ のサイトからwindows用のインストーラをダウンロードして実行


プロジェクトの作成
------------------
STM32CubeIDEを起動すると :numref:`Fig2` の"ようこそ画面"が開くので"Start_new_STM32_project"をクリック
(開かない場合はツールバーのHelp->information Centerでも開けます)

.. _Fig2:
.. figure:: fig2.jpg
   :scale: 60%
   :align: center

   :STM32起動画面

少し(ソフトが)悩んだ後、"Target_Selecton"画面が開くので、画面左側の"PRODUCT_INFO->series"で"STM32F7"ボックスにチェックを入れて、
画面右半分下のアイテム表で"Bord"の項をクリックして並び替えると 欄内に"NUCLEO-F756ZG"が出てくるので選択してnextをクリック。

.. _Fig3:
.. figure:: fig3.jpg
   :scale: 60%
   :align: center

   :基板環境選択画面

プロジェクト名を聞かれるので、適当に入力(nucleo-stmf746としました)。nextをクリックするといろいろ出ますが、
そのままの設定で"Finish"と"Yes"をクリック。

.. _Fig4:
.. figure:: fig4.jpg
   :scale: 60%
   :align: center

   :NUCLEO-F756ZGでのプロジェクト作成


FreeRTOSの追加
==============

プロジェクトの作成が完了すると以下の図の状態になります。ここでProjectExplorerのとなりの選択メニューから"Middleware"->"FREERTOS"を選択。
ここからFreeRTOSの設定になります。

.. _図5:
.. figure:: fig5.jpg
   :scale: 67%
   :align: center

   :FreeRTOSの設定

"Config_parameters"で使用するバージョンを選択します。ネット情報を参考に今回は"CMSIS_V1"としました。

.. _Fig6:
.. figure:: fig6.jpg
   :scale: 60%
   :align: center

   :FreeRTOSバージョンの選択

まず、"System_Core"メニューからRTOSが使用するベースタイマを設定します。これもネットの受け売りですが、
SysTick以外のタイマの使用を推奨とのことですので、
今回QEMUで追加したTIM6を設定します。

.. _Fig7:
.. figure:: fig7.jpg
   :scale: 55%
   :align: center

   :FreeRTOS基本タイマの設定

次にテスト用のタスク追加します。FreeRTOSのConfiguraton画面に戻って"Task_and_Queues"を選択し"Tasks枠"の"Add"をクリックすると
追加するタスクの設定枠が出てくるので、スタックサイズなどを設定してOKとします。今回はテストなのでそのままOKとしています。

.. _Fig8:
.. figure:: fig8.jpg
   :scale: 55%
   :align: center

   :タスクの設定(今回はデフォルト設定で2タスク追加しました)

設定が完了したので、"ProjectExplorer"にあるプロジェクト名.ioc(ここでは"nucleo-stm32f746.ioc")を右クリックして"Generate_Code"
をクリックするとFreeRTOS環境がプロジェクトに追加されます。

.. _Fig9:
.. figure:: fig9.jpg
   :scale: 60%
   :align: center

   :FreeRTOS環境が生成されプロジェクトに追加

以上がFreeRTOSの追加作業だったのですが、「RTOSのポーティングってこんなに簡単でいいんだっけ？」
ていうくらい、あっけなく完了してしまいました。その簡単さブルワーカー並み、マウスでポチポチしかしていないような．．．

　　　　　　　　　　　　　　「まったく・簡・単だ」。



デバッガのインストールと設定
============================
`Arm GNU Toolchain`_ のサイトよりwindows用のファイルをダウンロードして解凍し、適当な場所に置きます。
パスの設定は必ずしも必要ではありません。以下 に示すようにCubeIDEのデバッガの設定に登録します。

.. _Fig10-2:
.. figure:: fig10-2.jpg
   :scale: 85%
   :align: center

   :STM32CubeIDEでのデバッグ設定メニューへの入り方(eclipseと同じ)

"Debug_Configurations"画面の"Debugger"タブを図のように設定したら"Apply"をクリックして
いったん閉じます。リモートデバッグ方式となるので、デバッガ.exeだけでなく、"JTAG_Device"のTCP/IP設定や、"localhost:1234"の設定も必要です。

.. _Fig10:
.. figure:: fig10.jpg
   :scale: 85%
   :align: center

   :デバッガの設定画面


サンプルプログラムの実行
========================
テスト用のサンプルプロジェクトが出来たので、QEMU上で走らせてみます。

プロジェクトのビルド
--------------------
"ProjectExplorer"上でプロジェクトを選択して"Build_Project"をクリックするとビルドが始まります。
完了すると、プロジェクトフォルダ下の"Debug"フォルダの下にプロジェクト名.elf(今回はnucleo-stm32f746.elf)が作られます。
これをQEMUとSTM32CubeIDEから実行時に参照します。

.. _Fig12:
.. figure:: fig12.jpg
   :scale: 75%
   :align: center

   :サンプルプロジェクトのビルド

QEMUの実行
----------
QEMUをmakeする際に使用したMSYS2上で、QEMUの実行ファイル(qemu-system-arm.exe)がある場所へ移動します。
そこで、今回追加したSTM32F746エミュレータ(nucleo-stm32-f746)と先ほどビルドしたプロジェクト名.elfを指定してQEMUを実行。

::

   ./qemu-system-arm -S -gdb tcp::1234 -M nucleo-stm32-f746 
    -kernel /c/STM32CubeIDEワークスペース名/nucleo-stm32f746/Debug/nucleo-stm32f746.elf


.. _Fig11:
.. figure:: fig11.jpg
   :scale: 60%
   :align: center

   :MSYS2上でQEMUの起動


サンプログラムの実行
--------------------
最後に、STM32CubeIDEのデバッガからサンプルプログラムを実行します。デバッガ設定時に参照した、"Debug_Configurations"画面の
、今度は"mainタブ"で、ビルドした.elfファイルを指定します。設定出来たら"Debug"ボタンをクリックすると、QEMU上の
サンプルプログラムが実行されます。

.. _Fig13:
.. figure:: fig13.jpg
   :scale: 70%
   :align: center

   :サンプルプログラムの実行

動作確認
========

スタートアップ
--------------
デバッガの起動に成功すると、まずスタートアップ領域のリセットハンドラに飛んできていったん停止します。ここから、RAM領域の初期化～Sysytem初期化を経て
いわゆるmain関数を呼び出します。この工程はアセンブラです。図では切れていますが、このファイルを下に行くとmain関数が呼び出されています。
ステップ実行しても良いですが、時間がかかるのでmainまで実行します。

.. _Fig14:
.. figure:: fig14.jpg
   :scale: 85%
   :align: center

デバイス初期化とRTOS起動
------------------------
main関数まで来ました。ここでシステムクロックやIO、UART3(シリアルデバッグ用)などのデバイス類を初期化した後、FreeRTOSを起動します。

.. _Fig15:
.. figure:: fig15.jpg
   :scale: 85%
   :align: center

デバイス初期化を抜けて、FreeRTOSの実行部分へ。デフォルトタスク含めタスクを3つ生成した後、"osKernelStart()"で起動します。
問題となっていた"xPortStartScheduler()"はこの中(無事に起動したので省略)。

.. _Fig16:
.. figure:: fig16.jpg
   :scale: 85%
   :align: center

テストタスクの動作確認
----------------------
無事OSが起動して、各タスクが実行されるようになりました。なおタスク2では動作確認用に
UART3を用いてコンソール/ターミナルなどにデバッグ表示しています。

.. _Fig17:
.. figure:: fig17.jpg
   :scale: 85%
   :align: center

以上、サンプルプログラムの実行でした。

