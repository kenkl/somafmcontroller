#  SomaFM Controller

A companion to my [somafmplayer](https://github.com/kenkl/somafmplayer) project...

[somafmplayer](https://github.com/kenkl/somafmplayer) is a little Flask shim that drives mplayer to play a stream from the [SomaFM](https://somafm.com/) online radio (commercial-free, independent, listener-supported) station. 

This project is a simple TKinter application used to select/play a stream on the player. It pulls a list of available streams from [somafmplayer](https://github.com/kenkl/somafmplayer), and presents them in the drop-down list. Select one, hit 'PLAY'. Simple.

![alt text](https://i.imgur.com/nmfmB41.png "somafmcontroller ui")

2021-06-12: I've updated [somafmplayer](https://github.com/kenkl/somafmplayer) to pull the full streams list from SomaFM, changing the semantics of selecting/starting a stream. That necessitated changes to this controller to call the right way to the player.
