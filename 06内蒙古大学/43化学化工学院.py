#todo:刘粉荣/王文波/刘鹰
import re

from crawler import ReCrawler

school_name = '内蒙古大学'
college_name = '化学化工学院'
school_id = 6
college_id = 43
start_urls = ['https://chem.imu.edu.cn/szdw1/wjhx.htm',
              'https://chem.imu.edu.cn/szdw1/yjhx.htm',
              'https://chem.imu.edu.cn/szdw1/fxhx.htm',
              'https://chem.imu.edu.cn/szdw1/wlhx.htm',
              'https://chem.imu.edu.cn/szdw1/clkxygc.htm',
              'https://chem.imu.edu.cn/szdw1/hxgcygy.htm',
              'https://chem.imu.edu.cn/szdw1/myhxyjs.htm',
              'https://chem.imu.edu.cn/szdw1/rzpgcyjzx.htm',
              'https://chem.imu.edu.cn/szdw1/dxyqfxcszx.htm',
              'https://chem.imu.edu.cn/szdw1/syjxglzx.htm']

a_s_xpath_str = '//div[@class="xwlistnew"]/ul/li/div[@class="tea-content"]/a'
target_div_xpath_str = '//div[@id="vsb_content"]'
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

spider = ReCrawler(
                   school_name=school_name,
                   college_name=college_name,
                   school_id=school_id,
                   college_id=college_id,
                   # name_filter_re=r'导师简介',
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
                   email_pattern=re.compile(r'[a-zA-Z0-9._-]+(?:@|\(at\)|\(AT\)|\[at]|\[AT])(?=.{1,20}(?:\.com|\.cn|\.fr))[a-zA-Z0-9_-]+\.[a-zA-Z._-]+', re.S),
                   save2target='simple'
                   )

spider.run()


