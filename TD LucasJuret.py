from MaBase_MIB import *

# Question 1 

q1={gardien.Nom for gardien in BaseGardiens }


# Question 2 

q2= { agent.Ville for agent in BaseAgents }


# Question 3 

q3={ (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine }



# Question 4

q4={ (alien.Nom, cabine.NoAllee) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine==cabine.NoCabine }


# Question 5 

q5={ (alien.Nom) for alien in BaseAliens for cabine in BaseCabines if alien.NoCabine==cabine.NoCabine and cabine.NoAllee=='2'}


# Question 6

q6={ (alien.Planete) for alien in BaseAliens if float(alien.NoCabine)%2==0 }



# Question 7 

q7={ (alien.Nom) for alien in BaseAliens for gardien in BaseGardiens for agent in BaseAgents if alien.NoCabine==gardien.NoCabine and gardien.Nom==agent.Nom and agent.Ville=='Terminus'}



# Question 8 

q8={ (gardien.Nom) for gardien in BaseGardiens for alien in BaseAliens for miam in BaseMiams if miam.Aliment=='Bortsch' and miam.NomAlien==alien.Nom and alien.Sexe=='F' and alien.NoCabine==gardien.NoCabine }



# Question 9 

q9={ (cabine.NoCabine) for cabine in BaseCabines for gardien in BaseGardiens for alien in BaseAliens for agent in BaseAgents if (gardien.Nom==agent.Nom and agent.Ville=='Terminus' and gardien.NoCabine==cabine.NoCabine) or (alien.Sexe=='F' and alien.NoCabine==cabine.NoCabine) }



# Question 10 

q10={ (gardien.Nom,miam.Aliment) for gardien in BaseGardiens for miam in BaseMiams for alien in BaseAliens if miam.NomAlien==alien.Nom and alien.NoCabine==gardien.NoCabine and miam.Aliment[0]==gardien.Nom[0] }



# Question 11

q11={ (alien.Nom) for alien in BaseAliens if alien.Planete=='Euterpe' }



# Question 12

q12={ (alien.nom) for alien in BaseAliens if NomAliens=='x' }


# Question 13

q13={ (alien.nom,gardien.nom,agent.terminus) for alien in BaseAliens for gardien in BaseAliens for agent in BaseAliens if alien.NomAlien==x and gardien.NomVille=='Terminus' and gardien.NomGardians==x)



# Question 14 Existe-t-il un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terminus ?

q14={ (alien.sexe,alien.planete,miam.aliment,agent.ville) for alien in BaseAliens for miam in BaseAliens for agent in BaseAliens if alien.SexeAlien=='M' and alien.NomPlanete=='Trantor' and miam.Aliment=='Bortsch' and agent.NomVille='Terminus')                                                                 




