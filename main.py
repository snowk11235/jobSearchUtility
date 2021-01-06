"""
Re-work of ksnowJobsProject.
This is a Python utility that pulls data from different job sites and conglomerates them.
------------------------------------------------------------------------------------------
Author:K.*

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
    #database.create_indeed_table(cursor)
    database.create_stackovfl_table(cursor)

    # Get data from sites
    # GitHub
    github_data.extend(jobs.pull_github_data(github_url))
    alldata.extend(github_data)
    # Stack overflow
    stackovfl_data.extend(jobs.pull_partial_stackoverflow_data(stackovfl_url))
    alldata.extend(stackovfl_data)
    # Indeed
    # indeed_data.extend(jobs.pull_indeed_data(indeed_url))
    #alldata.extend(indeed_data)


    # Insert to db
    database.insert_into_github_table(cursor, github_data)
    database.insert_into_stackovfl_table(cursor, stackovfl_data)
    #database.insert_into_all_jobs_table(cursor, alldata)
    database.close_db(conn, cursor)





if __name__ == '__main__':
    main()