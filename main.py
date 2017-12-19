import time
from selenium import webdriver

browser = webdriver.Chrome(chrome_driver_path)
browser.get('https://upload.taobao.com/auction/sell.jhtml?spm=a313o.201708ban.category.d48.217216dbkKIwq0&mytmenu=wym')
test = []


def put_all_props():
    trs = browser.find_elements_by_xpath('//*[@id="saleProps"]/table/tbody/tr/td')
    tds = [td.text for td in trs]
    return tds


def cate_name():
    text = browser.find_element_by_xpath('//*[@id="catPath"]')
    name = text.text
    name = name.replace('切换类目', '')
    name = name.replace('类目：', '')
    return name.split('>>')


def put_all_values():
    attr_values = {}
    # blank_space = browser.find_element_by_xpath('//*[@id="itemBasic"]')
    # space = browser.find_element_by_xpath('//*[@id="props"]')
    trs = browser.find_elements_by_xpath('//*[@id="props"]/table/tbody/tr')
    for tr in trs:
        td = tr.find_element_by_xpath('td[1]/label')
        attr_values[td.text] = ''
        try:
            input_ = tr.find_element_by_xpath('td[2]/div/div[1]/div/div/div/div[1]/input')
            input_.click()
            time.sleep(0.5)
            values = tr.find_element_by_xpath('td[2]/div/div[1]/div/div/div/div[2]/ul').text
            # print(values)
            # print(values.split('\n'))
            attr_values[td.text] = values.split('\n')
            td.click()
            # space.click()
        except Exception as _:
            try:
                labels = tr.find_elements_by_xpath('td[2]/div/label')
                attr_values[td.text] = [label.text for label in labels]
            except Exception as _:
                pass
    return attr_values


def put_all():
    browser.implicitly_wait(2)
    cate_name_tuple = cate_name()
    all_values = put_all_values()
    all_props = put_all_props()
    print('Cate %s Have %d values' % (cate_name_tuple, len(all_values)))
    test.append({
        'text': cate_name_tuple,
        'attr': all_values,
        'prors': all_props
    })


def pr():
    ttt = set()
    for t in test:
        ttt.add(t['text'][0])
    for t in ttt:
        print(t)


def run1():
    publish_btn = browser.find_element_by_xpath('//*[@id="J_CatePubBtn"]')
    publish_btn.click()
    browser.implicitly_wait(3)
    put_all()
    browser.get(
        'https://upload.taobao.com/auction/sell.jhtml?spm=a313o.201708ban.category.d48.217216dbkKIwq0&mytmenu=wym')
    browser.implicitly_wait(3)


def run2():
    publish_btn = browser.find_element_by_xpath('//*[@id="J_CatePubBtn"]')
    publish_btn.click()
    browser.implicitly_wait(3)
    put_all()
    browser.find_element_by_xpath('//*[@id="catPath"]/span').click()
    browser.implicitly_wait(3)


def run3():

    run2()

    ccs, l_cc, l_lis = None, None, None
    flag_current_done = True

    def read_cate():
        nonlocal ccs, l_cc, l_lis
        # 被选中的全部分类
        ccs = browser.find_elements_by_class_name('cc-selected')
        # 最后一个被选中的分类
        l_cc = ccs[-1]
        # 最后一个被选中的分类的列表
        l_lis = l_cc.find_element_by_xpath('../../..').find_elements_by_xpath('li/ul/li')

    while True:

        read_cate()

        # 判断按钮是否可以点击
        publish_btn = browser.find_element_by_xpath('//*[@id="J_CatePubBtn"]')

        # 当前列完成, 回溯上一列
        if l_lis.index(l_cc) == len(l_lis) - 1:
            if flag_current_done:
                f_cc = ccs[-2]
                if ccs.index(f_cc) == 0:
                    break
                f_cc.click()
                browser.implicitly_wait(3)
                continue
        else:
            # 当前遍历
            if flag_current_done:
                l_lis[l_lis.index(l_cc) + 1].click()
                browser.implicitly_wait(3)
                flag_current_done = False
                continue

        # 可以
        if publish_btn.is_enabled():
            publish_btn.click()
            browser.implicitly_wait(3)
            put_all()
            browser.find_element_by_xpath('//*[@id="catPath"]/span').click()
            browser.implicitly_wait(3)
            flag_current_done = True
        # 不行
        else:
            if flag_current_done is False:
                next_l = l_cc.find_element_by_xpath('../../../../..').find_element_by_xpath(
                    'following-sibling::*[1]/div[2]/ul')
                next_l.find_elements_by_xpath('li/ul/li')[0].click()
                browser.implicitly_wait(3)
