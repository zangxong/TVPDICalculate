#Author:Zhang Xing & Zhang Haoyan
#2023..04.17
#ANY problem@ zangxong@outlook.com
#Python v:3.9.16


import os 
import arcpy
from arcpy import env
from arcpy.sa import *


arcpy.CheckOutExtension('spatial')

evi = []
lst = []
pre = []


def tvpdi(pathin1,pathin2, pathin3, pathout):
    name = []
    evi_names = os.listdir(pathin1)
    lst_names = os.listdir(pathin2)
    pre_names = os.listdir(pathin3)
    for evi_name in evi_names:
        print ("VCI is: ", evi_name)
        if evi_name[-4:] == ".tif":
            evi_data = pathin1 + "/" + evi_name
            in_evi = arcpy.Raster(evi_data)
            evi_maximum = arcpy.GetRasterProperties_management(in_evi, 'MAXIMUM')
            evi_minimum = arcpy.GetRasterProperties_management(in_evi, 'MINIMUM')
            str_max = evi_maximum.getOutput(0)
            str_min = evi_minimum.getOutput(0)
            evi_max = float(str_max)
            evi_min = float(str_min)
            print (evi_maximum, type(evi_maximum), evi_minimum, type(evi_minimum))
            print (evi_max, evi_min , type(evi_max), type(evi_min))
            evi.append(in_evi)
            name.append(evi_name)
    for lst_name in lst_names:
        print ("LST is: ", lst_name)
        if lst_name[-4:] == ".tif":
            lst_data = pathin2 + "/" + lst_name
            in_lst = arcpy.Raster(lst_data)
            lst_maximum = arcpy.GetRasterProperties_management(in_evi, 'MAXIMUM')
            lst_minimum = arcpy.GetRasterProperties_management(in_evi, 'MINIMUM')
            str_max = lst_maximum.getOutput(0)
            str_min = lst_minimum.getOutput(0)
            lst_max = float(str_max)
            lst_min = float(str_min)
            print (lst_maximum, type(lst_maximum), lst_minimum, type(lst_minimum))
            print (lst_max, lst_min , type(lst_max), type(lst_min))
            lst.append(in_lst)
    for pre_name in pre_names:
        print ("pre is: ", pre_name)
        if pre_name[-4:] == ".tif":
            pre_data = pathin3 + "/" + pre_name
            in_pre = arcpy.Raster(pre_data)
            pre_maximum = arcpy.GetRasterProperties_management(in_evi, 'MAXIMUM')
            pre_minimum = arcpy.GetRasterProperties_management(in_evi, 'MINIMUM')
            pre_max = pre_maximum.getOutput(0)
            pre_min = pre_minimum.getOutput(0)
            pre_max = float(pre_max)
            pre_min = float(pre_min)
            print (pre_maximum, type(pre_maximum), pre_minimum, type(pre_minimum))
            print (pre_max, pre_min , type(pre_max), type(pre_min))
            pre.append(in_pre)
    for d1_evi, d2_lst, d3_pre, name in zip(evi, lst, pre, name):
        out_name = os.path.join(pathout, os.path.basename(name).split('_')[0] + '_TVPDI_CN.tif')
        print (out_name)
        result1 = (Square(lst_max - d2_lst) + Square(d1_evi - evi_min) + Square(d3_pre - pre_min))
        tvpdi = float(SquareRoot(3) / 3) * SquareRoot(result1)
        tvpdi.save(out_name)
        print (tvpdi, type(tvpdi))

if __name__ == "__main__":
    pathin1 = r""
    pathin2 = r""
    pathin3 = r""
    pathout = r""
    tvpdi(pathin1,pathin2, pathin3, pathout)


