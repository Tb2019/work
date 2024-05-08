import re
from crawler import ReCrawler
from lxml import etree
from urllib import parse
# import os
#
# school_name = None
# college_name = None
#
# os.path.exists(f'./Results/{school_name}/{college_name}') or os.makedirs(f'./Results/{school_name}/{college_name}')

school_name = '青海大学'
college_name = '机械工程学院'
school_id = 3
college_id = 10
start_urls = ['https://jxxy.qhu.edu.cn/szgk/jxsjzzjqzdhjys/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/jxsjzzjqzdhjys/index1.htm',
              'https://jxxy.qhu.edu.cn/szgk/jxdzgcjys/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/clcxjys/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/clgcjys/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/yjgcjys/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/gctxjxzx/index.htm',
              'https://jxxy.qhu.edu.cn/szgk/jcgyxlzx/index.htm']

a_s_xpath_str = '//div[@class="pageList"]//ul/li/a'
target_div_xpath_str = '//div[@class="pageArticle"]'
# # 研究方向
# directions_pattern_list = [
#                             re.compile(r'', re.S),
#                             re.compile(r'', re.S)
#                           ]
# # 简介
# abstracts_pattern_list = [
#                             re.compile(r'', re.S),
#                             re.compile(r'', re.S)
#                           ]
# # 办公地点
# office_address_pattern_list = [
#                                 re.compile(r'', re.S)
#                               ]
# # 在职信息
# job_information_pattern_list = [
#                                 re.compile(r'', re.S)
#                               ]
# # 主要任职
# responsibilities_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
# # 教育经历
# education_experience_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
#
# # 工作经历
# work_experience_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
# # 专利
# patent_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
# # 科研项目
# project_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
# # 奖励/荣誉
# award_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]
# # 社会兼职
# social_job_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]


class Special_ReCrawler(ReCrawler):
    def parse_index(self, index_page, url):
        page = etree.HTML(index_page)
        a_s = page.xpath(self.a_s_xpath_str)
        for a in a_s:
            name = a.xpath('.//text()')
            if name:
                name = name[0]
                name = re.sub(r'(.*)\s+.*', r'\1', name)
                name = re.sub(self.name_filter_re, '', name)
                link = a.xpath('./@href')[0]
                link = parse.urljoin(url, link)
            else:
                continue
            yield name, link


spider = Special_ReCrawler(
                   school_name=school_name,
                   college_name=college_name,
                   school_id=school_id,
                   college_id=college_id,
                   # name_filter_re=,
                   start_urls=start_urls,
                   a_s_xpath_str=a_s_xpath_str,
                   target_div_xpath_str=target_div_xpath_str,
                   # directions_pattern_list=directions_pattern_list,
                   # abstracts_pattern_list=abstracts_pattern_list,
                   # office_address_pattern_list=office_address_pattern_list,
                   # job_information_pattern_list=job_information_pattern_list,
                   # responsibilities_pattern_list=responsibilities_pattern_list,
                   # education_experience_pattern_list=education_experience_pattern_list,
                   # work_experience_pattern_list=work_experience_pattern_list,
                   # patent_pattern_list=patent_pattern_list,
                   # project_pattern_list=project_pattern_list,
                   # award_pattern_list=award_pattern_list,
                   # social_job_pattern_list=social_job_pattern_list,
                   save2target='simple'
                   )

spider.run()


