# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 beezz <beezz@T500>

import os
import pytest
import confiskus

import ConfigParser


def test_simple_inh():
    par = []
    res = [
        os.path.abspath('test_files/deeper/parent4.ini'),
    ]
    fn = 'test_files/parent3.ini'
    cf = confiskus.Confiskus()
    cf.build_parents(fn, par)
    assert par == res


def test_all_inh():
    par = []
    res = [
        os.path.abspath('test_files/deeper/parent4.ini'),
        os.path.abspath('test_files/parent3.ini'),
        os.path.abspath('test_files/parent2.ini'),
        os.path.abspath('test_files/parent.ini'),
    ]
    fn = 'test_files/conf.ini'
    cf = confiskus.Confiskus()
    cf.build_parents(fn, par)
    assert par == res


def test_supply_par():
    config = confiskus.Confiskus(
        parents=['test_files/alone.ini', ],
    ).read('test_files/conf.ini')
    assert config.get('alone', 'name', 'value')


def test_supply_default():
    config = confiskus.Confiskus(
        defaults={'def_name': 'value'},
        parents=['test_files/no_defs.ini', ],
    ).read('test_files/conf.ini')
    assert config.get('defs', 'def_name', 'value')


def test_no_env():
    with pytest.raises(ConfigParser.InterpolationError):
        confiskus.Confiskus(
            use_env=False
        ).read('test_files/conf.ini')


def test_values():
    config = confiskus.Confiskus().read('test_files/conf.ini')
    assert config.get('db', 'url', 'parent_user4/localhost')
