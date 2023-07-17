#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

from model.native_model import Base
import datetime
from sqlalchemy.ext.declarative import declarative_base


# 单个对象方法1
def to_dict(p0):
    model_dict = dict(p0.__dict__)
    del model_dict['_sa_instance_state']
    return model_dict

# 单个对象方法2
def single_to_dict(p0):
    return {c.name: getattr(p0, c.name, None) for c in p0.__table__.columns}

# 多个对象
def dobule_to_dict(p0):
    result = {}
    for key in p0.__mapper__.c.keys():
        if getattr(p0, key) is not None:
            result[key] = str(getattr(p0, key))
        else:
            result[key] = getattr(p0, key)
    return result

# 配合多个对象使用的函数
def to_json(all_vendors):
    v = [dobule_to_dict(ven) for ven in all_vendors]
    return v

Base.to_dict = to_dict  # 如果使用的是flask-sqlalchemy，就使用对应的基类


class TypeCast:

    def to_dict(self):  # 方法一，该方法直接获取数据库原始数值,对于一些特殊字符如时间戳无法转换
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}  # 记得加None(网上一些教程没有加None是无法使用的)

    def to_dict(self):  # 方法二，该方法可以将获取结果进行定制，例如如下是将所有非空值输出成str类型
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    # def to_dict(self):  # 方法二定制，将时间戳值转为str类型，其他直接输出
    #     result = {}
    #     for key in self.__mapper__.c.keys():
    #         if type(getattr(self, key)) == datetime.datetime:
    #             result[key] = str(getattr(self, key))
    #         else:
    #             result[key] = getattr(self, key)
    #     return result

    # 配合to_dict一起使用
    def to_json(self, all_vendors):  # 多条结果时转为list(json)
        v = [ven.to_dict() for ven in all_vendors]
        return v


from datetime import datetime as cdatetime              #有时候会返回datatime类型
from datetime import date, time
# from flask_sqlalchemy import Model
from sqlalchemy.orm.query import Query
from sqlalchemy import DateTime, Numeric, Date, Time    #有时又是DateTime


def queryToList(models):
    if not models:
        return []
    if (isinstance(models, list)):
        lst = []
        for model in models:
            for mod in model:
                if (isinstance(mod, Base)):
                    gen = model_to_dict(mod)
                    dit = dict((g[0], g[1]) for g in gen).values()
                    lst.extend(list(dit))
                elif (isinstance(mod, dict)):
                    lst.extend(list(mod.values()))
                else:
                    lst.append(mod)
        return lst

def queryToLists(models):
    if not models:
        return []
    if (isinstance(models, list)):
        lst = []
        for model in models:
            tmp = []
            for mod in model:
                if (isinstance(mod, Base)):
                    gen = model_to_dict(mod)
                    dit = dict((g[0], g[1]) for g in gen).values()
                    tmp.extend(list(dit))
                elif (isinstance(mod, dict)):
                    tmp.extend(list(mod.values()))
                else:
                    tmp.append(mod)
            lst.append(tmp)
        return lst

def queryToDict(models):
    if not models:
        return []

    if (isinstance(models, list)):
            lst = []
            for model in models:
                tmp = {}
                for mod in model:
                    if (isinstance(mod, Base)):
                        gen = model_to_dict(mod)
                        dit = dict((g[0], g[1]) for g in gen)
                    else:
                        dit = result_to_dict(mod)
                    tmp.update(dit)
                lst.append(tmp)
            return lst

    else:
        if (isinstance(models[0], Base)):
            gen = model_to_dict(models)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


def queryToSYSDict(models):
    if not models:
        return []

    tmpDict = {}
    tmp = None
    if (isinstance(models, list)):
        KEYS = ["DICT_KEY", "KEY_", "LABEL", "SORT_", "INTRO", "REVISION"]
        for model in models:
            i = 0
            tmp2 = {}
            for mod in model:
                if (isinstance(mod, Base)):
                    gen = model_to_dict(mod)
                    dit = dict((g[0], g[1]) for g in gen)
                    if not tmpDict.get(dit["KEY_"]):
                        tmp = {}
                        tmpDict[dit["KEY_"]] = tmp
                        tmp["LABEL"] = dit["LABEL"]
                        tmp["INTRO"] = dit["INTRO"]
                        tmp["REVISION"] = dit["REVISION"]
                else:
                    if i == 0:
                        pass
                    elif i == 1:
                        tmp[mod] = tmp2
                    else:
                        tmp2[KEYS[i]] = mod
                    i += 1
        return tmpDict

    else:
        if (isinstance(models[0], Base)):
            gen = model_to_dict(models)
            print("gen", gen)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res

#当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    #这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res

#这段来自于参考资源
def model_to_dict(model):
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)


def find_datetime(value):
    for v in value:
        if (isinstance(value[v], cdatetime)):
            value[v] = convert_datetime(value[v])   #这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:
        if(isinstance(value, (cdatetime, DateTime))):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif(isinstance(value, (date, Date))):
            return value.strftime("%Y-%m-%d")
        elif(isinstance(value, (Time, time))):
            return value.strftime("%H:%M:%S")
    else:
        return ""
