like_cock = input() # 0 = No, 1 = Yes
like_vagina = input() # 0 = No, 1 = Yes
sex = input() # 0 = Male, 1 = Female.
gay_percent = 0
is_asesexual = 0

if int(sex) == 0:
 if int(like_cock) == 1:
  gay_percent += 50
  
 if int(like_vagina) == 0:
  if int(like_cock) == 0:
   is_asesexual = 1
  
  else:
   gay_percent += 50

 if int(is_asesexual) == 1:
  print("asesexual")

 else:
  print(str(gay_percent) + "%" + " Gay.")
 
if int(sex) == 1:
 if int(like_cock) == 0:
  if int(like_vagina) == 0:
   is_asesexual = 1
   
  else:
   gay_percent += 50

 if int(like_vagina) == 1:
  gay_percent += 50

 if int(is_asesexual) == 1:
  print("asesexual")

 else:
  print(str(gay_percent) + "%" + " Lesbian.")