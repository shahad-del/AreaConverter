class ConvertHelpers:
    def ConvertFromRopaniSystem(self, ropani, aana, paisa, daam):
        ropaniToDaam = ropani * 256
        aanaToDaam = aana * 16
        paisaToDaam = paisa * 4
        totalDaam = ropaniToDaam + aanaToDaam + paisaToDaam + daam
        totalDhur = totalDaam * 0.1174
        bigha = 0
        kattha = 0
        if totalDhur > 400:
            bigha += totalDhur // 400
            totalDhur = totalDhur % 400
        elif totalDhur > 20:
                kattha += totalDhur // 20
                totalDhur = totalDhur % 20
        squareFeet = totalDaam * 21.39 
        squareMeter = totalDaam * 1.987179487179487

        print(f"{ropani}Ropani {aana}Aana {paisa}paisa {daam}daam")
        print(f"{bigha}bigha {kattha}kattha {totalDhur:.2f}dhur")
        print(f"{squareFeet:2f} square feet")
        print(f"{squareMeter:2f} squareMeter")

    def ConvertFromBighaSystem(self,bigha, katha, dhur):
            bighaToDhur = bigha * 400
            kathaToDhur = katha * 20
            totalDhur = bighaToDhur + kathaToDhur + dhur
            totalDaam = totalDhur *  8.520
            ropani = 0
            aana = 0
            paisa = 0
            if totalDaam >= 256:
                ropani = totalDaam//256
                totalDaam = totalDaam % 256
            if totalDaam > 16:
                aana = totalDaam//16
                totalDaam = totalDaam % 16
            if totalDaam > 4:
                paisa = totalDaam//4
                totalDaam = totalDaam % 4
            squareMeter = totalDhur * 182.25
            squareFeet = totalDhur *  16.931438127090303


            print(f"{bigha}bigha {katha}kattha {dhur}dhur")
            print(f"{ropani}ropani {aana}aana {paisa}paisa {totalDaam:2f}daam")
            print(f"{squareFeet:2f} square feet")
            print(f"{squareMeter:2f} squareMeter")
    def converFromsquareFeet(self,sqFt):
        sqFtToDaam = sqFt * 0.047
        sqFtToDhur = sqFt * 0.005
        sqFtToSqmtr = sqFt * 0.0929022668153103
        ropani = 0
        aana = 0
        paisa = 0
        if sqFtToDaam >= 256:
            ropani = sqFtToDaam//256
            sqFtToDaam = sqFtToDaam % 256
        if sqFtToDaam > 16:
            aana = sqFtToDaam//16
            sqFtToDaam = sqFtToDaam % 16
        if sqFtToDaam > 4:
            paisa = sqFtToDaam//4
            sqFtToDaam = sqFtToDaam % 4
        bigha = 0
        kattha = 0
        if sqFtToDhur > 400:
            bigha = sqFtToDhur // 400
            sqFtToDhur = sqFtToDhur % 400
        elif sqFtToDhur > 20:
                kattha = sqFtToDhur // 20
                sqFtToDhur = sqFtToDhur % 20
        print(f"{sqFt} sqFt")
        print(f"{ropani:2f}ropani {aana:2f}aana {paisa:2f}paisa {sqFtToDaam:2f}daam")
        print(f"{bigha:2f}bigha {kattha:2f}kattha {sqFtToDhur:.2f}dhur")
        print(f"{sqFtToSqmtr:2f} sqmtr")
    def converFromsquareMeter(self,sqMtr):
        sqMtrToSqFt = sqMtr * 10.764
        sqFtToDaam = sqMtrToSqFt * 0.047
        sqFtToDhur = sqMtrToSqFt * 0.005
        ropani = 0
        aana = 0
        paisa = 0
        if sqFtToDaam >= 256:
            ropani = sqFtToDaam//256
            sqFtToDaam = sqFtToDaam % 256
        if sqFtToDaam > 16:
            aana = sqFtToDaam//16
            sqFtToDaam = sqFtToDaam % 16
        if sqFtToDaam > 4:
            paisa = sqFtToDaam//4
            sqFtToDaam = sqFtToDaam % 4
        bigha = 0
        kattha = 0
        if sqFtToDhur > 400:
            bigha = sqFtToDhur // 400
            sqFtToDhur = sqFtToDhur % 400
        elif sqFtToDhur > 20:
                kattha = sqFtToDhur // 20
                sqFtToDhur = sqFtToDhur % 20
        print(f"{sqMtr} sqMtr")
        print(f"{ropani}ropani {aana}aana {paisa}paisa {sqFtToDaam:2f}daam")
        print(f"{bigha}bigha {kattha}kattha {sqFtToDhur:.2f}dhur")
        print(f"{sqMtrToSqFt:2f} sqft")
