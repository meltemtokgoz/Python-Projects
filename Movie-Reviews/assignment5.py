import os
#**************************************STAGE 1**************************************************************************
dict_genre = {}
ugenreFile = open("u.genre","r")

for l in ugenreFile:
    l = l.rstrip('\n')
    name = l.split('|')[0]
    id = l.split('|')[1]
    dict_genre[id] = name
ugenreFile.close()

uitemFile = open("u.item","r")
group_lens_film = []
dict_film_id={}
dict_imdb_link={}
dict_all_films = {}

for line in uitemFile.readlines():
    line =line.rstrip("\n")
    line =line.split("|")
    line[1] = line[1].split("(")
    line[1][0] = line[1][0].rstrip(" ")
    x =line[1][0].lower()
    y =x.title()
    dict_film_id[y]=line[0]
    dict_imdb_link[y] = line[3]
    group_lens_film.append(y)
    dict_all_films[y] = {}
    dict_all_films[y]['title'] = y
    dict_all_films[y]['id'] = line[0]
    dict_all_films[y]['date'] = line[2]
    dict_all_films[y]['imdb'] = line[3]
    dict_all_films[y]['genres'] = [dict_genre[str(idx)] for idx, v in enumerate(line[4:]) if v == "1"]

uitemFile.close()

dennis_schwartz_film =[]
directory = os.path.normpath("film")
dennis_schwartz_film_reviews = {}
for subdir, dirs, files in os.walk(directory):
    for file in files:
        f=open(os.path.join(subdir, file),'r')
        total = f.readlines()
        a = total[0]
        a = a.rstrip("\n")
        a = a.split("(")
        a[0] =a[0].rstrip(" ")
        c = a[0].lower()
        d = c.title()
        dennis_schwartz_film.append(d)
        dennis_schwartz_film_reviews[d] = "".join(total[1:])
        f.close()
#**********************************STEP3********************************************************************************
output1= open("review.txt","w",encoding="utf-8")
common =[item for item in group_lens_film if item in dennis_schwartz_film]

class MyError(Exception):
    pass

for i in group_lens_film:
    try:
        if i in common:
            print(dict_film_id[i],i,"is found in folder", file=output1)
        if not i in  common:
           raise MyError
    except MyError:
        print(dict_film_id[i],i,"is not found in folder.Look at",dict_imdb_link[i], file=output1)
#***********************************************************************************************************************
udataFile =open("u.data","r")
data = []
for line1 in udataFile:
    line1=line1.rstrip("\n")
    line1=line1.split("\t")
    d = {}
    d["uid"]= line1[0]
    d["mid"]=line1[1]
    d["rating"]=line1[2]
    d["timestamp"]=line1[3]
    data.append(d)
udataFile.close()

dict_occupation = {}
uoccupationFile = open("u.occupation", "r")
for line3 in uoccupationFile:
    line3 = line3.rstrip('\n')
    line3 = line3.split("|")
    dict_occupation[line3[0]] = line3[1]
uoccupationFile.close()

uuserFile =open("u.user","r")
users = {}
for line2 in uuserFile:
    line2=line2.rstrip("\n")
    line2=line2.split("|")
    users[line2[0]] = {}
    users[line2[0]]["id"] = line2[0]
    users[line2[0]]["age"] = line2[1]
    users[line2[0]]["gender"] =line2[2]
    users[line2[0]]["occupation"]=  dict_occupation[line2[3]]
    users[line2[0]]["zip"]= line2[4]
uuserFile.close()
#*******************************************STEP4***********************************************************************
message = '''<html>
<head>
<title>{0}</title>
</head>
<body>
<font face="Times New Roman" font size="6" color="red"<b>{0}</b></font><br>
<b>Genre: </b>{1}<br>
<b>IMDB Link: </b><a href={2} >{0}</a><br>
<font face="Times New Roman" font size="4" color="black">
<b>Review: </b><br>{3}</font><br><br>
<b>Total User: {4}</b> / <b>Total Rate: {5}</b><br>
<br><b>User who rate the film: </b>
{6}
</body>
</html>'''

directory = "filmList"
if not os.path.exists(directory):
    os.makedirs(directory)

for c in common:
    mid = dict_film_id[c]
    f = open("filmList/" + mid + ".html", "w")
    cmessage = message
    title = c
    genres = " ".join(dict_all_films[title]["genres"])
    imdb = dict_all_films[title]["imdb"]
    review = dennis_schwartz_film_reviews[title]
    id = dict_all_films[title]["id"]
    voters = [d for d in data if id == d["mid"]]
    total_user = len(voters)
    total_vote = sum([float(r["rating"]) for r in voters])
    avg = 0
    try:
        avg = total_vote/total_user
    except ZeroDivisionError:
        pass
    users_rate_info = ""
    for item in voters:
        uid = item["uid"]
        s = "<b>User :</b>" + item["uid"] + " <b> Rate: </b>" + item["rating"] + "<br>"
        s += "<b>User Detail: </b> <b>Age: </b> " + users[uid]["age"] + " <b> Gender: </b> " + users[uid]["gender"]  +" <b> Occupation: </b> " + users[uid]["occupation"] + " <b> Zip Code: </b> " + users[uid]["zip"] + "<br>"
        users_rate_info += s

    cmessage = cmessage.format(title, genres, imdb, review, total_user, avg, users_rate_info)

    f.write(cmessage)
    f.close()

#**************************************STAGE 2**************************************************************************
import os
stop_words_file =open("stopwords.txt","r",encoding="utf8")
StopWord =[]
for s1 in stop_words_file:
    s1 = s1.rstrip("\n")
    StopWord.append(s1)

film_guess_dict = {}
unique_guess_dict = {}
unique_list =[]
directory = os.path.normpath("filmGuess")
for subdir, dirs, files in os.walk(directory):
    for file in files:
        f=open(os.path.join(subdir, file),'r')
        total = f.readlines()
        a = total[0]
        a = a.rstrip("\n")
        a = a.split("(director")
        a[0] =a[0].rstrip(" ")
        c = a[0].lower()
        d = c.title()
        review =" ".join(total[1:])
        film_guess_dict[d] =review
        for word in review.split(' '):
            word = word.lower()
            word = word.rstrip("\n")
            if word in StopWord:
                continue
            if not word in StopWord:
                unique_list.append(word)
        unique_guess_dict[d]= set(unique_list)
        unique_list = []
        f.close()

unknown_unique =[]
Action_unique =[]
Adventure_unique =[]
Animation_unique =[]
Childrens_unique =[]
Comedy_unique =[]
Crime_unique =[]
Documentary_unique =[]
Drama_unique =[]
Fantasy_unique =[]
FilmNoir_unique =[]
Horror_unique =[]
Musical_unique =[]
Mystery_unique =[]
Romance_unique =[]
SciFi_unique =[]
Thriller_unique =[]
War_unique =[]
Western_unique =[]


unique_genres_dict ={}
directory = os.path.normpath("film")
dennis_schwartz_film_reviews = {}
for subdir, dirs, files in os.walk(directory):
    for file in files:
        f=open(os.path.join(subdir, file),'r')
        total = f.readlines()
        a = total[0]
        a = a.rstrip("\n")
        a = a.split("(")
        a[0] = a[0].rstrip(" ")
        c = a[0].lower()
        e = c.title()
        review2 ="".join(total[1:])
        dennis_schwartz_film_reviews[e] = review2
        for word2 in review2.split(' '):
            word2 = word2.lower()
            if word2 in StopWord:
                continue
            if not word2 in StopWord:
                for ff in dict_all_films[e]["genres"]:
                    if ff == 'Action':
                        Action_unique.append(word2)
                    if ff == 'unknown':
                        unknown_unique.append(word2)
                    if ff == 'Adventure':
                        Adventure_unique.append(word2)
                    if ff == 'Animation':
                        Animation_unique.append(word2)
                    if ff == "Children's":
                        Childrens_unique.append(word2)
                    if ff == 'Comedy':
                        Comedy_unique.append(word2)
                    if ff == 'Crime':
                        Crime_unique.append(word2)
                    if ff == 'Documentary':
                        Documentary_unique.append(word2)
                    if ff == 'Drama':
                        Drama_unique.append(word2)
                    if ff == 'Fantasy':
                        Fantasy_unique.append(word2)
                    if ff == 'Film-Noir':
                        FilmNoir_unique.append(word2)
                    if ff == 'Horror':
                        Horror_unique.append(word2)
                    if ff == 'Musical':
                        Musical_unique.append(word2)
                    if ff == 'Mystery':
                        Mystery_unique.append(word2)
                    if ff == 'Romance':
                        Romance_unique.append(word2)
                    if ff == 'Sci-Fi':
                        SciFi_unique.append(word2)
                    if ff == 'Thriller':
                        Thriller_unique.append(word2)
                    if ff == 'War':
                        War_unique.append(word2)
                    if ff == 'Western':
                        Western_unique.append(word2)
        f.close()

output2= open("filmGenre.txt","w")

print("Guess Genres of Movie based on Movies", file=output2)

total_unknown =[]
total_action =[]
total_Adventure =[]
total_Animation =[]
total_Childrens =[]
total_Comedy = []
total_Crime = []
total_Documentary = []
total_Drama = []
total_Fantasy = []
total_FilmNoir = []
total_Horror = []
total_Musical = []
total_Mystery = []
total_Romance = []
total_SciFi = []
total_Thriller = []
total_War = []
total_Western = []

for k in (unique_guess_dict.keys()):
    for i in unique_guess_dict[k]:
        if i in set(Action_unique):
            total_action.append(i)
    if len(total_action) >= 20:
        q = ("Action")
    total_action =[]
    for i in unique_guess_dict[k]:
        if i in set(Adventure_unique):
            total_Adventure.append(i)
    if len(total_Adventure) >= 20:
        q += (" Adventure")
    total_Adventure =[]
    for i in unique_guess_dict[k]:
        if i in set(Animation_unique):
            total_Animation.append(i)
    if len(total_Animation) >= 20:
        q += (" Animation")
    total_Animation =[]
    for i in unique_guess_dict[k]:
        if i in set(Childrens_unique):
            total_Childrens.append(i)
    if len(total_Childrens) >= 20:
        q += (" Children's")
    total_Childrens =[]
    for i in unique_guess_dict[k]:
        if i in set(Comedy_unique):
            total_Comedy.append(i)
    if len(total_Comedy) >= 20:
        q += (" Comedy")
    total_Comedy = []
    for i in unique_guess_dict[k]:
        if i in set(Crime_unique):
            total_Crime.append(i)
    if len(total_Crime) >= 20:
        q += (" Crime")
    total_Crime = []
    for i in unique_guess_dict[k]:
        if i in set(Documentary_unique):
            total_Documentary.append(i)
    if len(total_Documentary) >= 20:
        q += (" Documentary")
    total_Documentary = []
    for i in unique_guess_dict[k]:
        if i in set(Drama_unique):
            total_Drama.append(i)
    if len(total_Drama) >= 20:
        q += (" Drama")
    total_Drama = []
    for i in unique_guess_dict[k]:
        if i in set(Fantasy_unique):
            total_Fantasy.append(i)
    if len(total_Fantasy) >= 20:
        q +=(" Fantasy")
    total_Fantasy = []
    for i in unique_guess_dict[k]:
        if i in set(FilmNoir_unique):
            total_FilmNoir.append(i)
    if len(total_FilmNoir) >= 20:
        q += (" Film-Noir")
    total_FilmNoir = []
    for i in unique_guess_dict[k]:
        if i in set(Horror_unique):
            total_Horror.append(i)
    if len(total_Horror) >= 20:
        q += (" Horror")
    total_Horror = []
    for i in unique_guess_dict[k]:
        if i in set(Musical_unique):
            total_Musical.append(i)
    if len(total_Musical) >= 20:
        q +=(" Musical")
    total_Musical = []
    for i in unique_guess_dict[k]:
        if i in set(Mystery_unique):
            total_Mystery.append(i)
    if len(total_Mystery) >= 20:
        q += (" Mystery")
    total_Mystery = []
    for i in unique_guess_dict[k]:
        if i in set(Romance_unique):
            total_Romance.append(i)
    if len(total_Romance) >= 20:
        q += (" Romance")
    total_Romance = []
    for i in unique_guess_dict[k]:
        if i in set(SciFi_unique):
            total_SciFi.append(i)
    if len(total_SciFi) >= 20:
        q += (" Sci-Fi")
    total_SciFi = []
    for i in unique_guess_dict[k]:
        if i in set(Thriller_unique):
            total_Thriller.append(i)
    if len(total_Thriller) >= 20:
        q += (" Thriller")
    total_Thriller = []
    for i in unique_guess_dict[k]:
        if i in set(War_unique):
            total_War.append(i)
    if len(total_War) >= 20:
        q += (" War")
    total_War = []
    for i in unique_guess_dict[k]:
        if i in set(Western_unique):
            total_Western.append(i)
    if len(total_Western) >= 20:
        q += (" Western")
    total_Western = []
    for i in unique_guess_dict[k]:
        if i in set(unknown_unique):
            total_unknown.append(i)
    if len(total_unknown) >= 20:
        q += (" unknown")
    total_unknown =[]
    print(k.upper(), ":", q ,file=output2)

output2.close()
