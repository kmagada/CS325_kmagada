import datapull
import embedding


def main():
    #pulls data with the API and saves to a JSON file
    datapull.main()

    #embeds the resume and job listings
    embedding.main()
    
# add Top N Selection here for top 10 jobs for the resume maybe use the OpenAI embedding to show recommendations

if __name__ == '__main__':
    main()