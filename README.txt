python=3.7
STEP 1: Libraries required are
-request
-sqlite3
-json
-flask
-colorama

STEP 2: check the directory as following:
eat_project/
├── get_data.py
├── clean_json.py
├── app.py
└── templates/
    ├── index.html
    └── restaurant.html
Data files "all_data.json" and "eat_task.db" are also included in this repo. If you want to generate yourself, delete them. Then go with following steps.

STEP 3: open "eat_project" folder in VS Code (or other IDE you like, but do not use google colab (it will not work for app.py because it need to use flask-ngrok.)

STEP 4: run get_data.py  -- generate all_data.json 

if you already have all_data.json, you can choose to skip step 4

STEP 5: run clean_json.py  -- generated eat_task.db

According to requirement, the code will only process the first 10 restaurant data. 
If you want the full data get processed and shown later on the webpage, in the clean_data method, delete [:10] to the for loop iteration over the restaurants' data. so it becomes:
for restaurant in data['restaurants']: I 

The existing eat_task.db stored all restaurants records of their id, name, rating, address and cuisines, and if you actually want to see the full record, you can choose to skip step 4. Otherwise delete the existing eat_task.db

STEP 6: run app.py
click the link in terminal and go to be webpage.

STEP 7: select the restaurant name, click show details, then you will see the cuisines, rating and address as well as the retaurant name.

Assumption/things not clear to me:
1.The requirement only mentioned build an interface, but I'm not sure it shall be interactive or not, so I think it's more safte to make it interactive.
2.It was not mentioned that how shall we present the "cuisines" data, so to reduce the data complexity, I extract the name of the different cuisine as string, and merge them into one string, seperated by "|". 
3.The content of cuisines is a bit confusing for me as some of them are not on the level in semantics. 
4.It's relative small amount of data, I‘m not sure about the reason for limiting it for only show the first 10 records? Or shall I use Dataframe so it saves more time and trouble?

Improvement I want to make:
Make the webpage more pretty with css. 
Add a fuction that aLLow to filter restaurant according to the cuisines content.



