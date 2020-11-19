import numpy as np

#The import list should include two companies with correspond information required below.

#To compare, matrix operations like, summation and normalization should be wote first.
class MatrixOperation():
    def normalization(self,array1):
        self.array1=array1
        sum1=0
        for i in range(len(self.array1)):
            sum1+=self.array1[i]
        for j in range(len(self.array1[1])):
            for k in range(len(self.array1)):
                self.array1[k][j]=self.array1[k][j]/sum1[j] #dividing each element in a column by their sum
        return self.array1

    def summation(self,array2):
        list1=[]
        for i in range(len(array2)):
            sublist=[]
            sum2=array2[i].sum()
            sublist.append(sum2)
            list1.append(sublist) #putting them in this structure for representing they are in a column instead of a row
        array1=np.array(list1)
        return array1
    
    #To find w value of certain matrix.
    def calculate(self,array3):
        array3 = self.normalization(array3)
        array3 = self.summation(array3)
        array3 = self.normalization(array3)
        return array3

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#The code below is to compare the score of two companies in development situation part.
class Development_Situation(MatrixOperation):
    def __init__(self,informationList):
        self.returnOfEquity = []
        self.increaseRateRevenue = []
        self.scoreOfSatification = []
        self.environmentallyConsciousSupplyChainManagementLevel = []
        self.standardDischargeRateOfWaterPollutants = []
        self.solidWasteTreatmentRate = []
        self.greenhouseGasEmissions = [] 
        for i in informationList:
            self.returnOfEquity.append(i[0])
            self.increaseRateRevenue.append(i[1])
            self.scoreOfSatification.append(i[2])
            self.environmentallyConsciousSupplyChainManagementLevel.append(i[3])
            self.standardDischargeRateOfWaterPollutants.append(i[4])
            self.solidWasteTreatmentRate.append(i[5])
            self.greenhouseGasEmissions.append(i[6])
        self.weightJudgmentMatrix = np.array([[1,1,1.25,1.67,1.25,1.25,1],
                                              [1,1,1.25,1.67,1.25,1.25,1],
                                              [0.8,0.8,1,1.33,1,1,0.8],
                                              [0.6,0.6,0.75,1,0.75,0.75,0.6],
                                              [0.8,0.8,1,1.33,1,1,0.8],
                                              [0.8,0.8,1,1.33,1,1,0.8],
                                              [1,1,1.25,1.67,1.25,1.25,1]
                                              ])
        
    def createSubMatrixForEach(self,value1,value2):
        compare1 = value2 / value1
        compare2 = value1 / value2
        subJudgmentMatrix = np.array([[1,compare2],[compare1,1]],dtype=float)
        return subJudgmentMatrix
    
    def compare(self):
        w0 = self.calculate(self.weightJudgmentMatrix)
        w11 = self.calculate(self.createSubMatrixForEach(self.returnOfEquity[0],self.returnOfEquity[1]))
        w12 = self.calculate(self.createSubMatrixForEach(self.increaseRateRevenue[0],self.increaseRateRevenue[1]))
        w13 = self.calculate(self.createSubMatrixForEach(self.scoreOfSatification[0],self.scoreOfSatification[1]))
        w14 = self.calculate(self.createSubMatrixForEach(self.environmentallyConsciousSupplyChainManagementLevel[0],self.environmentallyConsciousSupplyChainManagementLevel[1]))
        w15 = self.calculate(self.createSubMatrixForEach(self.standardDischargeRateOfWaterPollutants[0],self.standardDischargeRateOfWaterPollutants[1]))
        w16 = self.calculate(self.createSubMatrixForEach(self.solidWasteTreatmentRate[0],self.solidWasteTreatmentRate[1]))
        w17 = self.calculate(self.createSubMatrixForEach(self.greenhouseGasEmissions[0],self.greenhouseGasEmissions[1]))
        w1 = []
        for i in range(2):
            intermediate = []
            intermediate.append(w11[i][0])
            intermediate.append(w12[i][0])
            intermediate.append(w13[i][0])
            intermediate.append(w14[i][0])
            intermediate.append(w15[i][0])
            intermediate.append(w16[i][0])
            intermediate.append(w17[i][0])
            w1.append(intermediate)
        
        result = []
        for i in range(len(w1)):
            intermediate = 0
            for j in range(len(w0)):
                intermediate += w1[i][j] * w0[j]
            result.append(intermediate[0])
        return result
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#The code below is to compare the score of two companies in potential development part.
class Potential_Development(MatrixOperation):
    def __init__(self,informationList):
        self.profitGrowthRate = []
        self.totalAssetsGrowthRate = []
        self.publicImpression = []
        self.socialWelfareContributionLevel = []
        self.environmentalProtectionInvestment = []
        self.reductionOnTHREEWASTES = []
        self.CO2EmissionGrowthRate = []
        self.energyGrowthRate = []
        self.growthRateOfnumberOfspecialists = []
        self.growthRateOfRDFunds = []
        self.ratioOfCostOnTraining = []
        self.greenCompetitiveness =[]
        for i in informationList:
            self.profitGrowthRate.append(i[0])
            self.totalAssetsGrowthRate.append(i[1])
            self.publicImpression.append(i[2])
            self.socialWelfareContributionLevel.append(i[3])
            self.environmentalProtectionInvestment.append(i[4])
            self.reductionOnTHREEWASTES.append(i[5])
            self.CO2EmissionGrowthRate.append(i[6])
            self.energyGrowthRate.append(i[7])
            self.growthRateOfnumberOfspecialists.append(i[8])
            self.growthRateOfRDFunds.append(i[9])
            self.ratioOfCostOnTraining.append(i[10])
            self.greenCompetitiveness.append(i[11])
        self.weightJudgmentMatrix = np.array([[1,1,1.25,1.25,1.67,2.5,1.67,2.5,2.5,2.5,2.5,5],
                                              [1,1,1.25,1.25,1.67,2.5,1.67,2.5,2.5,2.5,2.5,5],
                                              [0.8,0.8,1,1,1.33,2,1.33,2,2,2,2,4],
                                              [0.8,0.8,1,1,1.33,2,1.33,2,2,2,2,4],
                                              [0.6,0.6,0.75,0.75,1,1.5,1,1.5,1.5,1.5,1.5,3],
                                              [0.4,0.4,0.5,0.5,0.67,1,0.67,1,1,1,1,2],
                                              [0.6,0.6,0.75,0.75,1,1.5,1,1.5,1.5,1.5,1.5,3],
                                              [0.4,0.4,0.5,0.5,0.67,1,0.67,1,1,1,1,2],
                                              [0.4,0.4,0.5,0.5,0.67,1,0.67,1,1,1,1,2],
                                              [0.4,0.4,0.5,0.5,0.67,1,0.67,1,1,1,1,2],
                                              [0.4,0.4,0.5,0.5,0.67,1,0.67,1,1,1,1,2],
                                              [0.2,0.2,0.25,0.25,0.33,0.5,0.33,0.5,0.5,0.5,0.5,1]
                                              ])
        
    def createSubMatrixForEach(self,value1,value2):
        compare1 = value2 / value1
        compare2 = value1 / value2
        subJudgmentMatrix = np.array([[1,compare2],[compare1,1]],dtype=float)
        return subJudgmentMatrix
    
    def compare(self):
        w0 = self.calculate(self.weightJudgmentMatrix)
        w11 = self.calculate(self.createSubMatrixForEach(self.profitGrowthRate[0],self.profitGrowthRate[1]))
        w12 = self.calculate(self.createSubMatrixForEach(self.totalAssetsGrowthRate[0],self.totalAssetsGrowthRate[1]))
        w13 = self.calculate(self.createSubMatrixForEach(self.publicImpression[0],self.publicImpression[1]))
        w14 = self.calculate(self.createSubMatrixForEach(self.socialWelfareContributionLevel[0],self.socialWelfareContributionLevel[1]))
        w15 = self.calculate(self.createSubMatrixForEach(self.environmentalProtectionInvestment[0],self.environmentalProtectionInvestment[1]))
        w16 = self.calculate(self.createSubMatrixForEach(self.reductionOnTHREEWASTES[0],self.reductionOnTHREEWASTES[1]))
        w17 = self.calculate(self.createSubMatrixForEach(self.CO2EmissionGrowthRate[0],self.CO2EmissionGrowthRate[1]))
        w18 = self.calculate(self.createSubMatrixForEach(self.energyGrowthRate[0],self.energyGrowthRate[1]))
        w19 = self.calculate(self.createSubMatrixForEach(self.growthRateOfnumberOfspecialists[0],self.growthRateOfnumberOfspecialists[1]))
        w110 = self.calculate(self.createSubMatrixForEach(self.growthRateOfRDFunds[0],self.growthRateOfRDFunds[1]))
        w111 = self.calculate(self.createSubMatrixForEach(self.ratioOfCostOnTraining[0],self.ratioOfCostOnTraining[1]))
        w112 = self.calculate(self.createSubMatrixForEach(self.greenCompetitiveness[0],self.greenCompetitiveness[1]))
        w1 = []
        for i in range(2):
            intermediate = []
            intermediate.append(w11[i][0])
            intermediate.append(w12[i][0])
            intermediate.append(w13[i][0])
            intermediate.append(w14[i][0])
            intermediate.append(w15[i][0])
            intermediate.append(w16[i][0])
            intermediate.append(w17[i][0])
            intermediate.append(w18[i][0])
            intermediate.append(w19[i][0])
            intermediate.append(w110[i][0])
            intermediate.append(w111[i][0])
            intermediate.append(w112[i][0])
            w1.append(intermediate)
        result = []
        for i in range(len(w1)):
            intermediate = 0
            for j in range(len(w0)):
                intermediate += w1[i][j] * w0[j]
            result.append(intermediate[0])
        return result
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#The code below is to compare the score of two companies in development coordination part.
class Development_Coordination(MatrixOperation):
    def __init__(self,informationList):
        self.investmentElasticCoefficient = []
        self.ratioOfNumberOfManagers = []
        self.regionalContribution = []
        self.percentageOfmedicalInsurance = []
        self.abilityControlLevelOfThreeWaste = []
        self.abilityReduceCO2Emission = []
        self.strategyBeEnvironmentallyFriendly = []
        self.completenessOfManagementStrategies = []
        self.Creativity = []
        self.abilityReactToEmergency = []
        for i in informationList:
            self.investmentElasticCoefficient.append(i[0])
            self.ratioOfNumberOfManagers.append(i[1])
            self.regionalContribution.append(i[2])
            self.percentageOfmedicalInsurance.append(i[3])
            self.abilityControlLevelOfThreeWaste.append(i[4])
            self.abilityReduceCO2Emission.append(i[5])
            self.strategyBeEnvironmentallyFriendly.append(i[6])
            self.completenessOfManagementStrategies.append(i[7])
            self.Creativity.append(i[8])
            self.abilityReactToEmergency.append(i[9])
        self.weightJudgmentMatrix = np.array([[1,1.33,1.33,1.33,1.33,1.33,1,1,1,1],
                                              [0.75,1,1,1,1,1,0.75,0.75,0.75,0.75],
                                              [0.75,1,1,1,1,1,0.75,0.75,0.75,0.75],
                                              [0.75,1,1,1,1,1,0.75,0.75,0.75,0.75],
                                              [0.75,1,1,1,1,1,0.75,0.75,0.75,0.75],
                                              [0.75,1,1,1,1,1,0.75,0.75,0.75,0.75],
                                              [1,1.33,1.33,1.33,1.33,1.33,1,1,1,1],
                                              [1,1.33,1.33,1.33,1.33,1.33,1,1,1,1],
                                              [1,1.33,1.33,1.33,1.33,1.33,1,1,1,1],
                                              [1,1.33,1.33,1.33,1.33,1.33,1,1,1,1]
                                              ])
    
    def createSubMatrixForEach(self,value1,value2):
        compare1 = value2 / value1
        compare2 = value1 / value2
        subJudgmentMatrix = np.array([[1,compare2],[compare1,1]],dtype=float)
        return subJudgmentMatrix
    
    def compare(self):
        w0 = self.calculate(self.weightJudgmentMatrix)
        w11 = self.calculate(self.createSubMatrixForEach(self.investmentElasticCoefficient[0],self.investmentElasticCoefficient[1]))
        w12 = self.calculate(self.createSubMatrixForEach(self.ratioOfNumberOfManagers[0],self.ratioOfNumberOfManagers[1]))
        w13 = self.calculate(self.createSubMatrixForEach(self.regionalContribution[0],self.regionalContribution[1]))
        w14 = self.calculate(self.createSubMatrixForEach(self.percentageOfmedicalInsurance[0],self.percentageOfmedicalInsurance[1]))
        w15 = self.calculate(self.createSubMatrixForEach(self.abilityControlLevelOfThreeWaste[0],self.abilityControlLevelOfThreeWaste[1]))
        w16 = self.calculate(self.createSubMatrixForEach(self.abilityReduceCO2Emission[0],self.abilityReduceCO2Emission[1]))
        w17 = self.calculate(self.createSubMatrixForEach(self.strategyBeEnvironmentallyFriendly[0],self.strategyBeEnvironmentallyFriendly[1]))
        w18 = self.calculate(self.createSubMatrixForEach(self.completenessOfManagementStrategies[0],self.completenessOfManagementStrategies[1]))
        w19 = self.calculate(self.createSubMatrixForEach(self.Creativity[0],self.Creativity[1]))
        w110 = self.calculate(self.createSubMatrixForEach(self.abilityReactToEmergency[0],self.abilityReactToEmergency[1]))
        w1 = []
        for i in range(2):
            intermediate = []
            intermediate.append(w11[i][0])
            intermediate.append(w12[i][0])
            intermediate.append(w13[i][0])
            intermediate.append(w14[i][0])
            intermediate.append(w15[i][0])
            intermediate.append(w16[i][0])
            intermediate.append(w17[i][0])
            intermediate.append(w18[i][0])
            intermediate.append(w19[i][0])
            intermediate.append(w110[i][0])
            w1.append(intermediate)
        
        result = []
        for i in range(len(w1)):
            intermediate = 0
            for j in range(len(w0)):
                intermediate += w1[i][j] * w0[j]
            result.append(intermediate[0])
        return result

class pairRanking(MatrixOperation):
    def __init__(self,informationList):
        self.companyName = []
        self.developmentSituation = []
        self.potentialDevelopment = []
        self.developmentCoordination = []
        for i in informationList:
            self.companyName.append(i[0])
            self.developmentSituation.append(i[1])
            self.potentialDevelopment.append(i[2])
            self.developmentCoordination.append(i[3])
        self.weightJudgmentMatrix = np.array([[1,1.167,1.167],
                                              [0.857,1,1],
                                              [0.857,1,1]
                                              ])
        
    def createSubMatrixForEach(self,value1,value2):
        compare1 = value2 / value1
        compare2 = value1 / value2
        subJudgmentMatrix = np.array([[1,compare2],[compare1,1]],dtype=float)
        return subJudgmentMatrix
    
    def compare(self):
        w0 = self.calculate(self.weightJudgmentMatrix)
        w11 = self.calculate(self.createSubMatrixForEach(self.developmentSituation[0],self.developmentSituation[1]))
        w12 = self.calculate(self.createSubMatrixForEach(self.potentialDevelopment[0],self.potentialDevelopment[1]))
        w13 = self.calculate(self.createSubMatrixForEach(self.developmentCoordination[0],self.developmentCoordination[1]))
        w1 = []
        for i in range(2):
            intermediate = []
            intermediate.append(w11[i][0])
            intermediate.append(w12[i][0])
            intermediate.append(w13[i][0])
            w1.append(intermediate)
        
        result = []
        for i in range(len(w1)):
            intermediate = 0
            for j in range(len(w0)):
                intermediate += w1[i][j] * w0[j]
            result.append(intermediate[0])
        return result

class Ranking():
    def __init__(self,CompanyList):
        self.CompanyList = CompanyList
    
    def compareEntirely(self,company1,company2):
        infoSituation1 = company1[1:8]
        infoSituation2 = company2[1:8]
        infoPotential1 = company1[8:20]
        infoPotential2 = company2[8:20]
        infoCoordination1 = company1[20:]
        infoCoordination2 = company2[20:]
        listSituation = []
        listPotential = []
        listCoordination = []
        listSituation.append(infoSituation1)
        listSituation.append(infoSituation2)
        listPotential.append(infoPotential1)
        listPotential.append(infoPotential2)
        listCoordination.append(infoCoordination1)
        listCoordination.append(infoCoordination2)
        Situation = Development_Situation(listSituation)
        Potential = Potential_Development(listPotential)
        Coordination = Development_Coordination(listCoordination)
        resultSituation = Situation.compare()
        resultPotential = Potential.compare()
        resultCoordination = Coordination.compare()
        nameList = []
        nameList.append(company1[0])
        nameList.append(company2[0])
        final = []
        for i in range(2):
            final1 = []
            final1.append(nameList[i])
            final1.append(resultSituation[i])
            final1.append(resultPotential[i])
            final1.append(resultCoordination[i])
            final.append(final1)
        resultPair = pairRanking(final)
        out = resultPair.compare()
        if out[0] > out[1]:
            return 1
        else:
            return 0
        
    def Run(self):
        finalResultList = []
# This part is to rank each companies.
        for i in range(len(self.CompanyList)):
            
            if i < 1:
                pass
            elif len(finalResultList) == 0 and i == 1:
                c1 = self.CompanyList[0]
                c2 = self.CompanyList[1]
                finalResult = self.compareEntirely(c1, c2)
                if finalResult == 1:
                    finalResultList.append(c1)
                    finalResultList.append(c2)
                else:
                    finalResultList.append(c2)
                    finalResultList.append(c1)
            else:
                c1 = self.CompanyList[i]
                cList = finalResultList.copy()
                value = 0
                for j in range(len(cList)):
                    c2 = cList[j]
                    finalResult = self.compareEntirely(c1, c2)
                    value += finalResult
                    if value == 1:
                        finalResultList.insert(j-1,c1)
                if value == 0:
                    finalResultList.insert(-1,c1)
        return finalResultList
                    
#The "companyList" has sub lists which has forms of：
#[companyName, score1...score29]

CompanyList = [['company1',70,29,60,50,70,80,70,70,60,40,78,42,69,66,79,88,89,90,70,71,60,66,84,74,76,75,87,66,54],['company2',65,33,57,50,73,86,70,70,60,40,68,49,79,69,49,91,89,90,73,71,60,56,74,65,73,75,89,59,21],['company3',74,29,68,50,70,80,70,70,60,40,78,42,67,66,79,88,89,80,70,71,60,66,84,74,66,75,87,66,56],['company4',65,33,57,50,73,86,70,70,60,40,68,49,79,69,49,91,89,90,73,71,60,56,74,65,73,75,89,59,21]]
#The CompanyList above is include some examples.
Output = Ranking(CompanyList)
rank = Output.Run()
#The for loop below is to samplify the result without showing data.
for i in range(len(rank)):
    print(str(i+1)+"."+rank[i][0])
        
        
        