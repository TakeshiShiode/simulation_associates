=========================================
ダウンロードはこちらから
=========================================

:エミュレータ: QEMU-8.1.0
:確認用サンプルプログラム: STM32CubeIDEプロジェクト

.. ハイパーリンク定義
.. _Githubのリポジトリ: https://github.com/TakeshiShiode/QEMU-develop.git
.. _MSYS2: https://www.msys2.org/
.. _こちら: https://wiki.qemu.org/Hosts/W32#Native_builds_with_MSYS2

サンプルプログラムダウンロード
==============================

`Githubのリポジトリ`_ からまとめてダウンロードできます。

ソフトウェア機材類
==================

* `MSYS2`_ : QEMUのmake用。makeについての説明は `こちら`_ (Native builds with MSYS2の項目参照)

QEMUのmakeについて
==================

makeも前述のNative builds with MSYS2の項に記載がありますが、全makeされるため時間が掛かってしまいます。
以下のように、arm周りに限定すると若干早くなります。

::

   MSYS2上でQEMUを置いたディレクトリに移動して
   
   makdir build //buildフォルダを作る
   cd build     //buildフォルダに移動
 
   ../configure --prefix=/c/QEMU置いたフォルダ/出力フォルダ名 --target-list=arm-softmmu --enable-gtk --enable-sdl

   make
   make install



