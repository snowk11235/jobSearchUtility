"""
Re-work of ksnowJobsProject.
This is a Python utility that pulls data from different job sites and conglomerates them.
------------------------------------------------------------------------------------------
Author:K.*
re-worked 12/21/20

NOTES:
> API DOCS:
    Glassdoor: https://www.glassdoor.com/developer/companiesApiActions.htm
    Indeed: https://opensource.indeedeng.io/api-documentation/docs/job-search/


"""
import database
import jobs


# build / populate databases
#

def main():

    github_url = "https://jobs.github.com/positions.json?"
    stackovfl_url = "https://stackoverflow.com/jobs/feed"
    indeed_url=""

    # List to hold incoming dictionaries
    alldata = []
    stackovfl_data = []
    github_data = []
    indeed_data = []

    # Open db and create tables
    conn, cursor = database.open_db("jobs_db.sqlite")
    database.create_all_jobs_table(cursor)
    database.create_github_table(cursor)
    database.create_indeed_table(cursor)
    database.create_stackovfl_table(cursor)

    # Get data from sites
    # GitHub
    alldata.extend(jobs.pull_github_data(github_url))
    github_data.extend(jobs.pull_github_data(github_url))
    # Stack overflow
    alldata.extend(jobs.pull_partial_stackoverflow_data(stackovfl_url))
    stackovfl_data.extend(jobs.pull_partial_stackoverflow_data(stackovfl_url))
    # Indeed
    #alldata.extend(jobs.pull_indeed_data(indeed_url))
    #github_data.extend(jobs.pull_indeed_data(indeed_url))


    # Insert to db
    database.insert_into_all_jobs_table(cursor, alldata)
    database.close_db(conn, cursor)





if __name__ == '__main__':
    main()