from beautiful import createSoup
import time
from db import addJobs
entry = "https://www.simplyhired.co.uk"
url = "/search?q=developer+internship&pn="




def scrapeApplicationPage(application_page):
    try:            
        application_url = "{entry}{application_url}".format(entry = entry, application_url = application_page)
        soup = createSoup(application_url)
        button_link = soup.find("div", class_="apply").a["href"]
        job_type = soup.findAll("span", class_="info-unit")
        if len(job_type) == 2:
            job_type = job_type[1].span.text
        else:
            job_type = job_type[0].span.text
        job_details = {
            "application_link": button_link,
            "job_type": job_type
        }
        return job_details
    except:
        return {"application_link": button_link, "job_type":""}


def simplyHired():
    print("################## Starting Simplyhired.com ##################")
    job_list = [] 
    page_number = 1
    for i in range(4):
        print("Page {page} of 4 ###########################".format(page=page_number))
        url_first_page = "{url_start}{url_end}{page}".format(url_start = entry, url_end = url, page = page_number)
        soup = createSoup(url_first_page)
        if soup != None:
            print("SUCCEEDED: Page to scrape FOUND")
            wrap = soup.find('div', class_='wrap')
            for jobCard in wrap.findAll('div', class_='SerpJob-jobCard'):
                print("New job found. Now saving.")
                try:            
                    job_posting_header = jobCard.find('div', class_="jobposting-title")
                    job_posting_title = job_posting_header.a.text
                    meta_container = jobCard.find('div', class_="jobposting-subtitle")

                    job_company = meta_container.find('span', class_="jobposting-company").text
                    job_location = meta_container.find('span', class_="jobposting-location").text

                    snippet_container = jobCard.find('div', class_="SerpJob-snippetContainer")
                    job_description = snippet_container.p.text

                    meta_info = jobCard.find('div', class_="SerpJob-metaInfoRight")
                    job_upload_date = meta_info.span.time["datetime"]

                    application_page = job_posting_header.a['href']
                    job_details = scrapeApplicationPage(application_page)
                    application_link = job_details["application_link"]
                    job_id = application_link.split("=")
                    job_id = job_id[1]
                    job_type = job_details["job_type"]
                        
                    job = {}
                    job["job_id"] = job_id
                    job["job_company_name"] = job_company
                    job["job_type"] = job_type
                    job["job_salary"] = None
                    job["job_location"] = job_location
                    job["job_title"] = job_posting_title
                    job["job_description"] = job_description
                    job["job_application_link"] = entry+application_link
                    job_list.append(job)
                    # print(application_link)
                    # print("#####################################################")
                except:
                    print("################## WARNING: Something was missing Simplyhired.com ##################")
                    pass
            page_number += 1
        else:
            print("################## Error: Page not found Simplyhired.com ##################")
    print("################## Finalizing Simplyhired.com ##################")
    addJobs(job_list)

if __name__ == "__main__":
    simplyHired()


# DATA:
# job application link
# job title
# job location
# job salary ----------
# job time stamp +++++++
# job company name
# job description

# div  wrapper{
#   div SerpJob-jobCard{
#       div jobposting-title.a.text,
#          LINK jobpost-title.a['href'] <---- brings us to the internship page on simplyhired
#       div jobposting-subtitle{
#           span jobposting-company.text
#           span jobposting-location.text
#    }
#    SerpJob-snippetContainer.p.text   
#  }
#   div SerpJob-metaInfoRight
#       span SerpJob-timestamp
#       time [datetime]
# }

# LINK -> {
#   div apply.a[href]
# 
# }