#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CompanySummary(object):
    def __init__(self):
        self.pid = None
        self.ent_name = None
        self.ent_type = None
        self.domicile = None

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())


class CompanyDetail(object):
    def __init__(self):
        self.pid = None
        self.basic_data = None  # '基本信息',
        self.directors_data = None  # '主要人员信息',
        self.branchs_data = None  # '分支机构信息',
        self.shareholders_data = None  # '股东信息',
        self.annual_report_data = None  # '企业年报信息',
        self.license = None  # '行政许可',
        self.abnormal = None  # '经营异常名录',
        self.change_record_data = None  # '变更信息',
        self.clearaccount = None  # 清算信息
        self.chattelmortgage = None  # '动产抵押信息',
        self.penalties = None  # '行政处罚信息',
        self.illegal = None  # '列入严重违法名录信息',
        self.equitypledge = None  # '股权质押信息',

    def __str__(self) -> str:
        return ', '.join('%s: %s' % elem for elem in self.__dict__.items())
