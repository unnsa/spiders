#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: albert
:date: 03/07/2019
"""

from dbutils.pooled_db import PooledDB
from config import MysqlEnviron
import logging as log
import pymysql

# connection_pool = PooledDB(creator=pymysql,
#                            maxconnections=20,
#                            host=MysqlEnviron.CONFIG.host,
#                            port=MysqlEnviron.port,
#                            db=MysqlEnviron.database,
#                            user=MysqlEnviron.username,
#                            passwd=MysqlEnviron.password)

connection_pool = PooledDB(creator=pymysql,
                           maxconnections=20,
                           host='10.143.133.42',
                           port=3306,
                           db='spider_qichacha',
                           user='bigdata',
                           passwd='zcbigdata')


def save_company_summary(data: dict):
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'insert ignore into company_summary(`pid`,`ent_name`,`ent_type`,`domicile`) ' \
          'values(%(pid)s,%(ent_name)s,%(ent_type)s,%(domicile)s)'
    return write(sql, data)


def getCompanyInfo():
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'SELECT pid FROM company_summary'
    return query(sql, {})


def save_company_Detail(data: dict):
    """
    插入操作
    :param data:
    :return:
    """
    sql = 'INSERT ignore INTO company_detail(`pid`, `basic_data`, `directors_data`, `branchs_data`, `shareholders_data`, `annual_report_data`, `license`, `abnormal`, `change_record_data`, `chattelmortgage`, `penalties`, `illegal`, `equitypledge`, `clearaccount`) ' \
          'VALUES (%(pid)s, %(basic_data)s, %(directors_data)s, %(branchs_data)s, %(shareholders_data)s, %(annual_report_data)s, %(license)s, %(abnormal)s, %(change_record_data)s, %(chattelmortgage)s, %(penalties)s, %(illegal)s, %(equitypledge)s, %(clearaccount)s)'
    return write(sql, data)


def write(sql: str, data: any):
    connection = connection_pool.connection()
    cursor = connection.cursor()
    result = cursor.execute(sql, data)

    try:
        connection.commit()
    except RuntimeError as error:
        connection.rollback()
        log.error('Insert Error!')
        raise error

    return result


def query(sql: str, data: any):
    connection = connection_pool.connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    results = cursor.fetchall()
    try:
        connection.commit()
    except RuntimeError as error:
        connection.rollback()
        log.error('Insert Error!')
        raise error
    return results
