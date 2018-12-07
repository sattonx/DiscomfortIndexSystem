#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import sys
import smbus2
class TH02:
    #定数宣言
    address = 0x40

    reg_conf = 0x03
    data_h = 0x01
    data_l = 0x02
    select_hum = 0x01
    select_temp = 0x11
    def __init__(self):
        self.channel = 1
        self.bus = smbus2.SMBus(self.channel)

    def readTemp(self):
        self.bus.write_i2c_block_data(self.address, self.reg_conf, [self.select_temp])
        self.bus.write_i2c_block_data(self.address, self.data_h, [])
        block1 = self.bus.read_i2c_block_data(self.address,0,3)

        data = (block1[1] << 8 | block1[2])
        data = data >> 2 
        data = (data/32.0) - 50.0
        return data

    def readHum(self): 
        self.bus.write_i2c_block_data(self.address, self.reg_conf, [self.select_hum])
        self.bus.write_i2c_block_data(self.address, self.data_h, [])
        block2 = self.bus.read_i2c_block_data(self.address,0,3)
       
        data = (block2[1] << 8 | block2[2])
        data = data >> 4 
        data = data / 16.0 - 24.0
        return data

    def outputDI(self, temp, hum):
        di = 0.81 * temp + 0.01 * hum * (0.99 * temp - 14.3) + 46.3
        return di
