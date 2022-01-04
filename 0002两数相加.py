class sumDouble():
    def doublesum(self,listA,listB):
        lengthA=len(listA)
        lengthB=len(listB)

        if(lengthA==0 and lengthB==0):
            print("两列表为空")
            return 0
        if(lengthA==0 and lengthB!=0):
            print(listB)
            return 0
        if(lengthB==0 and lengthA!=0):
            print(listA)
            return 0

        per =0
        i=0
        result=[]
        if lengthB>=lengthA:
            while(i<lengthA):
                sum =listA[i]+listB[i]+per
                per =sum//10
                cur =sum%10
                result.append(cur)
                i=i+1

            while(i<lengthB):
                sum = listB[i] + per
                per = sum // 10
                cur = sum % 10
                result.append(cur)
                i = i + 1
            if (per > 0):
                result.append(per)
            print("result", result)

        else:
            while(i<lengthB):
                sum =listA[i]+listB[i]+per
                per =sum//10
                cur =sum%10
                result.append(cur)
                i=i+1

            while(i<lengthA):
                sum = listA[i] + per
                per = sum // 10
                cur = sum % 10
                result.append(cur)
                i = i + 1

            if(per>0):
                result.append(per)
            print("result", result)
        return 0


S=sumDouble()
A=[9,9,9,9,9,9,9]
B=[9,9,9,9]

C=[2,4,3]
D=[5,6,4]

S.doublesum(C,D)