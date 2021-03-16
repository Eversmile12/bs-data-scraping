from beautiful import createSoup
import requests
import re
from db import addJobs

def createUrl(page):    
    job_site = 'https://www.totaljobs.com/jobs/developer-internship?page='
    job_site_first_page = "{entry}{end_url}".format(entry = job_site, end_url = page)
    return job_site_first_page


def totalJobs():
    print("################## Starting Totaljobs.com ##################")
    page_number = 1
    soup = createSoup(createUrl(page_number))

    parent_div = soup.find('div', class_="job-results")
    pagination = parent_div.find('ul', class_="pagination")
    pagination_items = pagination.findAll('li')
    last_pagination_item = pagination_items[len(pagination_items)-2].text.strip()
    last_page = int(last_pagination_item)
    job_list = []
    while page_number <= last_page:
            try:    
                parent_div = soup.find('div', class_="job-results")
                print("############## Scraping page " + str(page_number) + " of " + str(last_page) + " ##############")    
                
                new_job_div = parent_div.findAll('div', class_="job new")

                for job in new_job_div:
                    job_title_parent = job.find('div', class_="job-title")

                    job_application_link = job_title_parent.a["href"]
                    job_id = job_application_link.split("-")
                    job_id = job_id[-1]

                    job_title = job_title_parent.h2.text

                    job_detail_parent = job.find('div', class_="detail-body")

                    job_location_parent = job_detail_parent.find('li', class_="location")

                    job_location = job_location_parent.span.text
                    job_location_sanitized = re.findall("\\b[a-zA-Z]*\s?[a-zA-Z]+\s?[a-zA-Z]*\\b", job_location)[0]
                    # \b[a-zA-Z]+\s?[a-zA-Z]*?\b
                    if not job_location_sanitized:
                        job_location_sanitized = None
                    job_salary = job_detail_parent.find('li', class_="salary").text
                    
                    job_salary_sanitized = re.findall("\d+.?\d+", job_salary)
                    if not job_salary_sanitized:
                        job_salary_sanitized = None
                    else:
                        job_salary_sanitized = job_salary_sanitized[0]
                        job_salary_sanitized.replace(".","")
                        job_salary_sanitized.replace(",","")


                    job_type = job_detail_parent.find('li', class_="job-type").span.text
                    job_company = job_detail_parent.find('li', class_="company").h3.a.text

                    job_description = job_detail_parent.find('p', class_="job-intro").text
                    
                    job = {}
                    job["job_id"] = job_id
                    job["job_company_name"] = job_company
                    job["job_type"] = job_type
                    job["job_salary"] = job_salary_sanitized
                    job["job_location"] = job_location_sanitized
                    job["job_title"] = job_title
                    job["job_description"] = job_description
                    job["job_application_link"] = job_application_link
                    print("[New job found.]")
                    job_list.append(job)
            except:
                print("################## WARNING: Something was missing Totaljobs.com ##################")
                pass

            page_number += 1
            if page_number > last_page:
                break
            soup = createSoup(createUrl(page_number))
    print("################## Finalizing Totaljobs.com ##################")
    addJobs(job_list)

if __name__ == "__main__":
    totalJobs()

#{ div job-results{
#   div job new{
#       div job-title{
#           div job-title.a[href]
#           div job-title.h2
#       }
#       div detail-body {
#           li location.span.text
#           li salary.text
#           li company.h3.a.text
#           p job-intro.text
#           
#       }
#       
#   }
# }
# 
# 
# 
# 
# 
# 
# 
# }




# file = open("output.html", "w", encoding='utf-8')
# file.write(source)
# file.close()

# DATA:
# job application link
# job title
# job location
# job-type
# job salary ++++++++
# job time stamp -------
# job company name
# job description

# soup.findAll(True, {'class':['class1', 'class2']})
# class_='action-link showPhonesLink'

