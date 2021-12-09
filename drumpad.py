#2017级 计算机科学与技术4班 王朔 20177840240
#基于Pygame的电子打击乐器 - Sure's Drumpad
#键盘控制键RTYU FGHJ VBNM
import pygame
import ctypes
import os
import time
from pygame.locals import *
from sys import exit
#ctypes库允许python调用dll中的函数

ctypes.windll.user32.SetProcessDPIAware()
res=(ctypes.windll.user32.GetSystemMetrics(0),ctypes.windll.user32.GetSystemMetrics(1))
resX=ctypes.windll.user32.GetSystemMetrics(0)
resY=ctypes.windll.user32.GetSystemMetrics(1)
#获取Windows系统分辨率，禁用窗口采用Windows UI缩放

backgroundColor=(50,50,50)
backgroundUpperColor=(38,38,38)
beforeHitColor=(210,210,210)
afterHitColor=(0,161,233)
titleColor=(0,161,233)
white=(255,255,255)
exitBottonColor=(236,104,65)
presetBottonColor=(50,50,50)
#定义颜色

pygame.init()

pygame.mixer.init(frequency=44100, channels=16)
pygame.mixer.set_num_channels(16)
# 初始化混音器模块并设置混音器通道数量

titleFont=pygame.font.Font('font/pingfangSS.ttf',int(0.06*resX))
subtitleFont=pygame.font.Font('font/pingfangSS.ttf',int(0.03*resX))
bottonFont=pygame.font.Font('font/pingfangSS.ttf',int(0.02*resX))
padFont=pygame.font.Font('font/pingfangSS.ttf', int(0.03*resX))

REFRESH_RATE=20
clock=pygame.time.Clock()

mainScreen=pygame.display.set_mode(res, FULLSCREEN | NOFRAME)
pygame.display.set_caption("Sure's Drumpad")
pygame.display.set_icon(pygame.image.load('image/icon.png'))
mainScreen.fill(backgroundColor)
#创建主窗口并填充背景颜色

hit_pad1=0
hit_pad2=0
hit_pad3=0
hit_pad4=0
hit_pad5=0
hit_pad6=0
hit_pad7=0
hit_pad8=0
hit_pad9=0
hit_pad10=0
hit_pad11=0
hit_pad12=0
#创建各个鼓垫打击判定变量


loc_pad1=(0.025*resX,0.25*resY,0.2*resX,0.2*resY)
loc_pad2=(0.275*resX,0.25*resY,0.2*resX,0.2*resY)
loc_pad3=(0.525*resX,0.25*resY,0.2*resX,0.2*resY)
loc_pad4=(0.775*resX,0.25*resY,0.2*resX,0.2*resY)
loc_pad5=(0.025*resX,0.5*resY,0.2*resX,0.2*resY)
loc_pad6=(0.275*resX,0.5*resY,0.2*resX,0.2*resY)
loc_pad7=(0.525*resX,0.5*resY,0.2*resX,0.2*resY)
loc_pad8=(0.775*resX,0.5*resY,0.2*resX,0.2*resY)
loc_pad9=(0.025*resX,0.75*resY,0.2*resX,0.2*resY)
loc_pad10=(0.275*resX,0.75*resY,0.2*resX,0.2*resY)
loc_pad11=(0.525*resX,0.75*resY,0.2*resX,0.2*resY)
loc_pad12=(0.775*resX,0.75*resY,0.2*resX,0.2*resY)
#创建各个鼓垫位置及大小

loc_exitBotton=(0.95*resX,0,0.05*resX,0.05*resY)
exitBotton=pygame.Rect(loc_exitBotton)

loc_backgroundUpper=(0,0,resX,0.2*resY)
backgroundUpper=pygame.Rect(loc_backgroundUpper)

loc_presetBotton=(0.85*resX,0,0.1*resX,0.05*resY)
presetBotton=pygame.Rect(loc_presetBotton)
#创建各按钮元素位置及大小

pad1=pygame.Rect(loc_pad1)
pad2=pygame.Rect(loc_pad2)
pad3=pygame.Rect(loc_pad3)
pad4=pygame.Rect(loc_pad4)
pad5=pygame.Rect(loc_pad5)
pad6=pygame.Rect(loc_pad6)
pad7=pygame.Rect(loc_pad7)
pad8=pygame.Rect(loc_pad8)
pad9=pygame.Rect(loc_pad9)
pad10=pygame.Rect(loc_pad10)
pad11=pygame.Rect(loc_pad11)
pad12=pygame.Rect(loc_pad12)
#绘制12个未击打时的鼓垫

preset=2
#创建预设标识

while True:
    clock.tick(REFRESH_RATE)

    pygame.mouse.set_visible(True)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    pygame.draw.rect(mainScreen, backgroundUpperColor, backgroundUpper)
    pygame.draw.rect(mainScreen, exitBottonColor, exitBotton)
    pygame.draw.rect(mainScreen, presetBottonColor, presetBotton)

    title=titleFont.render("Sure's Drumpad",1,titleColor)
    mainScreen.blit(title, (0.02*resX,0))

    if preset == 1:
        subtitle1=subtitleFont.render("CSTRIKE",1,white)
        mainScreen.blit(subtitle1, (0.02*resX,0.11*resY))
    if preset == 2:
        subtitle2=subtitleFont.render("ACOUSTIC",1,white)
        mainScreen.blit(subtitle2, (0.02*resX,0.11*resY))
    if preset == 3:
        subtitle3=subtitleFont.render("ELECTRONIC",1,white)
        mainScreen.blit(subtitle3, (0.02*resX,0.11*resY))

    presetBottonText=bottonFont.render("PRESET",1,white)
    mainScreen.blit(presetBottonText,(0.865*resX,0.005*resY))
    exitBottonText=bottonFont.render("EXIT",1,white)
    mainScreen.blit(exitBottonText,(0.955*resX,0.005*resY))

    if preset == 1:
        sound1=pygame.mixer.Sound('sound/cstrike/ak47.wav')
        sound2=pygame.mixer.Sound('sound/cstrike/ak47.wav')
        sound3=pygame.mixer.Sound('sound/cstrike/ak47.wav')
        sound4=pygame.mixer.Sound('sound/cstrike/ak47.wav')
        sound5=pygame.mixer.Sound('sound/cstrike/awp.wav')
        sound6=pygame.mixer.Sound('sound/cstrike/awp.wav')
        sound7=pygame.mixer.Sound('sound/cstrike/awp.wav')
        sound8=pygame.mixer.Sound('sound/cstrike/awp.wav')
        sound9=pygame.mixer.Sound('sound/cstrike/c4.wav')
        sound10=pygame.mixer.Sound('sound/cstrike/c4.wav')
        sound11=pygame.mixer.Sound('sound/cstrike/c4.wav')
        sound12=pygame.mixer.Sound('sound/cstrike/c4.wav')
        presetText="CSTRIKE"
    if preset == 2:
        sound1=pygame.mixer.Sound('sound/acoustic/crash.wav')
        sound2=pygame.mixer.Sound('sound/acoustic/tom1.wav')
        sound3=pygame.mixer.Sound('sound/acoustic/tom2.wav')
        sound4=pygame.mixer.Sound('sound/acoustic/ride.wav')
        sound5=pygame.mixer.Sound('sound/acoustic/openhihat.wav')
        sound6=pygame.mixer.Sound('sound/acoustic/closehihat.wav')
        sound7=pygame.mixer.Sound('sound/acoustic/closehihat.wav')
        sound8=pygame.mixer.Sound('sound/acoustic/tom3.wav')
        sound9=pygame.mixer.Sound('sound/acoustic/snare.wav')
        sound10=pygame.mixer.Sound('sound/acoustic/snare.wav')
        sound11=pygame.mixer.Sound('sound/acoustic/kick.wav')
        sound12=pygame.mixer.Sound('sound/acoustic/kick.wav')
        presetText="ACOUSTIC"
    if preset == 3:
        sound1=pygame.mixer.Sound('sound/electronic/crash.wav')
        sound2=pygame.mixer.Sound('sound/electronic/tom2.wav')
        sound3=pygame.mixer.Sound('sound/electronic/lightning.wav')
        sound4=pygame.mixer.Sound('sound/electronic/ride.wav')
        sound5=pygame.mixer.Sound('sound/electronic/kick1.wav')
        sound6=pygame.mixer.Sound('sound/electronic/effect.wav')
        sound7=pygame.mixer.Sound('sound/electronic/closehihat.wav')
        sound8=pygame.mixer.Sound('sound/electronic/openhihat.wav')
        sound9=pygame.mixer.Sound('sound/electronic/kick2.wav')
        sound10=pygame.mixer.Sound('sound/electronic/snare.wav')
        sound11=pygame.mixer.Sound('sound/electronic/clap.wav')
        sound12=pygame.mixer.Sound('sound/electronic/tom3.wav')
        presetText="ELECTRONIC"
        #从文件创建声音对象


    if (loc_exitBotton[0]+loc_exitBotton[2]) > mouse[0] > loc_exitBotton[0] and (loc_exitBotton[1]+loc_exitBotton[3]) > mouse[1] > loc_exitBotton[1] and click[0] == 1:
        pygame.quit()
        exit()

    if (loc_presetBotton[0]+loc_presetBotton[2]) > mouse[0] > loc_presetBotton[0] and (loc_presetBotton[1]+loc_presetBotton[3]) > mouse[1] > loc_presetBotton[1] and click[0] == 1:
        preset = preset + 1
        time.sleep(0.3)
        if preset == 4:
            preset = 1

    if (loc_pad1[0]+loc_pad1[2]) > mouse[0] > loc_pad1[0] and (loc_pad1[1]+loc_pad1[3]) > mouse[1] > loc_pad1[1] and click[0] == 1 and (pygame.mixer.Channel(1).get_busy() == False):
        hit_pad1 = 1

    if (loc_pad2[0]+loc_pad2[2]) > mouse[0] > loc_pad2[0] and (loc_pad2[1]+loc_pad2[3]) > mouse[1] > loc_pad2[1] and click[0] == 1 and (pygame.mixer.Channel(2).get_busy() == False):
        hit_pad2 = 1

    if (loc_pad3[0]+loc_pad3[2]) > mouse[0] > loc_pad3[0] and (loc_pad3[1]+loc_pad3[3]) > mouse[1] > loc_pad3[1] and click[0] == 1 and (pygame.mixer.Channel(3).get_busy() == False):
        hit_pad3 = 1

    if (loc_pad4[0]+loc_pad4[2]) > mouse[0] > loc_pad4[0] and (loc_pad4[1]+loc_pad4[3]) > mouse[1] > loc_pad4[1] and click[0] == 1 and (pygame.mixer.Channel(4).get_busy() == False):
        hit_pad4 = 1

    if (loc_pad5[0]+loc_pad5[2]) > mouse[0] > loc_pad5[0] and (loc_pad5[1]+loc_pad5[3]) > mouse[1] > loc_pad5[1] and click[0] == 1 and (pygame.mixer.Channel(5).get_busy() == False):
        hit_pad5 = 1

    if (loc_pad6[0]+loc_pad6[2]) > mouse[0] > loc_pad6[0] and (loc_pad6[1]+loc_pad6[3]) > mouse[1] > loc_pad6[1] and click[0] == 1 and (pygame.mixer.Channel(6).get_busy() == False):
        hit_pad6 = 1

    if (loc_pad7[0]+loc_pad7[2]) > mouse[0] > loc_pad7[0] and (loc_pad7[1]+loc_pad7[3]) > mouse[1] > loc_pad7[1] and click[0] == 1 and (pygame.mixer.Channel(7).get_busy() == False):
        hit_pad7 = 1

    if (loc_pad8[0]+loc_pad8[2]) > mouse[0] > loc_pad8[0] and (loc_pad8[1]+loc_pad8[3]) > mouse[1] > loc_pad8[1] and click[0] == 1 and (pygame.mixer.Channel(8).get_busy() == False):
        hit_pad8 = 1

    if (loc_pad9[0]+loc_pad9[2]) > mouse[0] > loc_pad9[0] and (loc_pad9[1]+loc_pad9[3]) > mouse[1] > loc_pad9[1] and click[0] == 1 and (pygame.mixer.Channel(9).get_busy() == False):
        hit_pad9 = 1

    if (loc_pad10[0]+loc_pad10[2]) > mouse[0] > loc_pad10[0] and (loc_pad10[1]+loc_pad10[3]) > mouse[1] > loc_pad10[1] and click[0] == 1 and (pygame.mixer.Channel(10).get_busy() == False):
        hit_pad10 = 1

    if (loc_pad11[0]+loc_pad11[2]) > mouse[0] > loc_pad11[0] and (loc_pad11[1]+loc_pad11[3]) > mouse[1] > loc_pad11[1] and click[0] == 1 and (pygame.mixer.Channel(11).get_busy() == False):
        hit_pad11 = 1

    if (loc_pad12[0]+loc_pad12[2]) > mouse[0] > loc_pad12[0] and (loc_pad12[1]+loc_pad12[3]) > mouse[1] > loc_pad12[1] and click[0] == 1 and (pygame.mixer.Channel(12).get_busy() == False):
        hit_pad12 = 1
    #通过鼠标左键点击或触控触发鼓垫



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and pygame.mixer.Channel(1).get_busy() == False:
                hit_pad1 = 1
            if event.key == pygame.K_t and pygame.mixer.Channel(2).get_busy() == False:
                hit_pad2 = 1
            if event.key == pygame.K_y and pygame.mixer.Channel(3).get_busy() == False:
                hit_pad3 = 1
            if event.key == pygame.K_u and pygame.mixer.Channel(4).get_busy() == False:
                hit_pad4 = 1
            if event.key == pygame.K_f and pygame.mixer.Channel(5).get_busy() == False:
                hit_pad5 = 1
            if event.key == pygame.K_g and pygame.mixer.Channel(6).get_busy() == False:
                hit_pad6 = 1
            if event.key == pygame.K_h and pygame.mixer.Channel(7).get_busy() == False:
                hit_pad7 = 1
            if event.key == pygame.K_j and pygame.mixer.Channel(8).get_busy() == False:
                hit_pad8 = 1
            if event.key == pygame.K_v and pygame.mixer.Channel(9).get_busy() == False:
                hit_pad9 = 1
            if event.key == pygame.K_b and pygame.mixer.Channel(10).get_busy() == False:
                hit_pad10 = 1
            if event.key == pygame.K_n and pygame.mixer.Channel(11).get_busy() == False:
                hit_pad11 = 1
            if event.key == pygame.K_m and pygame.mixer.Channel(12).get_busy() == False:
                hit_pad12 = 1
            #通过键盘触发鼓垫
            if event.key == pygame.K_BACKSPACE:
                pygame.quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                hit_pad1 = 0
            if event.key == pygame.K_t:
                hit_pad2 = 0
            if event.key == pygame.K_y:
                hit_pad3 = 0
            if event.key == pygame.K_u:
                hit_pad4 = 0
            if event.key == pygame.K_f:
                hit_pad5 = 0
            if event.key == pygame.K_g:
                hit_pad6 = 0
            if event.key == pygame.K_h:
                hit_pad7 = 0
            if event.key == pygame.K_j:
                hit_pad8 = 0
            if event.key == pygame.K_v:
                hit_pad9 = 0
            if event.key == pygame.K_b:
                hit_pad10 = 0
            if event.key == pygame.K_n:
                hit_pad11 = 0
            if event.key == pygame.K_m:
                hit_pad12 = 0

    if hit_pad1 == 1:
        hit_pad1=0
        pygame.mixer.Channel(1).play(sound1)
        pygame.draw.rect(mainScreen, afterHitColor,pad1)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad1)


    if hit_pad2 == 1:
        hit_pad2 = 0
        pygame.mixer.Channel(2).play(sound2)
        pygame.draw.rect(mainScreen, afterHitColor,pad2)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad2)

    if hit_pad3 == 1:
        hit_pad3 = 0
        pygame.mixer.Channel(3).play(sound3)
        pygame.draw.rect(mainScreen, afterHitColor,pad3)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad3)

    if hit_pad4 == 1:
        hit_pad4 = 0
        pygame.mixer.Channel(4).play(sound4)
        pygame.draw.rect(mainScreen, afterHitColor,pad4)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad4)

    if hit_pad5 == 1:
        hit_pad5 = 0
        pygame.mixer.Channel(5).play(sound5)
        pygame.draw.rect(mainScreen, afterHitColor,pad5)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad5)

    if hit_pad6 == 1:
        hit_pad6 = 0
        pygame.mixer.Channel(6).play(sound6)
        pygame.draw.rect(mainScreen, afterHitColor,pad6)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad6)

    if hit_pad7 == 1:
        hit_pad7 = 0
        pygame.mixer.Channel(7).play(sound7)
        pygame.draw.rect(mainScreen, afterHitColor,pad7)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad7)

    if hit_pad8 == 1:
        hit_pad8 = 0
        pygame.mixer.Channel(8).play(sound8)
        pygame.draw.rect(mainScreen, afterHitColor,pad8)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad8)

    if hit_pad9 == 1:
        hit_pad9 = 0
        pygame.mixer.Channel(9).play(sound9)
        pygame.draw.rect(mainScreen, afterHitColor,pad9)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad9)

    if hit_pad10 == 1:
        hit_pad10 = 0
        pygame.mixer.Channel(10).play(sound10)
        pygame.draw.rect(mainScreen, afterHitColor,pad10)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad10)

    if hit_pad11 == 1:
        hit_pad11 = 0
        pygame.mixer.Channel(11).play(sound11)
        pygame.draw.rect(mainScreen, afterHitColor,pad11)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad11)

    if hit_pad12 == 1:
        hit_pad12 = 0
        pygame.mixer.Channel(12).play(sound12)
        pygame.draw.rect(mainScreen, afterHitColor,pad12)
    else:
        pygame.draw.rect(mainScreen, beforeHitColor,pad12)

    pygame.display.update()