import pandas as pd

def preproc_cohort(cohort_output:str, group_ethnicity):

    print("[CLEANING COHORT DATA]")
    cohort = pd.read_csv(f'./data/cohort/{cohort_output}.csv.gz', compression='gzip', parse_dates = ['intime', 'outtime'])
    
    def group_ethnicity_func(data):
        col_name = 'race' if 'race' in data.columns else 'ethnicity'
        return data.replace(to_replace={
            col_name:[r'^BLACK.*$', 
                      r'^WHITE.*$',
                      r'^ASIAN.*$', 
                      r'^HISPANIC.*$|SOUTH AMERICAN', 
                      r'^MULTIPLE.*', 
                      r'^OTHER$|.*NATIVE.*', 
                      r'UNKNOWN|DECLINED|^UNABLE.*|PORTUGUESE']}, 
            value={col_name:['Black', 'White', 'Asian','Hispanic', 'Mixed', 'Other', None]}, 
            regex=True)


    if(group_ethnicity=='Yes, group ethnicities'):
        cohort = group_ethnicity_func(cohort)

        print("Total number of ethnic groups:",len(cohort.ethnicity.unique()))
        cohort.to_csv(f'./data/cohort/{cohort_output}.csv.gz', compression='gzip', index=False)
        print("[SUCCESSFULLY UPDATED COHORT TABLE]")
        