
# dictionary like a table 

d = {};

d["Gorge"] = 24;
# print(d);

d["Tom"] = 32;
# print(d)


# print(d["Gorge"],d["Tom"]);

# update gorge value
d["Gorge"] = 20;
# print(d.items())


# iterate dictionary key value
for key, value in d.items():
    print('Key : ',key,"value : ", value);
    print();

