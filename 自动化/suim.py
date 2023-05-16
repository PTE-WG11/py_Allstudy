# -*- coding:utf-8 -*-
import urllib.parse

from selenium import webdriver


def url_NO(place):
    html = 'https://www.youbianku.com/SearchResults?address=%s' % urllib.parse.quote(place)  # 邮编查询
    return html


def auto_NO(placeName):
    """
    本函数实现了浏览器自动搜索地名的邮编

    :param placeName:

    :return:成功 NO,address，0失败
    """
    # 存入数据库是存库的最后一步，其他参数通过形参（文件读取函数）传入

    driver = webdriver.Edge()
    driver.implicitly_wait(10)  # 设置超时时间
    driver.maximize_window()  # 窗口最大化显示

    #  navigate to the application home page
    # placeName = '英雄山'

    url = url_NO(place=placeName)
    driver.get(url)

    # search_field = driver.find_element_by_id("kw")  # 找到输入框
    NO_xpath = '//*[@id="mw-content-text"]/div[2]/div/ul/div/table/tbody/tr[3]/td/a'
    address_xpath = '//*[@id="mw-content-text"]/div[2]/div/ul/div/table/tbody/tr[2]/td'
    try:
        NO_list = driver.find_elements_by_xpath(NO_xpath)
        address_list = driver.find_elements_by_xpath(address_xpath)
    # print(products.get_attribute("innerHTML"))
    except:
        driver.quit()
        return '000000', ''
    if len(NO_list) != 0 and len(address_list) != 0:
        NO = NO_list[0].get_attribute('innerHTML')
        # print(NO)
        address = address_list[0].get_attribute('innerHTML')
        # print(address)
        # 入库---修改后入库独立出来
        driver.quit()
        return NO, address
