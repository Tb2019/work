import re
from crawler import ReCrawler

school_name = '石河子大学'
college_name = '食品学院'
school_id = 2
college_id = 3
start_urls = ['https://spxy.shzu.edu.cn/zjrc/list.htm',
              'https://spxy.shzu.edu.cn/2935/list.htm',
              'https://spxy.shzu.edu.cn/2936/list.htm',
              'https://spxy.shzu.edu.cn/js/list.htm'
              ]

a_s_xpath_str = '//div[@id="wp_content_w6_0"]//a'
target_div_xpath_str = '//div[@class="infobox"]'
# 研究方向
directions_pattern_list = [
                            re.compile(r'教育背景.*?研究方向(?::|：)?(.*?)(?:科研项目|学术论文|承担教学)', re.S),
                            # re.compile(r'', re.S)
                          ]
# 简介
abstracts_pattern_list = [
                            re.compile(r'个人简介(?::|：)?(.*?)社会兼职', re.S),
                            # re.compile(r'', re.S)
                          ]
# 办公地点
office_address_pattern_list = [
                                re.compile(r'通讯地址(?::|：)?(.*?)(?:职位|个人简介)', re.S)
                              ]
# 在职信息
# job_information_pattern_list = [
#                                 re.compile(r'', re.S)
#                               ]
# 主要任职
responsibilities_pattern_list = [
                                    re.compile(r'职位(?::|：)?(.*?)个人简介', re.S),
                                    # re.compile(r'', re.S)
                                ]
# # 教育经历
# education_experience_pattern_list = [
#                                     re.compile(r'', re.S),
#                                     re.compile(r'', re.S)
#                                 ]

# 工作经历
work_experience_pattern_list = [
                                    re.compile(r'科研学术工作经历与教育背景(?::|：)?(.*?)研究方向(?::|：)?', re.S),
                                    # re.compile(r'', re.S)
                                ]
# 专利
patent_pattern_list = [
                                    re.compile(r'专利(?!.*?(?:社会兼职|科研项目).*?)(?::|：)?(.*?)承担教学', re.S),
                                    # re.compile(r'', re.S)
                                ]
# 科研项目
project_pattern_list = [
                                    re.compile(r'科研项目(?::|：)?(.*?)学术论文', re.S),
                                    # re.compile(r'', re.S)
                                ]
# 奖励/荣誉
award_pattern_list = [
                                    re.compile(r'获奖(?::|：)?(.*?)专利', re.S),
                                    # re.compile(r'', re.S)
                                ]
# 社会兼职
social_job_pattern_list = [
                                    re.compile(r'社会兼职(?::|：)?(.*?)科研学术工作经历与教育背景', re.S),
                                    # re.compile(r'', re.S)
                                ]

spider = ReCrawler(
                   school_name='02石河子大学',
                   college_name='食品学院',
                   school_id=school_id,
                   college_id=college_id,
                   name_filter_re=r'\s*',
                   start_urls=start_urls,
                   a_s_xpath_str=a_s_xpath_str,
                   target_div_xpath_str=target_div_xpath_str,
                   directions_pattern_list=directions_pattern_list,
                   abstracts_pattern_list=abstracts_pattern_list,
                   office_address_pattern_list=office_address_pattern_list,
                   # job_information_pattern_list=job_information_pattern_list,
                   responsibilities_pattern_list=responsibilities_pattern_list,
                   # education_experience_pattern_list=education_experience_pattern_list,
                   work_experience_pattern_list=work_experience_pattern_list,
                   patent_pattern_list=patent_pattern_list,
                   project_pattern_list=project_pattern_list,
                   award_pattern_list=award_pattern_list,
                   social_job_pattern_list=social_job_pattern_list,
                   save2target='simple'
                   )

spider.run()


