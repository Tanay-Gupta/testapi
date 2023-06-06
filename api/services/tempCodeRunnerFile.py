
        #1.get the html
        response=AtCoderService().make_request(CONTESTS_URL)

        htmlContent=response.content
        #html has been parse
        soup=BeautifulSoup(htmlContent,'html.parser')
        tables = soup.findAll(".table-default")

        print(tables)
        #data = AtCoderService().create_data_objec