=========================================
エミュレータの作成とQEMUへの追加
=========================================

:エミュレータ: QEMU-8.1.0
:想定評価ボード: NUCLEO-F746ZG(Nucleo-144:STM32F746ZG)

.. ハイパーリンク定義
.. _STM32F7x6関連のドキュメント: https://www.st.com/en/microcontrollers-microprocessors/stm32f7x6/documentation.html
.. _Issues_#1122: https://gitlab.com/qemu-project/qemu/-/issues/1122

概要
====

QEMUを用いてSTM32F746ZGを想定したエミュレータを作成します。
ベース環境はnetduino2、もしくはolimex-stm32-h405といったSTM32F405環境を参考に
"nucleo-stm32-f746"としてarmエミュレータへ追加しました(qemu-system-arm.exe)。
以下、変更内容です。

変更内容
========

.. list-table:: nucleo-stm32-f746用の変更および追加項目
   :header-rows: 1
   
   * - 項目/名称
     - olimex-stm32-h405
     - nucleo-stm32-f746
     - 備考
   * - SOC(想定)
     - STM32F405H
     - STM32F746ZG
     - `-`
   * - cpu
     - cortex-m4
     - cortex-m7
     - `-`
   * - SRAM
     - 0x20000000～0x20020000
     - 0x20000000～0x20050000
     - 128⇒320KBへ拡張
   * - タイマ
     - TIM2～TIM4
     - TIM2～TIM14
     - ただしTIM1とTIM8を除く
   * - RCC
     - `-`
     - モジュール追加
     - レジスタR/W程度
   * - Flash_IF
     - `-`
     - モジュール追加
     - レジスタR/W程度
   * - UART
     - ch1～7
     - レジスタ追加
     - レジスタR/W程度
   * - NVIC
     - `-`
     - 優先度レジスタ(0xE000E400)変更
     - ※マスク値(0xFF⇒0xF0)

NVIC優先度レジスタの変更について
================================

サンプルプログラム側のFreeRTOSの起動時に"xPortStartScheduler()"にて
"configASSERT"に落ちてしまうため、優先度レジスタを変更しています。

STMさんのサイトより `STM32F7x6関連のドキュメント`_ 「PM0253」の
4.2_ネスト化されたベクタ割込みコントローラ->4.2.7_割込み優先度レジスタ->表_47. IPRビット割当て
を参照し、私なりに解釈すると、

"優先度レジスタは0～255までの値を取れるがcortex-m7では割込み数mが240個のため、ここに0xFF(255)を書いても
読み値は0xF0(240)が返ります"

ということだと思われます(実機ではそうでした)。
ですがQEMU側ではここに255が設定できてしまうためASSERTとなってしまいます。

というわけで、E000E400のマスク値を0xF0としています。
本件については、QEMUサイト側でも課題提起されていますのでいずれ対応されるかもしれません。`Issues_#1122`_ 参照。
