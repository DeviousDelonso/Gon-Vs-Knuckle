def Gon():  # G for Gon
    GtotalAura = 21500
    Gabilities_li = ["Jajanken Rock", "Jajanken Paper", "Jajanken Scissors", "Offensive Ryu"]
    GabilitiesAura_li = [2000,2000,2000,1700]
    GabilitiesDamage_li = [2000,500,500,400]


    return GtotalAura, Gabilities_li, GabilitiesAura_li, GabilitiesDamage_li

def Knuckle(): #K for Knuckle
    KtotalAura = 45000
    Kabilities_li = ["Haymaker","Kick","Uppercut","Blitz"]
    KabilitiesAura_li = [2000,2000,2000,6000]
    KabilitiesDamage_li = [500,600,700,1800]
    auraLent_li = [500,400,300,1200]

    return KtotalAura, Kabilities_li, KabilitiesAura_li, KabilitiesDamage_li, auraLent_li

def Battle(GtotalAura,Gabilities_li,GabilitiesAura_li,GabilitiesDamage_li,KtotalAura,Kabilities_li,KabilitiesAura_li,KabilitiesDamage_li,auraLent_li):
    auraDebt = 0

    while GtotalAura > 1700:
        import random
        randomKnuckle1 = random.randrange(0,3)
        randomKnuckle2 = random.randrange(0,25)
        randomGon2 = random.randrange(0,5)
    
        print("------------------------------------------------------------------------------------------------------------------------")
        print("Jajanken Rock: Costs 2000 aura, deals 2000 aura(damage). Jajanken Paper: Costs 2000 aura, deals 500 aura(damage), can be used as a feint for Rock. Jajanken Scissors: Costs 2000 aura, deals 500 aura(damage), can be used as a feint for Rock. Offensive Ryu: Costs 1700 aura, can deal 400, 500 or 600 aura.")
        userChoice = str(input("What do you choose: "))
        if userChoice == Gabilities_li[0]:
            if random.randrange(0,10) == 7:
                GtotalAura -= GabilitiesAura_li[0]
                auraDebt -= GabilitiesDamage_li[0]
                print("Gon landed Jajanken Rock on Knuckle.")
                if auraDebt >= 0:
                    print("But Gon's Aura Debt covers this damage.")
                    print("Knuckle received no aura.")
                    print(f"Gon paid back {GabilitiesDamage_li[0]} of his debt, it is now at {auraDebt} aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    KtotalAura -= GabilitiesDamage_li[0]
                    print("Knuckle received 2000 aura in damage.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
            else:
                GtotalAura -= GabilitiesAura_li[0]
                if auraDebt >= 0:
                    print("Jajanken Rock did not connect.")
                    print("Knuckle received no aura.")
                    print(f"Gon did not land a hit and so repaid no aura. He has a debt of {auraDebt} aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Jajanken Rock did not connect.")
                    print("Knuckle received no aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                
        elif userChoice == Gabilities_li[1]:
            feint = str(input("Do you wish to attempt a feint into Rock (if so, you MUST say Yae): "))
            if feint == "Yae":
                GtotalAura -= (GabilitiesAura_li[0] + GabilitiesAura_li[1])
                if randomGon2 == 3:
                    KtotalAura -= (GabilitiesDamage_li[0] + GabilitiesDamage_li[1])
                    auraDebt -= GabilitiesDamage_li[1]
                    print("Gon threw Paper as a feint, managing to hit Knuckle with a surprise Rock.")
                    if auraDebt >= 0:
                        print("But Gon's Aura Debt covers this damage.")
                        print("Knuckle received no aura.")
                        print(f"Gon paid back {GabilitiesDamage_li[1]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                    else:   
                        print("Knuckle received 2500 aura in damage.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    KtotalAura -= GabilitiesDamage_li[1]
                    auraDebt -= GabilitiesDamage_li[1]
                    print("Gon threw Paper as a feint but did not manage to hit Knuckle with Rock.")
                    if auraDebt >= 0:
                        KtotalAura -= auraLent_li[1]
                        print("But Gon's Aura debt covers this damage.")
                        print("Knuckle received no aura.")
                        print(f"Gon paid back {GabilitiesDamage_li[1]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                    else:
                        print("Knuckle received 500 aura in damage.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")            
            else:
                KtotalAura -= GabilitiesDamage_li[1]
                GtotalAura -= GabilitiesAura_li[1]
                auraDebt -= GabilitiesDamage_li[1]
                print("Gon threw Paper at Knuckle. It connected.")
                if auraDebt >= 0:
                        KtotalAura -= auraLent_li[1]
                        print("But Gon's Aura debt covers this damage.")
                        print("Knuckle received no aura in damage.")
                        print(f"Gon paid back {GabilitiesDamage_li[1]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Knuckle received 500 aura in damage.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")  

        elif userChoice == Gabilities_li[2]:
            feint = str(input("Do you wish to attempt a feint into Rock (if so, you MUST say Yae): "))
            if feint == "Yae":
                GtotalAura -= (GabilitiesAura_li[0] + GabilitiesAura_li[2])
                if randomGon2 == 4:
                    KtotalAura -= (GabilitiesDamage_li[0]) + (GabilitiesDamage_li[2])
                    auraDebt -= GabilitiesDamage_li[2]
                    print("Gon slashed Scissors as a feint, managing to hit Knuckle with a surprise Rock.")
                    if auraDebt >= 0:
                        KtotalAura -= auraLent_li[2]
                        print("But Gon's Aura debt covers this damage.")
                        print("Knuckle received no aura.")
                        print(f"Gon paid back {GabilitiesDamage_li[2]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                    else:
                        print("Knuckle received 2500 aura in damage.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    KtotalAura -= GabilitiesDamage_li[2]
                    auraDebt -= GabilitiesDamage_li[2]
                    print("Gon slashed Scissors as feint but did not manage to hit Knuckle with Rock.")
                    if auraDebt >= 0:
                        KtotalAura -= auraLent_li[2]
                        print("But Gon's Aura debt covers this damage.")
                        print("Knuckle received no aura.")
                        print(f"Gon paid back {GabilitiesDamage_li[2]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                    else:
                        print("Knuckle received 500 aura in damage.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")       
            else:
                KtotalAura -= GabilitiesDamage_li[2]
                GtotalAura -= GabilitiesAura_li[2]
                auraDebt -= GabilitiesDamage_li[2]
                print("Gon slashed Scissors at Knuckle. It connected.")
                if auraDebt >= 0:
                        KtotalAura -= auraLent_li[2]
                        print("But Gon's Aura debt covers this damage.")
                        print("Knuckle received no aura.")
                        print(f"Gon paid back {GabilitiesDamage_li[2]} of his debt, it is now at {auraDebt} aura.")
                        print(f"Gon has {GtotalAura} aura remaining.")
                        print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Knuckle received 500 aura in damage.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")

        elif userChoice == Gabilities_li[3]:
            if random.randrange(0,4) == 2:
                GabilitiesDamage_li[3] = 500
                KtotalAura -= GabilitiesDamage_li[3]
                GtotalAura -= GabilitiesAura_li[3]
                auraDebt -= GabilitiesDamage_li[3]
                print("In a flurry of Ryu, Gon lands two hits.")
                if auraDebt >= 0:
                    KtotalAura -= auraLent_li[3]
                    print("But Gon's Aura debt covers this damage.")
                    print("Knuckle received no aura.")
                    print(f"Gon paid back {GabilitiesDamage_li[3]} of his debt, it is now at {auraDebt} aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Knuckle received 500 aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")     
            elif randomGon2 == 3:
                GabilitiesDamage_li[3] = 600
                KtotalAura -= GabilitiesDamage_li[3]
                GtotalAura -= GabilitiesAura_li[3]
                auraDebt -= GabilitiesDamage_li[3]
                print("In a flurry of Ryu, Gon lands three hits.")
                if auraDebt >= 0:
                    KtotalAura -= auraLent_li[3]
                    print("But Gon's Aura debt covers this damage.")
                    print("Knuckle received no aura.")
                    print(f"Gon paid back {GabilitiesDamage_li[3]} of his debt, it is now at {auraDebt} aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Knuckle received 600 aura in damage.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
            else:
                KtotalAura -= GabilitiesDamage_li[3]
                GtotalAura -= GabilitiesAura_li[3]
                auraDebt -= GabilitiesDamage_li[3]
                print("In a flurry of Ryu, Gon lands one hit.")
                if auraDebt >= 0:
                    KtotalAura -= auraLent_li[3]
                    print("But Gon's Aura debt covers this damage.")
                    print("Knuckle received no aura.")
                    print(f"Gon paid back {GabilitiesDamage_li[3]} of his debt, it is now at {auraDebt} aura.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                else:
                    print("Knuckle received 400 aura in damage.")
                    print(f"Gon has {GtotalAura} aura remaining.")
                    print(f"Knuckle has {KtotalAura} aura remaining.")
                    
        print("------------------------------------------------------------------------------------------------------------------------")
        if randomKnuckle2 == 7:
            GtotalAura -= KabilitiesDamage_li[3]
            KtotalAura -= KabilitiesAura_li[3]
            auraDebt += auraLent_li[3]
            print("Showing his superiority in speed, Knuckle Blitzes Gon. Sending a Haymaker, Kick and Uppercut to the poor child.")
            print("Gon receives 1800 aura in damage.")
            if auraDebt > 0:
                auraDebt = 0
                auraDebt += auraLent_li[3]
                print(f"Gon now owes APR {auraDebt} aura.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            elif auraDebt < 0:
                print("Gon doesn't owe APR anything.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            
                
                
        elif randomKnuckle1 == 0:
            GtotalAura -= KabilitiesDamage_li[0]
            KtotalAura -= KabilitiesAura_li[0]
            auraDebt += auraLent_li[0]
            print("Knuckle sends a crushing Haymaker towards Gon.")
            print("Gon receives 500 aura in damage.")
            if auraDebt > 0:
                auraDebt = 0
                auraDebt += auraLent_li[0]
                print(f"Gon now owes APR {auraDebt} aura.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            elif auraDebt < 0:
                print("Gon doesn't owe APR anything.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
        elif randomKnuckle1 == 1:
            GtotalAura -= KabilitiesDamage_li[1]
            KtotalAura -= KabilitiesAura_li[1]
            auraDebt += auraLent_li[1]
            print("Knuckle sends a crushing Kick towards Gon.")
            print("Gon receives 600 aura in damage.")
            if auraDebt > 0:
                auraDebt = 0
                auraDebt += auraLent_li[1]
                print(f"Gon now owes APR {auraDebt} aura.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            elif auraDebt < 0:
                print("Gon doesn't owe APR anything.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
        elif randomKnuckle1 == 2:
            GtotalAura -= KabilitiesDamage_li[2]
            KtotalAura -= KabilitiesAura_li[2]
            auraDebt += auraLent_li[2]
            print("Knuckle launches a jarring Uppercut on Gon.")
            print("Gon receives 700 aura in damage.")
            if auraDebt > 0:
                auraDebt = 0
                auraDebt += auraLent_li[2]
                print(f"Gon now owes APR {auraDebt} aura.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            elif auraDebt < 0:
                print("Gon doesn't owe APR anything.")
                print(f"Gon has {GtotalAura} aura remaining.")
                print(f"Knuckle has {KtotalAura} aura remaining.")
            
            
            
            
            
                
                
            
                
                    
                    
            
        
            
    
    
    

GonTotalAura, GonAbilities, GonAbilitiesAura, GonAbilitiesDamage = Gon()
KnuckleTotalAura, KnuckleAbilities, KnuckleAbilitiesAura, KnuckleAbilitiesDamage, auraLent = Knuckle()

print(Battle(GonTotalAura,GonAbilities,GonAbilitiesAura,GonAbilitiesDamage,KnuckleTotalAura,KnuckleAbilities,KnuckleAbilitiesAura,KnuckleAbilitiesDamage,auraLent))
