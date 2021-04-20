from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtMultimediaWidgets import *
from PySide2.QtMultimedia import *
import sys
from realplayerui import *


class video_player(Ui_window):
    '''让自己重写的类继承生成的ui类，就可以用self.setupui方法载入控件，然后也可以用self.labels或self.play_btn直接取出控件操作'''
    def __init__(self):
        self.windows=QMainWindow()
        self.setupUi(self.windows)
        self.player = QMediaPlayer(self.windows)
        self.player.setVideoOutput(self.videowidget)
        self.player.setVolume(50)
        self.windows.show()
        self.fullscreenflag = False

        self.play_btn.clicked.connect(self.playvideo)
        self.pause_btn.clicked.connect(self.pausevideo)
        self.volume_slider.valueChanged.connect(self.setVolume)
        self.select_video_btn.clicked.connect(self.choicefile2play)
        self.player.durationChanged.connect(self.setvideodurition)
        self.player.positionChanged.connect(self.setPlayProgress)
        self.play_progress_slider.sliderPressed.connect(self.playProgressSliderPressed)
        self.play_progress_slider.sliderReleased.connect(self.playProgressSliderReleased)
        self.play_progress_slider.ClickedValue.connect(self.playProgressSliderClicked)
        self.videowidget.doubleclicked.connect(self.videodoubleclicked)

    def playvideo(self):
        self.player.play()
    def pausevideo(self):
        self.player.pause()
    def setVolume(self):
        if self.volume_slider.value():
            self.player.setMuted(False)
            self.player.setVolume(self.volume_slider.value())
        else:
            self.player.setMuted(True)

    def choicefile2play(self):
        self.fileDialog = QFileDialog(self.select_video_btn)
        self.moviepath=self.fileDialog.getOpenFileName(self.select_video_btn,caption='打开视频')[0]
        if self.moviepath:
            self.player.setMedia(QMediaContent(self.moviepath)) #这个是选择播放的重要一环，把视频内容放上去
            self.player.play()
            self.video_line_edit.setText(self.moviepath)
        else:
            return


    def setPlayProgress(self):
        self.right = self.play_progress_label.text().split('/')[-1]
        self.position = self.player.position()
        self.second = int(self.position / 1000 % 60)
        self.minute = int(self.position / 1000 / 60)
        self.left = str(self.minute).zfill(2) + ':' + str(self.second).zfill(2)
        self.play_progress_label.setText(self.left + '/' + self.right)
        self.duration=self.player.duration()+1
        self.percent=round(self.position/self.duration,2)
        self.positions=self.percent*self.play_progress_slider.maximum()
        self.play_progress_slider.setValue(self.positions)

    def setvideodurition(self):
        self.left=self.play_progress_label.text().split('/')[0]
        self.second = int(self.player.duration() / 1000 % 60)
        self.minute = int(self.player.duration() / 1000 / 60)
        self.videoduration=str(self.minute).zfill(2) + ':' + str(self.second).zfill(2)
        self.play_progress_label.setText(self.left + '/' + str(self.videoduration))
        self.maximunofslider = round(self.player.duration() / 5000)#前进一步5秒
        self.play_progress_slider.setMaximum(self.maximunofslider)

    def playProgressSliderPressed(self):
         if self.player.state() != 0:
             self.player.pause()

    def playProgressSliderReleased(self):
         if self.player.state() !=0:
             self.value = round(self.play_progress_slider.value() / self.play_progress_slider.maximum() * self.player.duration())
             self.player.setPosition(self.value)
             self.player.play()

    def playProgressSliderClicked(self):
        self.point = round(self.play_progress_slider.value()/self.play_progress_slider.maximum()*self.player.duration())
        self.player.setPosition(self.point)
        self.player.play()

    def videodoubleclicked(self):
        if self.fullscreenflag ==False:  #当它不是全屏时,执行下面的语句(但是self.fullscreenflag==False要为正确判断)
            self.videowidget.setParent(self.windows)
            '''***上面这一步最重要:当你要为主窗口时,必须先让自己的parent为一个主窗口;然后再用setwindowflag设置为主窗口,不然切换会有问题***'''
            self.videowidget.setWindowFlag(Qt.Window)
            self.videowidget.showFullScreen()
            self.stackedWidget.removeWidget(self.videowidget)
            self.fullscreenflag = True
        else:
            self.videowidget.showNormal()
            self.videowidget.setParent(self.stackedWidget)
            self.stackedWidget.addWidget(self.videowidget)
            '''上面建立一个stackedWidget可以通过addWidget方法,removeWidget方法和setCurrentWidget方法进行控件管理,使其不会离开控件相对位置'''
            self.stackedWidget.setCurrentWidget(self.videowidget)
            self.fullscreenflag = False

app = QApplication(sys.argv)
myplayer = video_player()
sys.exit(app.exec_())